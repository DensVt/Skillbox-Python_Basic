import time
from typing import Callable, Any


def waiting(func: Callable) -> Any:
    """
    Декоратор, замедляющий работу функции на 5 сек.
    """
    def wrapped_func():
        time.sleep(4)
        # start_time = time.time()
        # while True:
        #     if time.time() - start_time >= 4:
        #         break
        func()
    return wrapped_func

@waiting
def test():
    print('<Тут что-то происходит...>')

test()