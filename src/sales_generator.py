"""
Project: Product Analyzer
Version: 1.0

Author: Mordvincev Gregory (Мордвинцев Григорий)

Description:
Generates a random product sales journal
for testing the Product Analyzer application.
"""

from random import choice
products = ["яблоко", "банан", "молоко", "сыр", "чай", "кофе", "масло"]

iteration = int(input("Введите количество продаж: "))
with open('product_list.txt', 'w') as f:
    for _ in range(iteration):
        f.write(f'{choice(products)}\n')

with open('product_list.txt', 'r') as f:
    text = f.read()

print(text)
print(f'''Журнал продаж успешно создан.
Количество записей: {len(text.split())}.
Файл: {"product_list.txt"}''')
