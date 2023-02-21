string = input("Введите строку: ")
curr_char = string[:1]
curr_cnt = 1
res = ''

for elem in string[1:]:
    if elem != curr_char:
        res += (curr_char + str(curr_cnt))
        curr_char = elem
        curr_cnt = 1
    else:
        curr_cnt += 1
res += (curr_char + str(curr_cnt))

print("Закодированная строка: ", res)




"""
Возвращает повторяющиеся элементы и их количество.


from itertools import groupby

string = input("Введите строку: ")
group_str = groupby(string)
res = ''.join(''.join((elem, str(len(list(grouper))))) for elem, grouper in group_str)

print("Закодированная строка: ", res)
"""
