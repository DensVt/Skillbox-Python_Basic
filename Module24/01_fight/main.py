import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def fight(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError

warriors = [Warrior("Воин1"), Warrior("Воин2")]

while True:
    question = input("1 - атака 2 - выход из игры ")

    if question == "1":
        res = random.randint(0, 1)
        attacker, victim = warriors[res], warriors[res - 1]
        attacker.fight(victim)
        print(f"\n{attacker.name} атаковал {victim.name}")
        print(f"У {victim.name} осталось здоровья - {victim.health}\n")
        if victim.health <= 0:
            print(attacker.name, "победил")
            break

    elif question == "2":
        print("Вы вышли из игры")
        break

    else:
        print("Ошибка ввода\n")
