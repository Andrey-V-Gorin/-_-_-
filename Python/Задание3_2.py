#Задание 2:
print("Задание 2:")
import collections
import string

def count_unique_words(text):
    # Удаляем знаки препинания и приводим к нижнему регистру
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Разбиваем текст на слова
    words = text.split()

    # Используем collections.Counter для подсчета уникальных слов
    unique_words_count = collections.Counter(words)

    # Возвращаем количество уникальных слов
    return len(unique_words_count)

# Пример:
input_text = "Напишите функцию, которая принимает на вход строку и выводит количество уникальных слов в ней, игнорируя знаки препинания и пробелы. Используйте модуль collections для этой задачи."
print(count_unique_words(input_text))
