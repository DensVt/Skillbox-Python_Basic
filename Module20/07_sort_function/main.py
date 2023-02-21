def tpl_sort(num):
    for elem in num:
        if not isinstance(elem, int):
            return num
    return tuple(sorted(num))


in_number = 6, 3, -1, 8, 4, 10, -5
print(tpl_sort(in_number))