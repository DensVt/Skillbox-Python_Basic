violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

how_many_songs = int(input("Сколько песен выбрать? "))
count = 0
for num in range(how_many_songs):

    name_of_the_track = input(f"Название {num + 1}-й песни: ")
    for number in violator_songs:
        if number[0] == name_of_the_track:
            count = round(count + number[1], 2)

print(f"\nОбщее время общее время звучания песен: {count} минут(ы)")
