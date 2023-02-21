# По аналогии с бесконечным итератором из практики предыдущего урока,
# реализуйте свой счётчик-генератор, который также в цикле будет бесконечно выдавать значения.
# Дополнительно: преобразуйте (или напишите с нуля) итератор простых чисел в функцию-генератор.

def counter():
    n = 0
    while True:
        n += 1
        yield n

def get_prime_nums(n):
    prime_nums = []
    for nums in range(2, n + 1):
        for prime in prime_nums:
            if nums % prime == 0:
                break
        else:
            prime_nums.append(nums)
            yield nums

for i in get_prime_nums(50):
    print(i, end='\t')



# Вам на обработку пришёл огромнейший файл с данными. Настолько огромный,
# что при его открытии компьютер просто зависает, так как данные не помещаются в оперативной памяти
# вашего суперкомпьютера (не очень-то и «супер»).
# В файле numbers.txt есть N чисел, разделённых пробелами и литералом пропуска строки.
# Напишите программу, которая подсчитает общую сумму чисел в файле.
# Для считывания файла реализуйте специальный генератор.

def file_parser(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            clear_line_sum = sum(map(int, line.rstrip().split()))
            # https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-map/
            yield clear_line_sum

all_sum = 0
# for num in file_parser("nums.txt"):
#     all_sum += num