goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for title, code in goods.items():
    total_quantity = 0
    total_cost = 0
    for goods in store[code]:
        item_quantity = goods["quantity"]
        item_cost = goods["price"]
        total_cost += item_quantity * item_cost
        total_quantity += item_quantity
    print("{0} - {1} шт, общая стоимость {2} рублей.".format(title, total_quantity, total_cost))
