max_num = int(input('Введите максимальное число: '))
all_nums = set(range(1, max_num + 1))

while True:
    guess = input('\nНужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    guess = {int(elem) for elem in guess.split()}
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_nums &= guess
    else:
        all_nums -= guess

print(*all_nums)
