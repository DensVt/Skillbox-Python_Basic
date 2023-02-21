def Move(num, start, stop):
    if num == 1:
        print("Переложить диск", '1', "со стержня номер", start, "на стержень номер", stop)
    else:
        tmp = 6 - start - stop
        Move(num - 1, start, tmp)
        print("Переложить диск", num, "со стержня номер", start, "на стержень номер", stop)
        Move(num - 1, tmp, stop)


desk_count = int(input("Введите количество дисков: "))
Move(desk_count, 1, 3)




"""
def move(num, start, stop):
    def correction(x, y):
        return ({1, 2, 3} - {x} - {y}).pop()

    if num:
        check = correction(start, stop)
        move(num - 1, start, check)
        print("Переложить диск", num, "со стержня номер", start, "на стержень номер", stop)
        move(num - 1, check, stop)


desk_count = int(input("Введите количество дисков: "))
move(desk_count, 1, 3)
"""
