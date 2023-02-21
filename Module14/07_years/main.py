
def three_digits(y1, y2):
    for i in range(y1, y2 + 1):
        a = i // 1000
        b = i // 100 % 10
        c = i // 10 % 10
        d = i % 10
        if (a == b == c) or (b == c == d) or (c == d == a) or (a == b == d):
            print(i)


first_year = int(input("Введите первый год: "))
second_year = int(input("Введите второй год: "))
print(f"Годы от {first_year} до {second_year} с тремя одинаковыми цифрами: ")
three_digits(first_year, second_year)