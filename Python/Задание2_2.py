#Задание 2:
print("Задание 2:")
class DataBuffer:
    def __init__(self):
        self.buffer = []

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            print("Буфер переполнен. Очищаем буфер.")
            self.buffer.clear()

    def get_data(self):
        if not self.buffer:
            print("Нет данных в буфере.")
            return None
        return self.buffer

# Пример:
buffer = DataBuffer()
buffer.add_data(1)
buffer.add_data(2)
buffer.add_data(3)
buffer.add_data(4)
buffer.add_data(5)
data = buffer.get_data()
print(data)
