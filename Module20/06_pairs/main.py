import random

list_origin = [random.randint(0, 10) for _ in range(10)]
print("Оригинальный список: ", list_origin)

my_tuple = list(zip(list_origin[::2], list_origin[1::2]))
print("Новый список: ",my_tuple)



"""
import random

list_origin = [random.randint(0, 10) for _ in range(10)]
print("Оригинальный список: ", list_origin)

num_list = [(list_origin[num], list_origin[num + 1]) for num, elem in enumerate(list_origin) if num % 2 == 0]
print("Новый список: ", num_list)
"""
