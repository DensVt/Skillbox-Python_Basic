word = input("Введите текст: ")
search = set("уоеи")
word = [elem for elem in word if elem in search]

print(f"Список гласных букв: {word}"
      f"\nДлина списка: {len(word)}")
