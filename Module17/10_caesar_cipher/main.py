string = input("Введите сообщение: ")
user_shift = int(input("Введите сдвиг: "))
alphabet = [chr(elem) for elem in range(ord("а"), ord("я") + 1)]
char_list = [(alphabet[(alphabet.index(sym) + user_shift) % 32] if sym in alphabet else sym) for sym in string]
print("Зашифрованное сообщение: ", "".join(char_list))

"""
def get_index(symbol, shift, alpha):
    index = alpha.index(symbol)
    if index + shift > len(alpha) - 1:
        index = index + shift - len(alpha)
    else:
        index += shift
    return index

message = input("Введите сообщение: ").lower()
shift = int(input("Введите сдвиг: "))
alpha = [chr(elem) for elem in range(ord("а"), ord("я") + 1)]
encrypted_string = ''
for symbol in message:
    if symbol in alpha:
        encrypted_string += alpha[get_index(symbol, shift, alpha)]
    else:
        encrypted_string += symbol

print(f"Зашифрованное сообщение: {encrypted_string}")
"""
