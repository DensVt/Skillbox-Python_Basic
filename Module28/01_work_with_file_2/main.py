import os

class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Ошибка типа {exc_type} произошло: {exc_val}.")
        return True

with File("example.txt", "w") as file:
    file.write("all ok!")

with File("example.txt", "r") as file:
    reading = file.read()
    print(reading)