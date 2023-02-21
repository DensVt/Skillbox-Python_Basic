pos = []
numbers_of_count = int(input("Кол-во чисел: "))

for _ in range(numbers_of_count):
    pos.append(int(input("Число: ")))
print(f"\nПоследовательность: {pos}")

counter = 0
while pos != pos[::-1]:
    pos.insert(numbers_of_count, pos[counter])
    counter += 1

print(f"Нужно приписать чисел: {counter}")
print(f"Сами числа: {pos[:counter][::-1]}")
