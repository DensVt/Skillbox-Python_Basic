string = input("Введите строку: ").split()
max_len = 0
max_word = ''

for elem in string:
    if len(elem) > max_len:
        max_len = len(elem)
        max_word = elem

print("Самое длинное слово: ", max_word)
print("Длина этого слова: ", max_len)



"""
string = sorted(input("Введите строку: ").split(), key=len)[-1]
print(f"Самое длинное слово: {string}"
      f"\nДлина этого слова: {len(string)}")
"""

