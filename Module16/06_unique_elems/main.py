first_list = []
second_list = []

for elem in range(3):
    first_list_number = int(input(f"Введите {elem + 1}-е число для первого списка: "))
    first_list.append(first_list_number)

for elem in range(7):
    second_list_number = int(input(f"Введите {elem + 1}-е число для второго списка: "))
    second_list.append(second_list_number)

print(f"Первый список: {first_list}")
print(f"Второй список: {second_list}")

first_list.extend(second_list)
for _ in range(len(first_list)):
    for num in first_list:
        if first_list.count(num) > 1:
            first_list.remove(num)
print(f"\nНовый первый список с уникальными элементами: {first_list}")
