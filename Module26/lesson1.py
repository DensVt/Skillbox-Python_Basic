# Дан любой итерируемый объект, например список из N чисел. Реализуйте функцию,
# которая эмулирует работу цикла for с помощью цикла while и проходит
# по всем элементам итерируемого объекта. Не забудьте про исключение «конца итерации».


import random
#
n = int(input("Введите кол-во чисел: "))
numbers = [random.randint(-100, 100) for _ in range(n)]

buffer_iter = iter(numbers)

while True:
    try:
        print(next(buffer_iter))
    except StopIteration:
        print("Конец!")
        break
