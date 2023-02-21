# Классы


# class User:   # создание класса
#     user_name = "Admin"
#     password = "qwerty"   # статические атрибуты класса
#     is_banned = False
#
# user_1 = User() # экземпляр класса User
# # user_1.user_name = "Том"
# # print(user_1.user_name) # имя меняем для user_1, сам класс остается не тронутым
# user_2 = User()
# user_2.user_name = "Том"
# print(user_1.user_name, user_2.user_name)
#
# User.user_name = "Noname"
# print(user_1.user_name, user_2.user_name)




#Практита

# Задача 1. Машина
#
# Напишите класс Toyota, состоящий из четырёх статических атрибутов:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Создайте три экземпляра класса и каждому из них поменяйте значение текущей скорости на случайное число от нуля до 200.

# import random
#
# class Toyota:
#     color_car = "red"
#     price = 1e6
#     speed_max = 200
#     current_speed = 0
#
# first_car = Toyota()
# first_car.current_speed = random.randint(0, 200)
#
# second_car = Toyota()
# second_car.current_speed = random.randint(0, 200)
#
# third_car = Toyota()
# third_car.current_speed = random.randint(0, 200)
#
# print(first_car.current_speed, second_car.current_speed, third_car.current_speed)



# Задача 2. Однотипные объекты
#
# В офис заказали небольшую партию из четырёх мониторов и трёх наушников. У монитора есть четыре характеристики:
# название производителя, матрица, разрешение и частота обновления экрана. Все четыре монитора отличаются только частотой.
#
# У наушников три характеристики: название производителя, чувствительность и наличие микрофона. Отличие только в наличии микрофона.


# class Monitor:
#     monitor_name = "Samsung"
#     monitor_matrix = 'VA'
#     monitor_res = 'WQHD'
#     monitor_freq = 0
#
# class Headphones:
#     headphones_name = 'Sony'
#     headphones_sensitivity = 108
#     headphones_micro = True
#
# monitors = [Monitor() for _ in range(4)]
# headphones = [Headphones() for _ in range(3)]
#
# for index, number in enumerate([60, 144, 70, 60]):
#     monitors[index].monitor_freq = number
#
# headphones[0].headphones_micro = False
# print(monitors)

