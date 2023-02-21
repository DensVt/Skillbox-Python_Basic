def score_key(a):
    return a[1][0] * 100000 - a[1][1]

score_table = dict()
number_rows = int(input("Сколько записей вносится в протокол? "))
print("Введите результат - имя участника (через пробел)")

for time in range(number_rows):
    res, name = input("{0}-ая запись: ".format(time + 1)).split()
    res = int(res)
    if res in score_table:
       if res >= score_table[name][0]:
           score_table[name][0] = res
           score_table[name][1] = time
    else:
        score_table[name] = [res, time]

scores = list(score_table.items())
scores.sort(key=score_key, reverse=True)
print("\n Итоги соревнований: ")

for winner_index in 0, 1, 2:
    print(f" {winner_index + 1}-e место. {scores[winner_index][0]} ", end=' ')
    print(f"({scores[winner_index][1][0]})", sep=' ')
