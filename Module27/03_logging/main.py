import datetime
import os
from typing import Callable, Any


def logging(func: Callable) -> Any:
    '''
    Декоратор логирования ошибок при выполнении функции.
    Ошибки записываются в файл function_errors.log
    '''

    def wrapped_func(*args, **kwargs):
        with open("function_errors.log", "a") as log_file:
            try:
                print("Название функции: {name}\n"
                      "Описание функции:"
                      "{description}".format(name=func.__name__, description=func.__doc__))
                return func(*args, **kwargs)
            except Exception as exc:
                string = datetime.datetime.now().strftime("%d.%m.%y %H:%M") \
                         + " " + func.__name__ + " " + type(exc).__name__ + "\n"
                log_file.write(string)

    return wrapped_func


@logging
def first_func(lst: list) -> None:
    """
    Функция печати списка
    :param lst: Список
    :return: None
    """
    for i in range(5):
        print(lst[i])


@logging
def second_func(first_num: int, second_num: int) -> float:
    '''
    Функция деления, одного числа на другое
    :param first_num:
    :param second_num:
    :return:
    '''
    return first_num / second_num


@logging
def third_func(value: Any) -> None:
    '''
    Функция преобразования значения в Integer
    и вывод на экран
    :param value:
    :return:
    '''
    print(int(value))


def delete_file():
    if "function_errors.log" in os.listdir(os.getcwd()):
        os.remove(os.path.abspath(os.path.join("function_errors.log")))


delete_file()
first_func([i for i in range(4)])
print(second_func(1, 0))
third_func("Не число")
