import os

path = os.path.abspath(os.path.join("..", "..", "module14"))
size = 0
path, dirs, files = next(os.walk(path))

for i_elem in files:
    element = os.path.join(path, i_elem)
    size += os.path.getsize(element)

print(path)
print("Размер каталога (в Кб):", size / 1024)
print("Количество подкаталогов:", len(dirs))
print("Количество файлов:", len(files))