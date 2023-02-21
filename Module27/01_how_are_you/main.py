from typing import Callable, Any


def how_are_you(func: Callable) -> Any:
    def wrapped_func():
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        func()

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
