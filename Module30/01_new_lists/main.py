from typing import List
import functools


def main():
    floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
    names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
    numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

    cubed_and_rounded = list(map(lambda elem: round(elem ** 3, 3), floats))
    print(cubed_and_rounded)

    long_names = list(filter(lambda name: len(name) >= 5, names))
    print(long_names)

    composition = functools.reduce(lambda x, y: x * y, numbers)
    print(composition)


if __name__ == '__main__':
    main()
else:
    print('Импортирован модуль', __name__)
