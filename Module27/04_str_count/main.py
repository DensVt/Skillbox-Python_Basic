import functools
from typing import Callable, Any

def counter(func: Callable) -> Any:
    '''
    декоратор, считающий и выводящий количество вызовов декорируемой функции.
    :return:
    '''
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        wrapped_func.count += 1
        func(*args, **kwargs)
    wrapped_func.count = 0
    return wrapped_func

@counter
def simple_func(num):
    print(num)

for i in range(5):
    simple_func(i)
print("Функция {name}, была вызвана: {count} раз".format(
    name=simple_func.__name__, count=simple_func.count
))