import random


class House:
    food = 50
    money = 0


class Person:
    def __init__(self, name, satiety=50):
        self.name = name
        self.satiety = satiety

    def day(self, action):
        if self.satiety < 20 and House.food >= 10:
            self.satiety += 10
            House.food -= 10
            print(f"{self.name} поел, сытость + {self.satiety} еда в холодильнике - {House.food}")
        elif House.food < 10 and House.money > 10:
            House.food += 20
            House.money -= 10
            print(f"{self.name} сходил в магазин, деньги в доме - {House.money} еда в доме + {House.food}")
        elif action == 1:
            House.money += 50
            print(f"{self.name} Работает, деньги + {House.money} сытость - {self.satiety}")
        elif action == 2:
            self.satiety += 10
            House.food -= 10
            print(f'{self.name} Трапезничает, сытость + {self.satiety} показатель еды - {House.food}')
        else:
            self.satiety -= 10
            print(f"{self.name} Играет, сытость - {self.satiety}")


class Result:
    def __init__(self, man_1, man_2):
        self.man_1 = man_1
        self.man_2 = man_2

    def life_and_death(self):
        if self.man_1.satiety == 0 or self.man_2.satiety == 0:
            return True, print("Один из участников умер")

    # def res(self):
    #     hum_1 = Person("Степан")
    #     hum_2 = Person("Олег")
    #
    #     result = Result(hum_1, hum_2)
    #
    #     count_day = 0
    #     while True:
    #         count_day += 1
    #         if count_day == 365:
    #             print("\nЭксперимент удался, все живы!")
    #             break
    #         elif result.life_and_death():
    #             break
    #         else:
    #             rand = random.randint(1, 6)
    #             hum_1.day(rand)
    #             hum_2.day(rand)
    #
    #     print("Количество прошедших дней", count_day)