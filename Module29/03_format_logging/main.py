import time
import functools
from typing import Callable, Any


def logged(time_format: str, name_prefix: str = ""):
    """
    Функция для обёртки декоратора log_methods

    :param time_format: формат даты и времени (str)
    :param name_prefix: префикс перед именем функции, для вывода; по умолчанию - '' (str)
    """
    def decorator(func: Callable) -> Callable:
        if hasattr(func, '_logged_decorator') and func._logged_decorator:
            return func

        @functools.wraps(func)
        def decorated_func(*args, **kwargs) -> Any:
            start_time = time.time()
            print("- Запускается '{}'. Дата и время запуска: {} ".format(
                name_prefix + func.__name__,
                time.strftime(time_format)
            ))
            result = func(*args, **kwargs)
            end_time = time.time()
            print("- Завершение '{}', время работы = {:0.3f}s ".format(
                name_prefix + func.__name__,
                end_time - start_time
            ))
            return result
        decorated_func._logged_decorator = True
        return decorated_func
    return decorator


def log_methods(time_format: str) -> Callable:
    """
    Декоратор. Логгирует все методы класса, используя функцию logged.

    :param time_format: формат даты и времени (str)
    """
    def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__'):
                continue
            a = getattr(cls, i_method)
            if hasattr(a, '__call__'):
                decorated_a = logged(time_format, cls.__name__ + ".")(a)
                setattr(cls, i_method, decorated_a)
        return cls
    return decorator


# from datetime import datetime

# def log_methods(date_format):
#     def decorator(cls):
#         class DecoratedClass(cls):
#             def __getattribute__(self, name):
#                 attribute = super().__getattribute__(name)
#                 if callable(attribute) and not name.startswith("__"):
#                     def wrapper(*args, **kwargs):
#                         now = datetime.now().strftime(date_format)
#                         print(f"Запускается '{cls.__name__}.{name}'. Дата и время запуска: {now}")
#                         start_time = datetime.now()
#                         res = attribute(*args, **kwargs)
#                         end_time = datetime.now()
#                         elaplsed_time = (end_time - start_time).total_seconds()
#                         print(f"Завершение '{cls.__name__}.{name}', время работы = {elaplsed_time:.3f}s")
#                         return res
#                     return wrapper
#                 else:
#                     return attribute
#         return DecoratedClass
#     return decorator


@log_methods("%b %d %Y - %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("%b %d %Y - %H:%M:%S")
class B(A):
    """Тестовый класс 2"""

    def test_sum_1(self) -> None:
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника ")

    def test_sum_2(self) -> int:
        print("Тут метод test sum 2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
