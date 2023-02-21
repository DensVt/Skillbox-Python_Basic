
def answer(file_str):
    name, mail, age = file_str.split(" ")
    symbol = ("@", ".")
    age = int(age)
    if name.isalpha() is False:
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if age not in range(10, 100):
        raise ValueError("Поле «Имя» содержит НЕ только буквы")

    for char in symbol:
        if char not in mail:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    return file_str


with open("registrations.txt", "r", encoding="utf-8") as file, \
        open("registration_bad.log", "a", encoding="utf-8") as error, \
        open("registration_good.log", "a", encoding="utf-8") as good:
    for i, elem in enumerate(file):
        # print(elem, end="")
        try:
            str_file = answer(elem)
        except (NameError, ValueError, SyntaxError) as exc:
            error.write(str(i) + str(exc) + "\n")
        else:
            good.write(elem + "\n")
