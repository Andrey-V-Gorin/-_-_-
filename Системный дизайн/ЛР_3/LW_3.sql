# create table
CREATE TABLE IF NOT EXISTS users (id INT, last_name VARCHAR(255), first_name VARCHAR(255), email VARCHAR(255), login VARCHAR(20), hashed_password VARCHAR(200), age INT);
CREATE TABLE IF NOT EXISTS Income_Expense (id INT, users_id INT, Income_Expense_name VARCHAR(50), Income_Expense_body VARCHAR(255), amount INT);

# create sequence
CREATE SEQUENCE IF NOT EXISTS users_id_seq START 1;

SELECT * from users;

select NEXTVAL('users_id_seq');

INSERT INTO users (id, first_name, last_name, email, login, hashed_password, age) VALUES (NEXTVAL ('users_id_seq'),'Petr', 'Petrov', 'pp@yandex.ru', 'Petr_killer', MD5(CONCAT('12345', 'salt')), '23');
INSERT INTO users (id, first_name, last_name, email, login, hashed_password, age) VALUES (NEXTVAL ('users_id_seq'),'Andr', 'Ezhof', 'ae@yandex.ru', 'Ezhof_777', MD5(CONCAT('hgt78', 'salt')), '33');
INSERT INTO users (id, first_name, last_name, email, login, hashed_password, age) VALUES (NEXTVAL ('users_id_seq'),'Ivan', 'Ivanov', 'ii@yandex.ru', 'king', MD5(CONCAT('w3%7h', 'salt')), '25');

CREATE SEQUENCE IF NOT EXISTS Income_Expense_id_seq START 1;


SELECT * from Income_Expense;

select NEXTVAL('Income_Expense_id_seq');

INSERT INTO Income_Expense (id, users_id, Income_Expense_name, Income_Expense_body, amount) VALUES (NEXTVAL ('Income_Expense_id_seq'), '46', 'Income', 'Зарплата', '120000');
INSERT INTO Income_Expense (id, users_id, Income_Expense_name, Income_Expense_body, amount) VALUES (NEXTVAL ('Income_Expense_id_seq'), '47','Expense', 'Магазин', '10000');
INSERT INTO Income_Expense (id, users_id, Income_Expense_name, Income_Expense_body, amount) VALUES (NEXTVAL ('Income_Expense_id_seq'), '48','Expense', 'АЗС', '3000');
INSERT INTO Income_Expense (id, users_id, Income_Expense_name, Income_Expense_body, amount) VALUES (NEXTVAL ('Income_Expense_id_seq'), '47','Income', 'Дивиденды', '300000');
INSERT INTO Income_Expense (id, users_id, Income_Expense_name, Income_Expense_body, amount) VALUES (NEXTVAL ('Income_Expense_id_seq'), '48','Expense', 'Рестораны', '5000');

# create index
CREATE UNIQUE INDEX users_email ON users (email);
CREATE UNIQUE INDEX users_login ON users (login);
CREATE UNIQUE INDEX Income_Expense_id ON Income_Expense (id);
create index inb_in on Income_Expense (Income_Expense_body);
create index a_in on Income_Expense (amount);
create index inn_in on Income_Expense (Income_Expense_name);

# select
SELECT * from users WHERE email like 'ae@yandex.ru';
SELECT * from users WHERE email like 'pp@yandex.ru';
SELECT * from users WHERE email like 'ii@yandex.ru';
SELECT * from users WHERE login like 'Petr_killer';
SELECT * from users WHERE login like 'Ezhof_777';
SELECT * from users WHERE login like 'king';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_name like 'Income';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_name like 'Income';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_name like 'Income';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_name like 'Expense';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_name like 'Expense';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_name like 'Expense';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_body like 'Дивиденды';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_body like 'Дивиденды';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_body like 'Дивиденды';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_body like 'Магазин';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_body like 'Магазин';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_body like 'Магазин';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_body like 'Рестораны';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_body like 'Рестораны';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_body like 'Рестораны';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_body like 'Зарплата';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_body like 'Зарплата';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_body like 'Зарплата';
SELECT * from Income_Expense WHERE users_id = 46 and Income_Expense_body like 'АЗС';
SELECT * from Income_Expense WHERE users_id = 47 and Income_Expense_body like 'АЗС';
SELECT * from Income_Expense WHERE users_id = 48 and Income_Expense_body like 'АЗС';
SELECT * from Income_Expense WHERE users_id = 48 and amount = 3000;
SELECT * from Income_Expense WHERE users_id = 46 and amount = 120000;
SELECT * from Income_Expense WHERE users_id = 47 and amount = 10000;