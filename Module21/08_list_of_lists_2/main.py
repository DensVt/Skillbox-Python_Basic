def foo(lst):
    if not lst:
        return []
    if isinstance(lst[0], list):
        return foo(lst[0]) + foo(lst[1:])
    return lst[:1] + foo(lst[1:])


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(foo(nice_list))




"""
def foo(num):
    if not num:
        return []
    return foo(num[:-1]) + ([num[-1]] if not isinstance(num[-1], list) else foo(num[-1]))


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print("Ответ: ", foo(nice_list))
"""
