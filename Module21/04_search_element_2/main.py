site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, max_depth=None, depth=1):
    result = None
    if max_depth and max_depth < depth:
        return result
    if key in struct:
        return struct[key]
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, depth=depth + 1)
            if result:
                break
    return result


key = input('Введите искомый ключ: ')
user_choice = input("Хотите ввести максимальную глубину? Y/N: ").upper()

if user_choice == "Y":
    maximum_depth = int(input('Введите максимальную глубину: '))
    value_key = find_key(site, key, maximum_depth)
    print(f'Значение ключа: {value_key}')
else:
    value = find_key(site, key)
    print(f'Значение ключа: {value}')





"""
site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}


def find_key(data, tag, depth=None):
    if depth is None or depth >= 1:
        if tag in data:
            return data[tag]
    else:
        return None
    for elem in data.values():
        if isinstance(elem, dict):
            result = find_key(elem, tag, depth - 1)
            if result:
                break
    else:
        result = None
    return result


def search_element(data, tag):
    result = None
    if tag in data:
        return data[tag]
    for key, value in data.items():
        if isinstance(value, dict):
            result = search_element(value, tag)
            if result:
                return result
    return result

key = input('Введите искомый ключ: ')
user_choice = input("Хотите ввести максимальную глубину? Y/N: ").upper()

if user_choice == "Y":
    maximum_depth = int(input('Введите максимальную глубину: '))
    value_key = find_key(site, key, maximum_depth)
    print(f'Значение ключа: {value_key}')
else:
    value = search_element(site, key)
    print(f'Значение ключа: {value}')
"""