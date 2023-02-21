class Potato:
    states = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"} # стадии, Статический атрибут

    def __init__(self, index):
        self.index = index
        self.state = 0      # динамический атр, отвечает за стадию зрелости

    def grow(self):    # метод для роста
        if self.state < 3:  # проверка, чтобы картошка не переросла
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):  # метод вывода зрелости на экран
        print("Картошка {} сейчас {}".format(
            self.index, Potato.states[self.state]
        ))



class PotatoGarden:

    def __init__(self, count):      # Инициализация грядки. Передаем сюда кол-во посаженой картошки
        self.potatoes = [Potato(index) for index in range(1, count + 1)]    # список в нем хранится вся картошка

    def grow_all(self):     # метод который взращивает всю картошку на грядке
        print("Картошка прорастает!\n")     # пройти по списку, для каждой картофелины вызвать метод grow
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):     # метод проверки, созрела ли наша поляна или нет
        # for i_potato in self.potatoes:    # стандартный вариант
        #     if not i_potato.is_ripe():
        #         print("Картошка еще не созрела!\n")
        #         break

        if not all([i_potato.is_ripe() for i_potato in self.potatoes]): # вариант с list comprehension
            print("Картошка еще не созрела!\n")
        else:
            print("\nВся картошка созрела! Можно собирать\n")

# my_garden = PotatoGarden(5)     # сажаем 5 клубней
# my_garden.are_all_ripe()
#
# for _ in range(3):
#     my_garden.grow_all()    # взращиваем 3 раза
#
# my_garden.are_all_ripe()