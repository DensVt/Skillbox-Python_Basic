def crypto(checking_list):
    return [value for index, value in enumerate(checking_list) if index >= 2 and is_prime(index)]


def is_prime(i_num):
    cnt = 0
    for elem in range(2, i_num // 2 + 1):
        if i_num % elem == 0:
            cnt += 1
    if cnt <= 0:
        return True
    return False


print(crypto('О Дивный Новый мир!'))
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))









