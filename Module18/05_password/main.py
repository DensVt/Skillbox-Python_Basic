while True:
    password = input("Придумайте пароль: ")
    cnt_up = 0
    cnt_num = 0

    for up in password:
        up.isupper()
        cnt_up += 1

    for num in password:
        num.isdigit()
        cnt_num += 1

    if (len(password) < 8) and (cnt_up < 1) and (cnt_num < 3):
        print("Пароль ненадёжный. Попробуйте ещё раз.")
    else:
        print("Это надёжный пароль!")
        break
