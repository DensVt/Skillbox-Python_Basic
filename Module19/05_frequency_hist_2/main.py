def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def reversed():
    text_dict = dict()
    for i_letter, i_num in hist.items():
        text_dict.setdefault(i_num, []).append(i_letter)
    return text_dict


text = input("Введите текст: ")
hist = histogram(text)
res = reversed()

print("Оригинальный словарь частот: ")
for elem in sorted(hist.keys()):
    print(elem, ":", hist[elem])

print("\nИнвертированный словарь частот: ")
for elem in res:
    print(elem, ':', res[elem])
