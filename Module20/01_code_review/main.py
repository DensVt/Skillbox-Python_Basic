students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)


def func(database):
    list_couple_id_students = ([(i, database.get(i).get("age")) for i in range(1, len(students) + 1)])
    full_list_interesting = set(sum([students.get(i).get('interests') for i in range(1, len(students) + 1)], []))
    full_len_surname = sum([len(database.get(i).get("surname")) for i in range(1, len(students) + 1)])

    print('Список пар "ID студента — возраст": ', list_couple_id_students)
    print('Полный список интересов всех студентов: ', full_list_interesting)
    print('Общая длина всех фамилий студентов: ', full_len_surname)


func(students)
