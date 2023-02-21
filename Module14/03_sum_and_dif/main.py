
def len_num(num):
    print("Количество цифр в числе: ",len(str(num)))
    print("Разность суммы и количества цифр: ",summ_of_numbers(number) - len(str(num)))
def summ_of_numbers(num):
    count = 0
    while num > 0:
        digit = num % 10
        num //= 10
        count += digit
    return count

number = int(input("Введите число: "))

print("Сумма чисел: ", summ_of_numbers(number))
len_num(number)