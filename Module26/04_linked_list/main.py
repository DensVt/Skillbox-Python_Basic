class Node:

    def __init__(self, name=None, next=None):
        self.name = name
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            next = self.head
            while next.next:
                next = next.next
            next.next = Node(value)

    def __str__(self):
        if self.head == None:
            return "Нет значений"
        else:
            next = self.head
            string = "[" + str(next.name)
            while next.next:
                next = next.next
                string += " " + str(next.name)
            return string + "]"

    def get(self, num):
        if self.head == None:
            return "Нет значений"
        else:
            cnt = 0
            next = self.head
            while next:
                if num == cnt:
                    return next.name
                next = next.next
                cnt += 1
            else:
                return "Индекс за пределами списка"

    def remove(self, num):
        if self.head != None:
            if num == 0:
                self.head = self.head.next
                return
            cnt = 1
            next = self.head
            while next:
                if num == cnt:
                    if next.next.next == None:
                        next.next = None
                    else:
                        next.next = next.next.next
                    return
                next = next.next
                cnt += 1
            else:
                return "Индекс за пределами списка"


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
