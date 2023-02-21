# Методы класса, аргумент self


# class User:   # создание класса
#     user_name = "Admin"
#     password = "qwerty"   # статические атрибуты класса
#     is_banned = False
#     friends = []
#
#     def print_info(self):   # метод
#         print(
#             "Name: {}\nPassword: {}\nBan status: {}".format(
#                 self.user_name, self.password, self.is_banned)
#         )
#
#     def add_friend(self, friend):
#         if isinstance(friend, User):
#             self.friends.append(friend.user_name)
#         else:
#             self.friends.append(friend)
#
# user_1 = User() # экземпляр класса User
# user_1.print_info()
#
# user_2 = User()
# user_2.user_name = "Alina"
# user_1.add_friend("Bob")
# user_1.add_friend(user_2)
# print(user_1.friends)






# class Family:
#     surname = "Common family"
#     money = 100000
#     have_a_house = False
#
#     def info(self):      # метод инфо о себе
#         print(
#             "Family name: {}\nFamily funds: {}\nHaving a house: {}\n".format(
#                 self.surname,self.money, self.have_a_house
#             )
#         )
#
#     def earn_money(self, amount):    # метод заработок денег
#         self.money += amount
#         print("Earned {} money! Current value: {}".format(amount, self.money))
#
#     def bue_house(self, house_price, discount=0): # 2 - цена дома, скидка - дефолтная. Метод покупки дома.
#         house_price -= house_price * discount / 100 # пересчет цены дома
#         if self.money >= house_price:       # проверка, сможем ли купить дом
#             self.money -= house_price   # вычитаем деньги
#             self.have_a_house = True    # устанавливаем флаг
#             print("House purchased! Current money: {}\n".format(self.money))
#         else:
#             print("Not enough money!\n")
#
# my_family = Family()   # создать экземпляр класса
# my_family.info()    # вывод метода инфо о себе
# print("Try to bue a house")
# my_family.bue_house(10 ** 6)    # метод покупки, аргумента 1кк
# if not my_family.have_a_house:      # проверка если не получилось купить,
#     my_family.earn_money(800000)    # заработаем еше
#     print("Try to bue a house again")
#     my_family.bue_house(10 ** 6, 10)    # покупаем со скидкой в 10 процентов
#
# my_family.info()




# Практика
# Задача 1. Машина 2
#
# Модернизируйте класс Toyota из прошлого видео. Атрибуты остаются такими же:
#
# цвет машины (например, красный),
# цена (один миллион),
# максимальная скорость (200),
# текущая скорость (ноль).
#
#
# Добавьте два метода класса:
#
# Отображение информации об объекте класса.
# Метод, который позволяет устанавливать текущую скорость машины.
# Проверьте работу этих методов.

# class Toyota:
#     color_car = "red"
#     price = 1e6
#     speed_max = 200
#     current_speed = 0
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
# my_car = Toyota()
# my_car.check_info()
# my_car.change_speed(100)
# my_car.check_info()
# print(Toyota.current_speed) # обратите внимание, что скорость внутри Класса осталась той же, её изменения не коснулись



# Задача 2. Семья
#
# Реализуйте класс «Семья», который состоит из атрибутов «Имя»,
# Деньги» и «Наличие дома» и объекты которого могут выполнять следующие действия:
#
# Отобразить информацию о себе.
# Заработать денег (подаётся число, которое прибавляется к текущему значению денег).
# Купить дом (подаётся стоимость дома и необязательный аргумент «Скидка»).
# Вывести соответствующее сообщение об успешной/неуспешной покупке дома.
# Создайте как минимум один экземпляр класса и проверьте работу методов.

class Family:
    name = ""
    money = 0
    house = False

    def print_info(self):
        print("Family name: " + self.name, "Family funds: " + str(self.money),
              "Having a house: " + str(self.house), sep="\n")

    def get_money(self, count):
        self.money += count
        print(f"Earned {count} money! Current value: {self.money}")

    def bue_a_house(self, price, discount=0):
        house_price = (price - price * (discount / 100))
        if self.money >= house_price:
            self.money -= house_price
            self.house = True
            print(f"House purchased! Current money: {self.money}\n")
        else:
            print("\nNot enough money!\n")

human = Family()
human.name = "Common family"
human.money = 100000

human.print_info()
house_price = 900000
human.bue_a_house(house_price)
human.get_money(house_price - human.money)
human.bue_a_house(house_price)
human.print_info()

