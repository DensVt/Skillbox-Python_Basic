import os


def save_files(string):
    way = input("Куда хотите сохранить документ? Введите последовательность папок (через пробел): ")
    file_name = input("Введите имя файла: ")
    r_path = way.replace(" ", "/")
    real_path = os.path.join(r_path, file_name)
    path = "C:/" + real_path
    check_file = os.path.exists(path)

    if check_file:
        ans_q = input("Вы действительно хотите перезаписать файл? ").lower()
        if ans_q == "да" or ans_q == "yes":
            with open(path, "w") as file:
                file.write(string)
                print("Файл успешно перезаписан!")
        else:
            print('Файл не перезаписан')
    else:
        with open(path, "w") as file:
            file.write(string)
            print('Файл успешно сохранён!')


save_files(input("Введите строку: "))
