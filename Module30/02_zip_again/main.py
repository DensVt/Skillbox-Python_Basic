from typing import List, Tuple

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]


def main():
    res: List[Tuple[str, int]] = list(
        map(lambda x, y: (x, y), letters, numbers))
    print(res)


if __name__ == '__main__':
    main()
else:
    print('Импортирован модуль', __name__)
