skates = []
peoples = []

number_of_skates = int(input("Количество коньков: "))
for elem in range(number_of_skates):
    the_size = int(input(f"Размер {elem + 1}-й пары: "))
    skates.append(the_size)

number_of_people = int(input("\nКоличество людей: "))
for num in range(number_of_people):
    foot_size = int(input(f"Размер ноги {num + 1}-го человека: "))
    peoples.append(foot_size)

res = list(set(skates) & set(peoples))

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {len(res)}")
