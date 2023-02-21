def text_check(some_text):
    """ Проверка Имени и Фамилии на длину"""
    for elem in some_text:
        if not elem.isalpha():
            raise NameError(elem, "не является буквой")
        if len(some_text) < 1:
            raise NameError("Имя или фамилия не должны быть такими короткими")
    return some_text


class Person:

    def __init__(self, name, sur_name, age):
        self.__name = name
        self.__sur_name = sur_name
        self.__age = age

    def set_name(self, name):
        return text_check(name)

    def set_sur_name(self, sur_name):
        return text_check(sur_name)

    def set_age(self, age):
        if not 18 < int(age) < 99:
            raise ValueError("Возраст должны быть в диапазоне от 18 до 99")
        else:
            return int(age)

    def get_name(self):
        return self.__name

    def get_sur_name(self):
        return self.__sur_name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, sur_name, age):
        super().__init__(name, sur_name, age)

    def earnings(self):
        return 0


class Manager(Employee):
    def __init__(self, name, sur_name, age):
        super().__init__(name, sur_name, age)

    def earnings(self):
        return 13000

    def info(self):
        return "Моё имя {name} фамилия {sur_name}. Я {work} моя зарплата {money}".format(
            name=self.get_name(),
            sur_name=self.get_sur_name(),
            work='Manager',
            money=self.earnings()
        )


class Agent(Employee):
    def __init__(self, name, sur_name, age, salary=5000):
        super().__init__(name, sur_name, age)
        self.__salary = self.set_salary(salary)

    def set_salary(self, salary):
        if salary > 0:
            return salary
        else:
            raise ValueError("Обьем продаж должен быть больше нуля")

    def get_salary(self):
        return self.__salary

    def earnings(self):
        return 5000 + self.__salary * 0.5

    def info(self):
        return "Моё имя {name} фамилия {sur_name}. Я {work} выполнил {sales} объем продаж, " \
               "моя зарплата {money}".format(
            name=self.get_name(),
            sur_name=self.get_sur_name(),
            work="Agent",
            sales=self.get_salary(),
            money=self.earnings()
        )


class Worker(Employee):
    def __init__(self, name, sur_name, age, hours_worked):
        super().__init__(name, sur_name, age)
        self.__hours_worked = self.set_hours_worked(hours_worked)

    def set_hours_worked(self, hours_worked):
        if hours_worked > 0:
            return hours_worked
        else:
            raise ValueError("Отработанные часы не могут быть отрицательным значением")

    def get_hours_worked(self):
        return self.__hours_worked

    def earnings(self):
        return 100 * self.__hours_worked

    def info(self):
        return "Моё имя {name} фамилия {sur_name}. Я {work} усердно работал в течении {hours} часов" \
               "моя зарплата {money}".format(
            name=self.get_name(),
            sur_name=self.get_sur_name(),
            work="Worker",
            hours=self.get_hours_worked(),
            money=self.earnings()
        )
