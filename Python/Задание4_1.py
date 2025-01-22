#Задание 1:
print("Задание 1:")

from datetime import datetime, timedelta

# Отображение текущей даты и времени
def display_current_datetime():
    now = datetime.now()
    print("Текущая дата и время:", now)

def calculate_date_difference():
    # Преобразование строки в объект даты
    date_input_1 = input("Введите начальные дату и время в формате (yyyy-mm-dd hh:mm): ")
    date_input_2 = input("Введите конечные дату и время в формате (yyyy-mm-dd hh:m): ")
    date_format = "%Y-%m-%d %H:%M"
    date1 = datetime.strptime(date_input_1, date_format)
    date2 = datetime.strptime(date_input_2, date_format)

    # Вычисление разницы между двумя датами
    difference = abs(date2 - date1)
    print(f"Разница между {date1} и {date2} составляет {difference.days} дней и {difference.seconds // 3600} часов.")

# Пример:
display_current_datetime()
calculate_date_difference()
