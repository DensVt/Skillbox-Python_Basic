def func(num):
    if num != 0:
        func(num - 1)
        print(num)

number = int(input("Введите число: "))
func(number)