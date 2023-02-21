my_list = int(input("Введите длину списка: "))
my_list = [1 if elem % 2 == 0 else elem % 5 for elem in range(my_list)]

print(f"Результат: {my_list}")
