"""
def histogram(string):
    symbol_dict = dict()
    for sym in string:
        if sym in symbol_dict:
            symbol_dict[sym] += 1
        else:
            symbol_dict[sym] = 1
    return symbol_dict


text = input("Введите текст: ").lower()
hist = histogram(text)

for elem in sorted(hist.keys()):
    print(elem, ":", hist[elem])

print("Максимальная сумма: ", max(hist.values()))
"""

"""
small_storage = {
    "Гвозди": "5000",
    "Шурупы": "3040",
    "Саморезы": "2000",
}

big_storage = {
    "Доски": "1000",
    "Балки": "150",
    "Рейки": "600",
}

big_storage.update(small_storage)
search = input("Название интересующего Вас товара: ")

if search in big_storage:
    print(big_storage.get(search))
else:
    print("Ошибка: такого товара нет в наличии")

if big_storage.get(search):
    print(big_storage[search])
else:
    print("Ошибка: такого товара нет в наличии")
"""

"""
incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

result = sum(incomes.values())
min_keys = min(incomes, key=incomes.get)
min_values = min(incomes.values())
incomes.pop(min_keys)

print("Общий доход за год составил {} рублей".format(result))
print("Самый маленький доход у {}. Он составляет {} рублей".format(min_keys, min_values))
print("Итоговый словарь: {}".format(incomes))
"""

"""
new_phonebook = {
    "Александр": "+7 960 098 0909",
    "Евгений": "+7 927 098 0808",
    "Макар": "+7 918 098 0303",
}

old_phonebook = {
    "Григорий": "+7 918 098 1021",
    "Таврий": "+7 999 098 0404",
    "Ахмед": "+7 944 098 0101",
}

new_phonebook.update(old_phonebook)
new_phonebook["Лаврентий"] = new_phonebook.pop("Евгений")
print(new_phonebook)
print(new_phonebook.get("Альфред"))

print()
for i_elem in new_phonebook:
    print(i_elem, new_phonebook[i_elem])
"""
