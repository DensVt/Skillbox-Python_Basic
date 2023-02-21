guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")

    question_to_the_user = input("Гость пришёл или ушёл? ")

    if question_to_the_user == "пришел":
        guest_name = input("Имя гостя: ")

        if len(guests) >= 6:
            print(f"Прости, {guest_name}, но мест нет.\n")
        else:
            guests.append(guest_name)
            print(f"Привет, {guest_name}!\n")

    elif question_to_the_user == "ушел":
        guest_name = input("Имя гостя: ")
        guests.remove(guest_name)
        print(f"Пока {guest_name}!\n")

    else:
        print("\nВечеринка закончилась, все легли спать.")
        break
