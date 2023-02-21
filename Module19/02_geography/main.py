data_set = {}
amount_country = int(input("Кол-во стран: "))

for i_elem in range(amount_country):
    value = input("{}-я страна: ".format(i_elem + 1)).split()
    for i_city in value[1:]:
        data_set[i_city] = value[0]

for i_elem in range(3):
    city = input("\n{}-й город: ".format(i_elem + 1))
    country = data_set.get(city)

    if country:
        print("Город {} расположен в стране {}.".format(city, country))
    else:
        print("По городу {} данных нет.".format(city))