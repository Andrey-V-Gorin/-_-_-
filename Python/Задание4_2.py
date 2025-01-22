#Задание 2:
print("Задание 2:")
import itertools
import time

# Создание бесконечного генератора чисел
def infinite_number_generator(start=0):
    while True:
        yield start
        start += 1

# Функция для применения к каждому элементу в итераторе
def apply_function(func, iterator):
    for item in iterator:
        yield func(item)

# Объединение нескольких итераторов в один
def combine_iterators(*iterators):
    for iterator in itertools.chain(*iterators):
        yield iterator

# Пример:
try:
    # Создаем бесконечный генератор
    number_gen = infinite_number_generator()

    # Применяем функцию "возвести в квадрат" к первыми 5 элементам
    squared_numbers = apply_function(lambda x: x**2, itertools.islice(number_gen, 5))

    print("Квадраты первых 5 чисел:")
    for num in squared_numbers:
        print(num)

    # Объединяем несколько итераторов
    iter1 = itertools.count(1, 2)
    iter2 = itertools.count(2, 3)
    combined_iter = combine_iterators(itertools.islice(iter1, 5), itertools.islice(iter2, 5))

    print("\\nОбъединенные значения из двух итераторов:")
    for value in combined_iter:
        print(value)

except StopIteration:
    print("Итератор закончился.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
