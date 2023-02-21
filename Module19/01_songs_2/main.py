violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

user_choice = input("Сколько песен выбрать? ")
all_time = 0

for elem in range(len(user_choice)):
    song = input("Название {}-ой песни: ".format(elem + 1))
    all_time += round(violator_songs.get(song, 0), 2)

print(f"Общее время звучания песен: {all_time} минуты")
