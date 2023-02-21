from classes import Manager, Worker, Agent
import random

names_list = []
surnames_list = []


def text_finder(some_line):
    temp_word = ""
    for letter in some_line:
        if letter.isalpha():
            temp_word += letter
    return temp_word


with open('names.txt', 'r', encoding='utf-8') as names_file:
    for line in names_file:
        names_list.append(text_finder(line))

with open('sur_names.txt', 'r', encoding='utf-8') as surnames_file:
    for line in surnames_file:
        surnames_list.append(text_finder(line))

manager_list = [Manager(name=random.choice(names_list), sur_name=random.choice(surnames_list),
                        age=random.randint(19, 99)) for _ in range(3)]

worker_list = [Worker(name=random.choice(names_list), sur_name=random.choice(surnames_list),
                      age=random.randint(19, 99),
                      hours_worked=random.randint(1, 5000)) for _ in range(3)]

agent_list = [Agent(name=random.choice(names_list), sur_name=random.choice(surnames_list),
                    age=random.randint(19, 99),
                    salary=random.randint(1500, 50000)) for _ in range(3)]

workers_list = manager_list + worker_list + agent_list

for worker in workers_list:
    print(worker.info())
