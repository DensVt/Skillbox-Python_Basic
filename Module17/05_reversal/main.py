line = input("Введите строку: ")
check = line[line.find("h") + 1: line.rfind("h")][::-1]

print(f"Развёрнутая последовательность между первым и последним h: {check}")
