import math

degrees_list = [elem for elem in range(0, 360)]


class Vehicle:
    def __init__(self, x=0, y=0, a=90):
        self.__x = self.set_x(x)
        self.__y = self.set_y(y)
        self.__alpha = self.set_a(a)

    def set_x(self, x):
        if isinstance(x, int) or isinstance(x, float):
            return x
        else:
            return 0

    def set_y(self, y):
        if isinstance(y, int) or isinstance(y, float):
            return y
        else:
            return 0

    def set_a(self, a):
        if isinstance(a, int) or isinstance(a, float):
            return a
        else:
            return 0

    def set_direction(self, direction):
        if direction.lower() == "влево":
            return direction
        elif direction.lower() == "вправо":
            return direction
        else:
            raise NameError("direction принимает значение - строка (вправо/влево)")

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_a(self):
        return self.__alpha

    def process(self, distance):
        x = self.get_x() + distance * math.cos(math.radians(self.get_a()))
        y = self.get_y() + distance * math.sin(math.radians(self.get_a()))
        print(f"Автомобиль проехал расстояние: {distance} и теперь находится на координатах: ({x}:{y}")
        self.change_x(x)
        self.change_y(x)

    def change_x(self, new_x):
        self.__x = new_x

    def change_y(self, new_y):
        self.__y = new_y

    def change_a(self, new_a):
        self.__alpha = new_a

    def turn(self, direction, a):
        choice_direction = self.set_direction(direction)
        if choice_direction.lower() == "влево" or choice_direction.lower() == "вправо":
            if degrees_list.index(self.get_a()) + a > len(degrees_list):
                overflow = degrees_list.index(self.get_a()) + a
                while overflow > len(degrees_list):
                    overflow -= len(degrees_list)
                new_a = overflow
            else:
                new_a = degrees_list.index(self.get_a()) + a
        else:
            if degrees_list.index(self.get_a()) - a < 0:
                overflow = degrees_list.index(self.get_a()) - a
                while overflow < 0:
                    overflow + len(degrees_list)
                new_a = overflow
            else:
                new_a = degrees_list.index(self.get_a()) - a
        self.change_a(new_a)
        print(f"Вы повернули {choice_direction} текущее направление {new_a} градусов")


class Bus(Vehicle):
    def __init__(self, x, y, a, passengeres=0, money=0):
        super().__init__(x, y, a)
        self.__passengers = self.set_passengers_q(passengeres)
        self.__money = self.set_money(money)

    def take_passengers(self, quantity):
        self.__passengers = self.set_passengers_q(quantity)
        print(f"Вы взяли {quantity} пассажиров")

    def set_passengers_q(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            return quantity
        else:
            raise ValueError("Кол-во пассажиров - целое, положительное число")

    def set_money(self, money):
        if isinstance(money, (int, float)):
            return money
        else:
            raise ValueError("Тут должно быть число")

    def add_money(self, money):
        self.__money += money

    def let_passengers_go(self, quantity):
        self.__passengers -= self.set_passengers_to_go(quantity)
        print(f"Вышло {quantity} пассажиров")

    def set_passengers_to_go(self, quantity):
        if isinstance(quantity, int) and 0 < quantity < self.get_passengers_q():
            return quantity
        else:
            raise ValueError("Кол-во пассажиров - целое число, и меньше текущего")

    def get_passengers_q(self):
        return self.__passengers

    def get_money(self):
        return self.__money

    def process(self, distance):
        x = self.get_x() + distance * math.cos(math.radians(self.get_a()))
        y = self.get_y() + distance * math.cos(math.radians(self.get_a()))

        self.change_x(x)
        self.change_y(y)
        if distance > 0:
            earned_money = round(distance / 5 * self.get_passengers_q(), 2)
            self.add_money(earned_money)
            if earned_money == 0:
                end_off_phrase = "отсутствуют пассажиры, отсутствует оплата"
            else:
                end_off_phrase = f"Заработано за поездку {earned_money} рублей"

        if distance < 0:
            end_off_phrase = f"В обратном направлении оплата отсутствует"
        print(f"Автобус проехал: {distance} сейчас его координаты"
              f" ({round(x, 2)} : {round(y, 2)})" + str(end_off_phrase))
