shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part_name = input("Название детали: ")
count = 0
price_sum = 0

for elem in shop:
    if elem[0] == part_name:
        count += elem.count(part_name)
        price_sum += elem[1]

print(f"Количество делатей - {count}"
      f"\nОбщая стоимость - {price_sum}")
