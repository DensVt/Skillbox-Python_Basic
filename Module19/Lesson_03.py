"""
family_member = {
    "name": "jane",
    "surname": "doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "name": "alice",
            "age": 6
        },
        {
            "name": "bob",
            "age": 8
        }
    ]
}

children_dict = {}
for child in family_member["children"]:
    children_dict[child["name"]] = child["age"]

search_bob = children_dict.get("bob")
if search_bob:
    print("Найден bob")
else:
    print("bob-a no")

children_surname = family_member.get("surname")
if children_surname:
    print(children_surname)
else:
    print("no surname")
"""

"""
player_dict = {
    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
}

help_dict = {
    "rest": "отдыхают",
    "Training": "тренируются",
    "Travel": "путешествуют",
}

team_status = ["A", "B", "C"]

for index, state in enumerate(help_dict):
    print(f"Все члены команды {team_status[index]} которые {help_dict[state]}: ")
    for _, player in player_dict.items():
        if player["status"] == state and player["team"] == team_status[index]:
            print(player["name"])
"""
