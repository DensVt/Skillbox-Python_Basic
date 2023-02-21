import os


def line_counter(dir: str):
    os.chdir(dir)
    total_cnt = 0
    for elem in os.listdir(dir):
        cnt = 0
        if os.path.basename(elem).endswith(".py"):
            with open(os.path.basename(elem), "r") as curr_python_file:
                for line in curr_python_file:
                    for symbols in line:
                        if symbols.isalpha() or symbols.isdigit() and not symbols == "#":
                            cnt += 1
                            break
            total_cnt += cnt
            yield f"В файле {os.path.basename(elem)} {cnt} строчек кода"
    yield f"Всего строчек кода в файлах этой директории: {total_cnt}"


path = input("Введите путь к директории, которая содержит файла '.py': ")
for result in line_counter(path):
    print(result)



