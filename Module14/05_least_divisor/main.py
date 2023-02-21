def nok(num):
    gcd = 1
    for i in range(1,num + 1):
        if num % i == 0:
            gcd = i
        if gcd > 1:
            break
    return gcd

number = int(input("Введите число: "))
print("Наименьший делитель, отличный от единицы: ",nok(number))
