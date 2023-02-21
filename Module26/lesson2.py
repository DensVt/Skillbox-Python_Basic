import random
# Реализуйте итератор-счётчик, который не принимает никаких атрибутов
# и имеет только один статический атрибут — счётчик. Итератор увеличивает счётчик
#  и возвращает предыдущее значение. У вас должен получиться бесконечный итератор.
# То есть при вызове такого кода в основной программе



#  my_iter = СountIterator()
# for i_elem in my_iter:
#     print(i_elem)

# значения будут выдаваться бесконечно.


class CountIterator:
    count = 0

    def __iter__(self):
        return self

    def __next__(self):
        CountIterator.count += 1
        return CountIterator.count


my_count = CountIterator()

# for elem in my_count:
#     print(elem)




# Алексею по работе необходимо обрабатывать огромные массивы данных из миллионов элементов.
# Каждый новый элемент — это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента
# (первый элемент — просто случайное вещественное число от 0 до 1).
# Алексею нельзя хранить в памяти весь этот список, а со значениями работать как-то надо.
# Помогите Алексею, реализуйте такой класс-итератор и проверьте его работу.
# Также сделайте, чтобы при каждом новом вызове итератора в цикле значения считались заново.
#
# Пример работы программы:
# Кол-во элементов: 5
# Элементы итератора:
# 0.74
# 1.13
# 1.95
# 2.2
# 2.55
# Новое кол-во элементов: 6
# Элементы итератора:
# 0.79
# 1.58
# 2.55
# 2.81
# 3.06
# 3.34



class Sum_of_last_two:
    def __init__(self, count):
        self.last = 0
        self.end = count
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.end:
            raise StopIteration
        self.last += random.random()
        return self.last

counter = Sum_of_last_two(count=5)
# for elem in counter:
#     print(round(elem, 2))



# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
# Основной код:
#
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
#
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47


class Primes:
    def __init__(self, n):
        self.n, self.i, self.prime_numbers = n, 1, []

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        while self.i <= self.n:
            self.i += 1
            for prime in self.prime_numbers:
                if self.i % prime == 0:
                    break
            else:
                self.prime_numbers.append(self.i)
                return self.i
        raise StopIteration

prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
