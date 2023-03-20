# import requests
# import json

# my_reg = requests.get(
#     'https://swapi.dev/api/people/3/')
# # print(my_reg.text)
# data = json.loads(my_reg.text)   # десериализация json

# with open('my_test.json', 'w') as file:
#     json.dump(data, file, indent=4)   # сериализация json

# with open('my_test.json', 'r') as file:
#     data = json.load(file)

# print(data)


# Задача 1. Звёздные войны
# Повторите пример парсинга, разобранный в уроке: перейдите на сайт с API, посвящённый вселенной Star Wars.

# После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/).

# Затем напишите программу, которая парсит данные об этом человеке, изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла.

# Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка. В том же коде спарсите эту ссылку и посмотрите, что там.

# Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать, поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.

import requests
import json

# res = requests.get('https://swapi.dev/api/people/3/')
# if res.status_code == 200:
#     json_dict = json.loads(res.text)
#     json_dict['name'] = input('Введите имя: ')
#     with open('swap.json', 'w') as file:
#         json.dump(json_dict, file, indent=4)

#     # доп
#     result = requests.get(json_dict['homeworld'])
#     print('Вывод того что хранится по ссылке: ')
#     print(result.text)


# Задача 2. Документация API
# Обычно к открытым API прилагается подробная документация,
# где описывается логика формирования ссылок и какие данные по ним можно получать (или отправлять!).
#
# Изучите документацию того же сайта по «Звёздным войнам».
# Поэкспериментируйте с получением данных о кораблях, планетах, фильмах и так далее.
# А ещё попробуйте библиотеку swapi (о ней также в документации)
# и с её помощью выведите начало сюжета из фильма «Новая надежда» (A New Hope).


# import swapi

# print(swapi.get_film(1))
# библиотека не работает, получить начало сюжета можно напрямую

# res = requests.get('https://swapi.dev/api/films/1/')

# json_dict = json.loads(res.text)
# print(json_dict['opening_crawl'])

# with open('film_history.json', 'w') as file:
#     json.dump(json_dict['opening_crawl'], file, indent=4)
