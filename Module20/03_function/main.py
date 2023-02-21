def slicer(tuple, number):
    if number not in tuple:
        return ()
    if tuple.count(number) == 1:
        return tuple[tuple.index(number):]
    return tuple[tuple.index(number): tuple.index(number, tuple.index(number) + 1) + 1]


print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
