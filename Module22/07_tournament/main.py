with open("first_tour.txt", "w", encoding="utf-8") as first_tour:
    first_tour.write("80\n")
    first_tour.write("Ivanov Serg 80\n")
    first_tour.write("Sergeev Petr 92\n")
    first_tour.write("Petrov Vasiliy 98\n")
    first_tour.write("Vasiliev Maxim 78")

with open("first_tour.txt", "r", encoding="utf-8") as new_file:
    k = int(new_file.readline())
    my_list = []

    for line in new_file:
        new_line = line.split()
        if new_line != [] and int(new_line[-1]) > k:
            my_list.append(new_line)

my_list.sort(key=lambda a: int(a[-1]))
my_list.reverse()

count = str(len(my_list))
out = []
wins_cnt = 1

for elem in my_list:
    name = str(elem[0][0]) + "."
    winners = str(wins_cnt) + ") " + name + " " + elem[1] + " " + elem[-1]
    out.append(winners)
    wins_cnt += 1

with open("second_tour.txt", "w", encoding="utf-8") as file_out:
    file_out.write(count + "\n".join(out))

for elem in out:
    print(elem)
