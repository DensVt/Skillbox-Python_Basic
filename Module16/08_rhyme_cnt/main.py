number_of_people = int(input("Кол-во человек: "))
number_in_a_puzzle = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {number_in_a_puzzle}-й человек")

circle_of_people = list(range(1, number_of_people + 1))
out = 0

for _ in range(number_of_people - 1):
    print(f"\nТекущий круг людей: {circle_of_people}")
    start = out % len(circle_of_people)
    out = (start + number_in_a_puzzle - 1) % len(circle_of_people)
    print(f"Начало счёта с номера {circle_of_people[start]}")
    print(f"Выбывает человек под номером {circle_of_people[out]}")
    circle_of_people.remove(circle_of_people[out])
print("\nОстался человек под номером", *circle_of_people)