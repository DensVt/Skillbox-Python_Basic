people_count = int(input("Введите количество человек: "))
database = dict()
lvl_dict = dict()

for num in range(1, people_count):
    couple = input(f"{num}-я пара: ").split()
    database[couple[0]] = couple[1]
    lvl_dict[couple[0]] = 0
    lvl_dict[couple[1]] = 0

for elem in database:
    people = elem
    while people in database:
        people = database[people]
        lvl_dict[elem] += 1

print("\n«Высота» каждого члена семьи: ")
for elem in sorted(lvl_dict):
    print(elem, lvl_dict[elem])
