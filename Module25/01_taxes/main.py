class Property:
    def __init__(self, worth):
        self.worth = worth


class Apartment(Property):
    def tax(self):
        return self.worth / 1000


class Car(Property):
    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    def tax(self):
        return self.worth / 500


total_tax = 0

money = int(input("Ваш кэш: "))

apartment_price = int(input("Ценник квартиры: "))
car_price = int(input("Ценник машины: "))
country_house_price = int(input("Ценник дачи: "))

tax_list = [Apartment(apartment_price), Car(car_price), CountryHouse(country_house_price)]

for items in tax_list:
    print('Налог на {} составит {}'.format(
        items.worth,
        items.tax()
    ))
    total_tax += items.tax()

print("\nСумма налога составила", total_tax)

if total_tax > money:
    print("Вам не хватает", total_tax - money, "для расчета с налоговой")
else:
    print("Вы успешно рассчитались с налоговой, у вас на руках осталось", money - total_tax, "кэша")