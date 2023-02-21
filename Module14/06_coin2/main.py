def scaner(x, y):
    if x ** 2 + y ** 2 < r ** 2:
        return "Монетка где то рядом"
    return "Монетки в области нет"

print("Введите координаты монетки")
x = float(input("x: "))
y = float(input("y: "))
r = int(input("Введите радиус: "))
print(scaner(x, y))
