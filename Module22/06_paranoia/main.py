import string

with open('text.txt', 'w') as text:
    text.write("Hello \n" * 4)

with open('text.txt', 'r', encoding='utf8') as text, \
        open("cipher_text.txt", "w") as cipher_text:
    
    for elem, text_translate in enumerate(text.readlines(), 1):
        lower = (string.ascii_lowercase[elem:] + string.ascii_lowercase[:elem])
        translate = {ord(a): d for (a, d) in zip(string.ascii_letters, (lower + lower.upper()))}
        cipher_text.write(str.translate(text_translate, translate))


"""
def caesar(letter, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvw \n\n'

    word = []

    for i in letter.lower():
        word.append(alphabet[(alphabet.find(i) + shift) % len(alphabet)].lower())

    return "".join(word)


with open("text.txt", "w") as text:
    text.write("Hello\n" * 4)

with open('text.txt', 'r') as text_file, \
        open('cipher_text.txt', 'w') as caesar_file:
    cont = 1
    for line in text_file:
        caesar_file.write(caesar(line.replace("\n", ""), cont))
        cont += 1
"""