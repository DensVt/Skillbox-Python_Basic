import random
from test import Person, Result

hum_1 = Person("Степан")
hum_2 = Person("Олег")

result = Result(hum_1, hum_2)

count_day = 0
while True:
    count_day += 1
    if count_day == 365:
        print("\nЭксперимент удался, все живы!")
        break
    elif result.life_and_death():
        break
    else:
        rand = random.randint(1, 6)
        hum_1.day(rand)
        hum_2.day(rand)

print("Количество прошедших дней", count_day)