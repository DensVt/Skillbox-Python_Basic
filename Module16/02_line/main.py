first_class = list(range(160, 176, 2))
second_class = list(range(162, 180, 3))
my_list = first_class + second_class
my_list.sort()
print(f"Отсортированный список учеников: {my_list}")
