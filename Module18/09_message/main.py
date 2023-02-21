message = input("Сообщение: ")
str_new = ''
out = ''

for elem in message:
    if elem != '':
        if elem.isalpha():
            str_new += elem
        else:
            out += str_new[::-1] + elem
            str_new = ''
    else:
        out += str_new[::-1] + elem
        str_new = ''
print("Новое сообщение: ", out)




"""
from itertools import groupby

message = input("Сообщение: ")
res = ''
for elem, sub in groupby(message, str.isalnum):
    sub = list(sub)
    if elem:
        sub = sub[::-1]
    res += ''.join(sub)

print("Новое сообщение: ", res)
"""
