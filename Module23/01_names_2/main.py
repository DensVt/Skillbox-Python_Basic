import datetime

with open("people.txt", "w", encoding="utf-8") as people_file:
    for name in ["Василий\n", "Николай\n", "Надежда\n", "Никита\n",
                 "Ян\n", "Ольга\n", "Евгения\n", "Кристина\n"]:
        people_file.write(name)

with open("people.txt", "r", encoding="utf-8") as people_file:
    line = people_file.read().split("\n")
    result = "".join(line)
    try:
        for num, name in enumerate(line):
            if len(name) < 3:
                raise ValueError(f"Ошибка: менее трёх символов в строке {num + 1}")
    except ValueError as exc:
        print(f"Ошибка: менее трёх символов в строке {num + 1}")
        with open("errors.txt", "a+", encoding="utf-8") as errors:
            print(f"{datetime.datetime.now()} {type(exc)} менее трёх символов в строке {num + 1}", file=errors)
    finally:
        print(f"Общее количество символов: {len(result)}")































#
#
#
#
#
#
#
#
# with open("people.txt", "r", encoding="utf-8") as people_file:
#     line = people_file.read().split("\n")
#     res = "".join(line)
#     try:
#         for number, name in enumerate(line):
#             if len(name) < 3:
#                 raise ValueError(f'менее трёх символов в строке {number}')
#     except ValueError:
#         print(f'менее трёх символов в строке {number}')
#         with open("errors.txt", "a+", encoding="utf-8") as errors:
#             print(f'{datetime.datetime.now()} менее трёх символов в строке {number}', file=errors)
#     finally:
#         print(f"Общее количество символов: {len(res)}")