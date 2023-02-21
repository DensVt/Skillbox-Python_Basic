# Задача 1. Двойной вызов
# Реализуйте декоратор do_twice, который дважды вызывает декорируемую функцию. Не забывайте про документацию и аннотации типов.
# Пример декорируемой функции:
#
# def greeting(name):
#     print('Привет, {name}!'.format(name=name))
#
# Основной код:
#
# greeting('Tom')
#
# Результат:
# Привет, Tom!
# Привет, Tom!


import time
from typing import Callable, Any

def do_twice(func: Callable) -> Callable:
    """декоратор do_twice, который дважды вызывает декорируемую функцию"""
    def wrapped_func(*args, **kwargs) -> Any:
        func(*args, **kwargs)
        func(*args, **kwargs)
        return
    return wrapped_func

@do_twice
def greeting(name: str) -> None:
    print('Привет, {name}!'.format(name=name))

greeting("!")


# Задача 2. Таймер 2
#
# Для замера времени передачи различных данных на множество сайтов вы написали специальную функцию, которая сделала всю работу за вас,
# что позволило большую часть времени смотреть видео с котиками в интернете. Однако, увидев свой код, вы как программист с опытом поняли,
# что этот код можно написать намного красивее и удобнее.
#
# Реализуйте декоратор, который замеряет время работы задекорированной функции и выводит ответ на экран.
# Для проверки примените декоратор к какой-нибудь «тяжеловесной» функции и вызовите её в основной программе.


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунд(ы)')
        return result

    return surrogate


@time_track
def hard_func():
    return [x ** 2 ** x for x in range(22)]


hard_func()