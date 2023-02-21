string = input("Введите строку: ").lower()
set_str = set()

for elem in string:
    if elem in set_str:
        set_str.remove(elem)
    else:
        set_str.add(elem)

print(("Можно", "Нельзя")[len(set_str) > 1], "сделать палиндромом")
