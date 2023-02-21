# # class Pet:
# #     legs = 4
# #     has_tail = True
# #
# #     def __str__(self):
# #         tail = 'да' if self.has_tail else 'нет'
# #         return 'всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
# #             legs=self.legs,
# #             has_tail=tail
# #         )
# #
# #     def walk(self):
# #         print("Гуляет")
# #
# #
# # class Dog(Pet):
# #
# #     def sound(self):
# #         return "Гав!"
# #
# #
# # class Cat(Pet):
# #
# #
# #     def sound(self):
# #         return "Мяу!"
# #
# #
# # class Frog(Pet):
# #     has_tail = False
# #
# #     def sound(self):
# #         return "Ква!"
# #
# #     def walk(self):
# #         print("Плавает")
# #
# #
# # cat = Cat()
# # dog = Dog()
# # frog = Frog()
# #
# # cat.walk()
# # frog.walk()
#
#
# class Person:
#     __count = 0
#
#     def __init__(self, name, age):
#         self.__name = name
#         # self.__age = age
#         self.set_age(age)
#         Person.__count += 1
#
#     def __str__(self):
#         return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)
#
#     def get_count(self):  # Геттер
#         return self.__count
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def set_age(self, age):  # метод изменения данных - сеттер
#         if age in range(1, 90):
#             self.__age = age
#         else:
#             raise Exception("Недопустимый возраст.")
#
#
# class Student(Person):
#     def __init__(self, name, age, university):
#         super().__init__(name, age)
#         self.university = university
#
#     def __str__(self):
#         # info = super().__str__()                                                       # 1 вариант
#         # info = '\n'.join(
#         #     (
#         #         info,
#         #         "Студент учится в универе {}".format( self.university)
#         #     )
#         # )
#         # return info
#         return "Студент {} учится в универе {}".format(self.get_name(), self.university)  # 2 вариант
#
#
# class Employee(Person):
#     def __init__(self, name, age, company, salary):
#         super().__init__(name, age)
#         self.company = company
#         self.salary = salary
#
#     def __str__(self):
#         info = super().__str__()  # 1 вариант
#         info = '\n'.join(
#             (
#                 info,
#                 "компания {} получает {}".format(self.company, self.salary)
#             )
#         )
#         return info
#         # return ("Работник {} компания {} получает {}".format(self.get_name(), self.company, self.salary)) # 2 вариант
#
#
# my_student = Student(name="Tom", age=24, university="MGU")
# print(my_student)
#
# my_employee = Employee(name="Carl", age=32, company="GeneralMotors", salary=320000)
# print(my_employee)





# class Unit:
#     def __init__(self, health):
#         self.__health = health
#
#     def set_health(self, amount):
#         self.__health = amount
#
#     def get_health(self):
#         return self.__health
#
#     def get_damage(self, amount):
#         self.set_health(self.get_health() - 0)
#
# class Soldier(Unit):
#     def get_damage(self, amount):
#         self.set_health(self.get_health() - amount)
#
# class Citizen(Unit):
#     def get_damage(self, amount):
#         self.set_health(self.get_health() - amount * 2)



# class CanFly:
#
#     def __init__(self):
#         self.altitude = 0  # метров
#         self.velocity = 0  # км/ч
#
#     def take_off(self):
#         pass
#
#     def fly(self):
#         pass
#
#     def land_on(self):
#         self.altitude = 0
#         self.velocity = 0
#
#     def __str__(self):
#         return '{} высота {} скорость {}'.format(
#             self.__class__.__name__, self.altitude, self.velocity,
#         )




class Butterfly(CanFly):

    def take_off(self):
        self.altitude = 1

    def fly(self):
        self.velocity = 0.1


class Aircraft(CanFly):

    def take_off(self):
        self.velocity = 300
        self.altitude = 1000

    def fly(self):
        self.velocity = 800


class Missile(CanFly):

    def take_off(self):
        self.velocity = 1000
        self.altitude = 10000

    def land_on(self):
        self.altitude = 0
        self.destroy_enemy_base()

    def destroy_enemy_base(self):
        print('Ракета показала себя великолепно. Только упала не на ту планету (C) Вернер фон Браун')

