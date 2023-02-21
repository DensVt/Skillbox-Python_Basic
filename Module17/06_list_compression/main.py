import random

count_numbers = int(input("Количество чисел в списке: "))
count_numbers = [random.randint(0, 2) for _ in range(count_numbers)]
my_zip = [elem for elem in count_numbers if elem]

print(f"Список до сжатия: {count_numbers}"
      f"\nСписок после сжатия: {my_zip}")
