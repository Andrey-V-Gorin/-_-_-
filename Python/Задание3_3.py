#Задание 3:

#1: Создание виртуального окружения используя модуль venv на macOS и Linux:
    #python3 -m venv .myvenv

#2: Активация виртуального окружения на macOS и Linux:
    #source .myvenv/bin/activate

#3: Установка необходимых модулей requests и BeautifulSoup4:
    #pip3 install requests beautifulsoup4

#4: Написание скрипта для получения и парсинга данных:
import requests
from bs4 import BeautifulSoup

# Указание URL
url = input("Укажите URL: ")

try:
    # Получение данных с веб-сайта
    response = requests.get(url)

    # Проверка на успешное выполнение запроса
    response.raise_for_status()

    # Парсинг HTML-кода с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример: получение заголовка страницы
    title = soup.title.string
    print(f"Заголовок страницы: {title}")

except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

#5: Запуск скрипта:
    #python3 Задание3_3.py

#6: Деактивация виртуального окружения:
    #deactivate
