#Задание 1:
SELECT product_name FROM products WHERE unit_price >= 3 and unit_price < 7


#Задание 2:
SELECT min(unit_price) min_price FROM products where category_id = 1

#Задание 3:
SELECT supplier_id, max(unit_price) max_price FROM products where supplier_id in (1, 3, 5) group by supplier_id order by supplier_id
