file = open("C:/PycharmProjects/skillbox/Python_Basic/Module22/02_zen_of_python/zen.txt").read().lower()
letters = [elem for elem in file if elem in "abcdefghijklmnopqrstuvwxyz"]

print("Количество букв в файле:", len(letters),
      "\nКоличество слов в файле:", len(file.split()),
      "\nКоличество слов в файле:", len(file.split('\n')),
      "\nНаиболее редкая буква:", min(letters, key=letters.count))



