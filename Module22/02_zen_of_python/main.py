with open('zen.txt') as file:
    for elem in reversed(file.readlines()):
        print(elem, end='')
