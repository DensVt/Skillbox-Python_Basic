# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)
print("Результат работы программы: ")

my_list = [1, 5, 3]
my_list.extend([1, 5, 1, 5])
first_count_nums = my_list.count(5)
print(f"Кол-во цифр 5 при первом объединении: {first_count_nums}")

for elem in my_list:
    if elem == 5:
        my_list.remove(5)

my_list.extend([1, 3, 1, 5, 3, 3])
second_count_nums = my_list.count(3)
print(f"Кол-во цифр 3 при втором объединении: {second_count_nums}")

print(f"Итоговый список: {my_list}")
