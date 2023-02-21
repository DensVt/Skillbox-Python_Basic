friends_of_count = int(input("Количество друзей: "))
receipt = int(input("Долговых расписок: "))
friends_list = []

for _ in range(friends_of_count):
    friends_list.append(0)

for number in range(receipt):
    print(f"\n{number + 1}-я расписка")
    to_who = int(input("Кому? "))
    from_who = int(input("От кого? "))
    how_many = int(input("Сколько? "))
    friends_list[to_who - 1] -= how_many
    friends_list[from_who - 1] += how_many
print("\nБаланс друзей: ")

for index in range(len(friends_list)):
    print(f"{index + 1} : {friends_list[index]}")