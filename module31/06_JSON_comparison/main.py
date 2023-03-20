import json

with open('json_old.json', 'r') as file:
    data_old = json.load(file)

with open('json_new.json', 'r') as file:
    data_new = json.load(file)

print('Данные, загруженные из json_old.json: \n', data_old, '\n')
print('Данные, загруженные из json_new.json: \n', data_new, '\n')

diff_list = ["services", "staff", "datetime"]
results = {}

for key in diff_list:
    if data_old['data'][key] != data_new['data'][key]:
        results[key] = data_new['data'][key]

print('Вывод результата: \n', results)

with open('result.json', 'w') as file:
    json.dump(results, file)
