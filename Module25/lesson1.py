class Person:
    __count = 0   # __ - замок

    def __init__(self, name, age):
        self.__name = name
        # self.__age = age
        self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return "Имя: {}\tВозраст: {}".format(self.__name, self.__age)

    def get_count(self):            #Геттер - снять замок
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age): # метод изменения данных - сеттер
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст.")

alex = Person("Alex", 20)
Jain = Person("Jain", 18)
Rain = Person("Rain", 18)

# new_age = 10
# Jain.set_age(new_age)
print(Jain.get_count())
print(alex.get_age())
