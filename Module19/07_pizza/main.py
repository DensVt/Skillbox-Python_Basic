orders_count = int(input("Введите количество заказов: "))
database = dict()

for number in range(1, orders_count + 1):
    order = input(f"{number}-й заказ: ").split()
    if order[0] in database:
        if order[1] in database[order[0]]:
            database[order[0]][order[1]] += int(order[2])
        else:
            database[order[0]][order[1]] = order[2]
    else:
        database[order[0]] = dict({order[1]: int(order[2])})

for fst in sorted(database):
    print(f"\n{fst}:")
    for snd in sorted(database[fst]):
        print(f"\t{snd}: {database[fst][snd]}")