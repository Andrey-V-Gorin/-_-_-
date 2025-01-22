#Задание 1:
print("Задание 1:")

#1. Создаем пакет: my_package, содержащий файлы sum_module.py и __init__.py

#2. Код для sum_module.py:
#class SumCalculator:
    #def calculate_sum(self, number_list):
        #return sum(number_list)

#3. Пример использования пакета:
from my_package.sum_module import SumCalculator
calculator = SumCalculator()
numbers = [1, 2, 3, 4, 5]
print(f"Сумма чисел: {calculator.calculate_sum(numbers)}")
