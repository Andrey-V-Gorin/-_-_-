#Задание 2:
print("Задание 2:")
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount):
        self.quantity += amount

    def decrease_quantity(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            raise ValueError("Недостаточно товара на складе")

    def total_value(self):
        return self.quantity * self.price


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def total_inventory_value(self):
        return sum(product.total_value() for product in self.products)


class Seller:
    def __init__(self, name):
        self.name = name
        self.sales_report = []

    def sell_product(self, product, amount):
        product.decrease_quantity(amount)
        sale_value = amount * product.price
        self.sales_report.append((self.name, product.name, amount, sale_value))

    def generate_sales_report(self):
        return self.sales_report


# Пример использования
warehouse = Warehouse()
Product1 = Product("iPhone", 10, 100000)
Product2 = Product("iPad", 3, 50000)
warehouse.add_product(Product1)
warehouse.add_product(Product2)

seller1 = Seller("Анастасия")
seller1.sell_product(Product1, 7)
seller2 = Seller("Андрей")
seller2.sell_product(Product2, 3)

print(f"Отчет о продажах за смену: {seller1.generate_sales_report()}")
print(f"Отчет о продажах за смену: {seller2.generate_sales_report()}")
