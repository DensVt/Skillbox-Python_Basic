while True:
    ip_address = input("Введите IP: ").split(".")
    for symbol in ip_address:
        if len(ip_address) != 4:
            print("Адрес - это четыре числа, разделенные точками")
            break
        elif not symbol.isdigit():
            print(f"{symbol}-это не целое число")
            break
        elif not (0 <= int(symbol) <= 255):
            print(f"{symbol} превышает 255.")
            break
    else:
        print("IP-адрес корректен.")
        break
