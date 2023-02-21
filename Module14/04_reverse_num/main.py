def revers(num):
    parts = str(num).split(".")
    reversed_parts = [''.join(reversed(part)) for part in parts]

    return float('.'.join(reversed_parts))


first_num = float(input("Введите первое число: "))
second_num = float(input("Введите второе число: "))

print(f"Первое число наоборот: {revers(first_num)}")
print(f"Второе число наоборот: {revers(second_num)}")
print(f"Сумма: {revers(first_num) + revers(second_num)}")