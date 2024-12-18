from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
import os
import redis
import json

# Настройка SQLAlchemy
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db/postgres")
engine = create_engine(DATABASE_URL)

REDIS_URL = os.getenv("REDIS_URL", "redis://cache:6379/0")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель SQLAlchemy
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    login = Column(String, index=True)
    hashed_password = Column(String, index=False)

    @property
    def password(self):
        raise AttributeError('Password is not readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Income_Expense(Base):
    __tablename__ = "Income_Expense"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    Income_Expense_name = Column(String, index=True)
    Income_Expense_body = Column(String, index=False)
    amount = Column(Float, index=True)

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Модель Pydantic для валидации данных
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str 
    login: str 
    hashed_password: str

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str 
    login: str 
    hashed_password: str

    class Config:
        orm_mode = True

class Income_ExpenseCreate(BaseModel):
    Income_Expense_name: str
    Income_Expense_body: str
    amount: int

class Income_ExpenseResponse(BaseModel):
    id: int
    user_id: int
    Income_Expense_name: str
    Income_Expense_body: str
    amount: int

    class Config:
        orm_mode = True

app = FastAPI()

# Зависимости для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания пользователя
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db), tags=["Users"]):
    users_db = User(**user.dict())
    db.add(users_db)
    db.commit()
    db.refresh(users_db)
    return users_db

# Маршрут для получения пользователя по id
@app.get("/users/{user_id}", response_model=UserResponse, tags=["Users"])
def get_user(user_id: int, db: Session = Depends(get_db)):
    cache_key = f"user:{user_id}"
    if redis_client.exists(cache_key):
        print('# from_cache')
        cached_user = redis_client.get(cache_key)
        return json.loads(cached_user)
    else:
        user = db.query(User).filter(User.id == user_id).first()
        user_json = dict()
        for k in user.__dict__:
            if k != '_sa_instance_state':
                user_json[k] = user.__dict__[k]

        if user:
            redis_client.set(cache_key, json.dumps(user_json),ex = 60)
        else:
            raise HTTPException(status_code=404, detail="User not found")
        return user

# Маршрут для получения всех пользователей
@app.get("/users/", response_model=list[UserResponse], tags=["Users"])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Маршрут для создания дохода/расхода
@app.post("/Income_Expense/", response_model=Income_ExpenseResponse)
def create_user(user: Income_ExpenseCreate, db: Session = Depends(get_db), tags=["Income_Expense"]):
    Income_Expense_db = Income_Expense(**Income_Expense.dict())
    db.add(Income_Expense_db)
    db.commit()
    db.refresh(Income_Expense_db)
    return Income_Expense_db

# Маршрут для получения всех доходов/расходов по id пользователя
@app.get("/Income_Expense/", response_model=list[Income_ExpenseResponse], tags=["Income_Expense"])
def get_all_Income_Expense(db: Session = Depends(get_db)):
    Income_Expense_all = db.query(Income_Expense).all()
    return Income_Expense_all

# Запуск сервера
#if __name__ == "__main__":
   # import uvicorn
   # uvicorn.run(app, host="0.0.0.0", port=8000)