"""
Project: Sales Generator
Version: 1.1

Author: Mordvincev Gregory (Мордвинцев Григорий)

Description:
Generates a random product sales journal
for testing the Product Analyzer application.
"""

# Import 
from random import choice

# Product list
products = ["молоко", "сыр", "масло сливочное", "йогурт", "сметана",
    "чай чёрный", "чай зелёный", "каркадэ", "кофе", "какао", "яйца",
    "масло подсолнечное", "масло оливковое", "сахар", "соль",
    "виноград", "помело", "лимоны", "яблоки", "бананы", "персики",
    "нектарины", "груши", "мандарины", "апельсины", "манго", "личи",
    "чеснок", "лук", "томаты", "огурцы", "картофель", "морковь",
    "капуста", "свёкла", "салат листовой", "перец сладкий", "перец чили"]

# User input
while True:
    iteration = input("Введите количество продаж: ")
    try:
        iteration = int(iteration)
        break
    except ValueError:
        print('Неверный ввод, попробуйте снова')

# Sales generation
if iteration < 0:
    print('Количество продаж не может быть отрицательным')
elif iteration == 0:
    print('Продаж не зарегистрировано')
else:
    with open('data/product_list.txt', 'w', encoding='utf-8') as f:
        for _ in range(iteration):
            f.write(f'{choice(products)}\n')

# Reading a file
with open('data/product_list.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Output
print(f'''Журнал продаж успешно создан.
Количество записей: {len(text.split())}.
Файл: {"data/product_list.txt"}''')
