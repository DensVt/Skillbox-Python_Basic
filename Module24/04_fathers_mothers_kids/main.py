class Parent:
    def __init__(self, name, age, childs):
        self.name, self.age, self.child_list = name, age, childs

    def __str__(self):
        return self.name + " " + str(self.age) + " года" + "\n" + "\n".join([str(elem) for elem in self.child_list])

    def calm(self, child):
        for elem in self.child_list:
            if elem is child:
                elem.calmness = True

    def hunger(self, child):
        for elem in self.child_list:
            if elem is child:
                elem.hunger = True

class Child:
    def __init__(self, name, age, calmness, hunger):
        self.name, self.age, self.calmness, self.hunger = name, age, calmness, hunger

    def __str__(self):
        return self.name + " " + str(self.age) + " лет " + \
               ("спокоен(а)" if self.calmness else " раздражен(а)") + \
               (" сыт(a)" if self.hunger else " голоден(а)")

petr = Child("Петр", 10, True, False)
anna = Child("Аня", 7, False, False)
john = Parent("Джон", 32, [petr, anna])

print(john)
john.calm(anna)
print(john)
john.hunger(anna)
print(john)
john.hunger(petr)
print(john)
