"""
num = int(input("Введите целое число: "))
num_dict = {num: num ** 2 for num in range(1, num + 1)}
print("Результат: ", num_dict)
"""

"""
student_info = input(
    "Введите информацию о студенте через пробел "
    "(имя, фамилия, город, место учёбы, оценки): "
    ).split()

student_dict = {
    "Имя": student_info[0],
    "фамилия": student_info[1],
    "город": student_info[2],
    "место учёбы": student_info[3],
    "Оценки": [int(grade) for grade in list(student_info[4:])]
}

for key in student_dict:
    print(key, student_dict[key])
"""

"""
phonebook = {}
while True:
    print("Текущие контакты на телефоне: ")
    if phonebook:
        for i_name in phonebook:
            print(i_name, phonebook[i_name])
    else:
        print("<Пусто>")

    new_contact = input("Введите имя: ")
    new_number = input("Введите номер телефона: ")
    if new_contact in phonebook:
        print("Человек с именем {} уже существует".format(new_contact))
    else:
        phonebook[new_contact] = new_number
"""