# class Pet:
#     legs = 4
#     has_tail = True
#
#     def __str__(self):
#         tail = 'да' if self.has_tail else 'нет'
#         return 'всего ног: {legs}\nХвост присутствует - {has_tail}'.format(
#             legs=self.legs,
#             has_tail = tail
#         )
#
# class Dog(Pet):
#
#     def sound(self):
#         return "Гав!"
#
#
# class Cat(Pet):
#
#     def sound(self):
#         return "Мяу!"
#
# class Frog(Pet):
#     has_tail = False
#
#     def sound(self):
#         return "Ква!"
#
#
# cat = Cat()
# dog = Dog()
# frog = Frog()
# print(cat)
# print(dog)
# print(frog)
#
# print(cat.sound())
# print(dog.sound())
# print(frog.sound())

#
class Ship:

    def __init__(self, model="Корабль"):
        self.model = model

    def __str__(self):
        return self.model

    def swim(self):
        print(f'{self.model} идет по воде!')


# class CargoShip(Ship):
#
#
#     def __init__(self, model='Грузовой корабль'):
#         super().__init__(model)
#         self.tonnage_load = 0
#
#     def load(self):
#         print("Загружаем корабль")
#         self.tonnage_load += 1
#         print("Текущая загруженность", self.tonnage_load)
#
#     def unload(self):
#         print("Разгружаем корабль")
#         if self.tonnage_load > 0:
#             self.tonnage_load -= 1
#         else:
#             print("Корабль разгружен")
#         print("Текущая загруженность", self.tonnage_load)
#
#
# class WarShip(Ship):
#     def __init__(self, gun, model="Военный корабль"):
#         super().__init__(model)
#         self.gun = gun
#
#     def attack(self):
#         print("атакует с помощью", self.gun)
#
#
# cargoship = CargoShip('Баржа')
# cargoship.swim()
# cargoship.load()
#
#
# warship = WarShip("Зенитное орудие","Крейсер")
# warship.swim()
# warship.attack()




# class Robot:
#     def __init__(self, model):
#         self.model = model
#
#     def __str__(self):
#         return "Робот марки - {}".format(
#             self.model
#         )
#
#     def operate(self):
#         print("Ротот ездит по кругу")
#
# class WarRobot(Robot):
#     def __init__(self, model, gun):
#         super().__init__(model)
#         self.gun = gun
#
#     def operate(self):
#         print("Робот охраняет обьект с помощью вооружения -", self.gun)
#
#
# class VacuumCleanerRobot(Robot):
#     bag_is_full = 0
#
#     def __init__(self, model):
#         super().__init__(model)
#
#     def operate(self):
#         print("Робот пылесосит пол")
#         self.bag_is_full += 1
#         print("Текущая заполненость мешка", self.bag_is_full)
#
#
# class SubmarineWarRobot(Robot):
#     def __init__(self, model):
#         super().__init__(model)
#
#     def operate(self):
#         print("Охрана ведется под водой")
#
#
# warrobot = WarRobot("Судья", "Система Залп")
# print(warrobot)
# warrobot.operate()
#
# vaccumcleanerrobot = VacuumCleanerRobot("Сосун")
# print(vaccumcleanerrobot)
# vaccumcleanerrobot.operate()
#
# submarinewarrobot = SubmarineWarRobot("Охотник")
# print(submarinewarrobot)
# submarinewarrobot.operate()



class DivisionError(Exception):
    pass


with open("numbers.txt", "r", encoding="utf8") as file:
    for line in file:
        try:
            clear_line = line.rstrip()
            first, second = clear_line.split()
            if int(first) < int(second):
                raise DivisionError("нельзя делить большее на меньшее")
        except (ValueError, DivisionError) as exc:
            print(exc, type(exc), first, second)

