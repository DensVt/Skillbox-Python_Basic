from random import random

with open("file_out.txt", "w") as file_out:
    cnt = 0
    while True:
        num = int(input("Введите число: "))

        if random() < 0.13:
            print("Вас постигла неудача!")
            break
        cnt += num
        file_out.write(str(num) + "\n")

        if cnt >= 777:
            print("Вы успешно выполнили условие для выхода из порочного цикла!")
            break
