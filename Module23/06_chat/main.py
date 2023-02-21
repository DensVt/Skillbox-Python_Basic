user = input('Введите имя: ')
while True:
    print('\nЧтобы посмотреть текущий текст чата - введите <0>')
    print('Чтобы отправить сообщение - введите <1>')
    print('Чтобы изменить имя - введите <2>')
    action = input()


    if action == '0':

        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                for i_message in file:
                    print(i_message, end='')
        except FileNotFoundError:
            print('История сообщений пуста. \n')

    elif action == '1':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write(f'{user}: {message}\n')

    elif action == '2':
        user = input('Введите имя: ')

    else:
        print('Такой команды нет')