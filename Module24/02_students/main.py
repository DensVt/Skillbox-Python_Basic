class Student:
    def __init__(self, full_name, num_group, grade):
        self.full_name = full_name
        self.num_group = num_group
        self.grade = grade

    def average(self):
        return sum(self.grade) / len(self.grade)

    def __str__(self):
        res = self.full_name, self.num_group, self.grade
        return res

students = []
for elem in range(2):
    print(f"Студент {elem + 1}")
    full_name = input("Имя: ")
    num_group = int(input("Номер группы: "))
    grade = list(map(int, input("Успеваемость: ").split()))
    students.append(Student(full_name, num_group, grade))

sort_stud = sorted(students, key=lambda stud: stud.average())
print(*sort_stud, sep="\n")