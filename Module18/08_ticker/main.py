fst_string = input("Первая строка: ")
snd_string = input("Вторая строка: ")

pos = (fst_string + fst_string).find(snd_string)

if pos > -1:
    print(f'Первая строка получается из второй со сдвигом {pos}.')
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")



"""
fst_string = input("Первая строка: ")
snd_string = input("Вторая строка: ")

if snd_string == fst_string:
    print("Строки одинаковы")
else:
    if len(snd_string) != len(fst_string):
        print("Строки имеют разную длину")
    else:
        shift = 1
        flag = False
        for elem in range(len(fst_string) - 1):
            snd_string = snd_string[-1] + snd_string[:-1]
            if fst_string == snd_string:
                print(f"Первая строка получается из второй со сдвигом {shift}")
                flag = True
                break
            else:
                shift += 1
        if not flag:
            print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
"""
