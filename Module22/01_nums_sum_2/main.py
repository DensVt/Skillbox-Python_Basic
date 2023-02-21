# numbers = open("numbers.txt", "r")
# print("Содержимое файла numbers.txt")
#
# all_sum = 0
# for elem in numbers:
#     print(elem, end='')
#     clear = elem.rstrip()
#     if clear:
#         all_sum += int(clear)
# numbers.close()
# print("\nСодержимое файла answer.txt")
# print(all_sum)
#
# answer = open("answer.txt", "w")
# answer.write(str(all_sum))
# answer.close()

with open("numbers.txt", "r") as file1, open("answer.txt", "w") as file2:
    file2.write(str(sum(map(int, filter(lambda x: x, (
        line.replace("\n", "").strip()
        for line in file1
    ))))))