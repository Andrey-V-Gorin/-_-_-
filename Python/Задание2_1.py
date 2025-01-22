#Задание 1:
print("Задание 1:")
file_path = input("Укажите путь к файлу: ")
def read_numeric_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        number = float(line)
                        print(line)
                    except ValueError:
                        raise TypeError(f"Некорректное значение: '{line}' не является числом.")
    except FileNotFoundError:
        print(f"Ошибка: Файл с именем '{file_path}' не найден.")

# Пример:
read_numeric_lines(file_path)
