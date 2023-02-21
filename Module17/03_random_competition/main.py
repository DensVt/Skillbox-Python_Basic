import random

fst_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
snd_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winning_team = [fst_team[elem] if fst_team[elem] > snd_team[elem] else snd_team[elem] for elem in range(20)]

print(f"Первая команда: {fst_team}"
      f"\nВторая команда: {snd_team}"
      f"\nПобедители тура: {winning_team}")
