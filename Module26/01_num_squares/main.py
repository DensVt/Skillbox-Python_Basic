from collections.abc import Iterable


class Iterator:
    def __init__(self, num: int) -> None:
        self.current = 0
        self.count = num

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> int:
        if self.current < self.count:
            self.current += 1
            return self.current ** 2
        else:
            raise StopIteration


def square(num: int) -> Iterable:
    # for elem in range(1, num + 1):
    #     yield elem ** 2
    gen = [elem ** 2 for elem in range(1, num + 1)]
    return gen

N = int(input("Введите число: "))

print("через класс:")
for num in Iterator(N):
    print(num, end=' ')

print("\nчерез функцию:")
for num in square(N):
    print(num, end=" ")

print("\nчерез выражение:")
for num in (elem ** 2 for elem in range(1, N + 1)):
    print(num, end=" ")
