sticks_cnt = int(input('Кол-во палок: '))
throws_cnt = int(input('Кол-во бросков: '))

line = ['I' for _ in range(sticks_cnt)]

for i_throw in range(1, throws_cnt + 1):
    print('Бросок', i_throw, end=' ')
    left = int(input('Сбиты палки с номера ')) - 1
    right = int(input('по номер '))

    if left > right:
        left, right = right, left

    line = ['.' if index in range(left, right) else line[index] for index in range(len(line))]

answer = ''
for i_elem in line:
    answer += i_elem
print(answer)


"""
sticks_of_count = int(input("Количество палок: "))
throws_of_count = int(input("Количество бросков: "))
row = [elem for lst in
       [list(range(int(input(f"Бросок {elem + 1}. Сбиты палки с номера, ")) - 1, int(input(f"По номер "))))
        for elem in range(throws_of_count)] for elem in lst]
res = ''.join(['I' if i not in row else '.' for i in range(sticks_of_count)])
print(f"Результат: {res}")
"""