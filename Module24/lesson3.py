# Конструктор __init__ и работа с несколькими классами


# class Employee: # Класс работника
#
#     def __init__(self, name, salary):       # - это конструктор класса, метод отвечающий за инициализацию
#         self.name = name        # это Динамические атрибуты
#         self.salary = salary        # это Динамические атрибуты
#
#
#     def info(self):
#         print(
#             "Name: {} \nSalary: {}".format(self.name, self.salary)
#             # "Name: " + self.name, "Salary: " + str(self.salary), sep='\n'   # 2 вариант
#         )
#
# emp_1 = Employee("Tom", 10000)
# emp_2 = Employee("Elsa", 20000)
#
# emp_1.info()
# emp_2.info()



# Есть картошка со следующими характеристиками:
# 1. Номер картошки в грядке(индекс)
# 2. Стадия зрелости(стадии: Отсутствует, Росток, Зеленая, Зрелая)
#
# Картошка может:
# 1. Расти(переходить на следующую стадию созревания)
# 2. Предоставлять инфу о своей зрелости
#
# Есть грядка с картошкой, которая:
# 1. Содержит список картошки, которая на ней растет
#
# И может:
# 1. Взращивать картошку
# 2. Предоставлять инфу о зрелости всей картошки.

# class Potato:
#     states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"} # стадии, Статический атрибут
#
#     def __init__(self, index):
#         self.index = index
#         self.state = 0      # динамический атр, отвечает за стадию зрелости
#
#     def grow(self):    # метод для роста
#         if self.state < 3:  # проверка, чтобы картошка не переросла
#             self.state += 1
#         self.print_state()
#
#     def is_ripe(self):
#         if self.state == 3:
#             return True
#         return False
#
#     def print_state(self):  # метод вывода зрелости на экран
#         print("Картошка {} сейчас {}".format(
#             self.index, Potato.states[self.state]
#         ))
#
#
#
# class PotatoGarden:
#
#     def __init__(self, count):      # Инициализация грядки. Передаем сюда кол-во посаженой картошки
#         self.potatoes = [Potato(index) for index in range(1, count + 1)]    # список в нем хранится вся картошка
#
#     def grow_all(self):     # метод который взращивает всю картошку на грядке
#         print("Картошка прорастает!")     # пройти по списку, для каждой картофелины вызвать метод grow
#         for i_potato in self.potatoes:
#             i_potato.grow()
#
#     def are_all_ripe(self):     # метод проверки, созрела ли наша поляна или нет
#         # for i_potato in self.potatoes:    # стандартный вариант
#         #     if not i_potato.is_ripe():
#         #         print("Картошка еще не созрела!\n")
#         #         break
#
#         if not all([i_potato.is_ripe() for i_potato in self.potatoes]): # вариант с list comprehension
#             print("Картошка еще не созрела!\n")
#         else:
#             print("Вся картошка созрела! Можно собирать\n")
#
# my_garden = PotatoGarden(5)     # сажаем 5 клубней
# my_garden.are_all_ripe()
#
# for _ in range(3):
#     my_garden.grow_all()    # взращиваем 3 раза
#
# my_garden.are_all_ripe()





# Практика


# Задача 1. Машина 3
# Вам предстоит снова немного видоизменить класс Toyota из прошлого урока. На всякий случай вот описание класса.
#
# Четыре атрибута:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
# Два метода:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Теперь все четыре атрибута должны инициализироваться при создании экземпляра класса (то есть передаваться в init).
# Реализуйте такое изменение класса.


# class Toyota:
#
#     def __init__(self, color_car, price, speed_max, current_speed):
#         self.color_car = color_car
#         self.price = price
#         self.speed_max = speed_max
#         self.current_speed = current_speed
#
#     def check_info(self):
#         print(
#             "color_car: {}\nprice: {}\nspeed_max: {}\ncurrent_speed: {}\n".format(
#                 self.color_car, self.price, self.speed_max, self.current_speed
#             )
#         )
#
#     def change_speed(self, new_speed):
#         self.current_speed = new_speed
#
#
# car_1 = Toyota("red", 1e6, 200, 0)
# car_2 = Toyota("green", 2e6, 400, 0)
#
# car_1.check_info()
# car_2.check_info()





# Объект «Точка» на плоскости имеет координаты X и Y. При создании новой точки могут передаваться
# пользовательские значения координат, по умолчанию x = 0, y = 0.
#
# Реализуйте класс, который будет представлять эту точку, и напишите метод, который предоставляет
# информацию о ней. Также внутри класса пропишите счётчик, который будет отвечать за количество созданных точек.
#
# Подсказка: счётчик можно объявить внутри самого класса и увеличивать его в методе __init__.

# class Point:
#     count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def print_info(self):
#         print("x: {} \ny: {}".format(self.x, self.y))
#
#
# my_point = Point()
# p1 = Point(10, 10)
# p2 = Point(20, 15)
#
# my_point.print_info()
# p1.print_info()
# p2.print_info()




