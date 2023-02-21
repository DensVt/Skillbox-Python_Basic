with open("calc.txt", "w", encoding="utf-8") as calc:
    for elem in ["100 + 34\n", "10 +* 3\n", "20 -* 2\n", "23 / 4"]:
        calc.write(elem)

result = []
with open("calc.txt", "r", encoding="utf-8") as calc_file:
    for elem in calc_file.readlines():
        try:
            result.append(eval(elem))
        except:
            if input("Обнаружена ошибка: " + elem + "Хотите исправить? ") == "да":
                elem = input('Введите исправленную строку: ')
                result.append(eval(elem))
print(sum(result))