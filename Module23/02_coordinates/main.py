import random
# def f(x, y):
#     x += random.randint(0, 10)
#     y += random.randint(0, 5)
#     return x / y
#
#
# def f2(x, y):
#     x -= random.randint(0, 10)
#     y -= random.randint(0, 5)
#     return y / x
#
#
# try:
#     file = open('coordinates.txt', 'r')
#     for line in file:
#         nums_list = line.split()
#         res1 = f(int(nums_list[0]), int(nums_list[1]))
#         try:
#             res2 = f2(int(nums_list[0]), int(nums_list[1]))
#             try:
#                 number = random.randint(0, 100)
#                 file_2 = open('result.txt', 'w')
#                 my_list = sorted([res1, res2, number])
#                 file_2.write(' '.join(my_list))
#             except Exception:
#                 print("Что-то пошло не так")
#         except Exception:
#             print("Что-то пошло не так со второй функцией")
#         finally:
#             file.close()
#             file_2.close()
# except Exception:
#     print("Что-то пошло не так с первой функцией")


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'w') as create_file:
    create_file.write('2 2')

with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
        except Exception:
            print("Что-то пошло не так с первой функцией")
        try:
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except Exception:
            print("Что-то пошло не так со второй функцией")

number = random.randint(0, 100)
try:
    with open('result.txt', 'w') as file_2:
        my_list = sorted([res1, res2, number])
        file_2.write(' '.join(map(str, my_list)))
except Exception:
    print("Что-то пошло не так")
