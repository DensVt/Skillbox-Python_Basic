my_contacts = dict()
while True:
    user_choice = int(input("1. Добавить контакт"
                            "\n2. Найти человека"
                            "\nВведите номер действия: "))

    if user_choice == 1:
        name = input("Введите имя и фамилию нового контакта (через пробел): ").split()
        if (name[0].capitalize(), name[1].capitalize()) in my_contacts:
            print("Такой человек уже есть в контактах.")
            print("Текущий словарь контактов: ", my_contacts)
        else:
            my_contacts[(name[0], name[1])] = int(input("Введите номер телефона: "))
            print("Текущий словарь контактов: ", my_contacts)

    if user_choice == 2:
        for key, value in my_contacts.items():
            search = input("Введите фамилию для поиска: ")
            if search in key[1][:len(search)]:
                print(key[0].capitalize(), key[1].capitalize(), value)