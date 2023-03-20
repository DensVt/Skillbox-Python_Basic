from collections import Counter


# def main():
#     def can_be_poly(s: str) -> bool:
#         freg = Counter(s)
#         odd_freg_count = sum(freg[elem] % 2 == 1 for elem in freg)
#         return odd_freg_count <= 1

def main():
    def can_be_poly(s): return sum(map(lambda elem: elem %
                                       2 == 1, Counter(s).values())) <= 1
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))


if __name__ == '__main__':
    main()
else:
    print('Импортирован модуль', __name__)
