"""
Project: Product Analyzer
Version: 1.0

Author: Mordvincev Gregory (Мордвинцев Григорий)

Description:
Generates a random product sales journal
for testing the Product Analyzer application.
"""

from random import choice
products = ["молоко", "сыр", "масло сливочное", "йогурт", "сметана",
    "чай чёрный", "чай зелёный", "каркадэ", "кофе", "какао", "яйца",
    "масло подсолнечное", "масло оливковое", "сахар", "соль",
    "виноград", "помело", "лимоны", "яблоки", "бананы", "персики",
    "нектарины", "груши", "мандарины", "апельсины", "манго", "личи",
    "чеснок", "лук", "томаты", "огурцы", "картофель", "морковь",
    "капуста", "свёкла", "салат листовой", "перец сладкий", "перец чили"]

iteration = int(input("Введите количество продаж: "))
with open('data/product_list.txt', 'w') as f:
    for _ in range(iteration):
        f.write(f'{choice(products)}\n')

with open('product_list.txt', 'r') as f:
    text = f.read()

print(text)
print(f'''Журнал продаж успешно создан.
Количество записей: {len(text.split())}.
Файл: {"product_list.txt"}''')
