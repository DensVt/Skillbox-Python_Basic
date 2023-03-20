import requests
import json

res = requests.get('https://swapi.dev/api/starships/10')
data = json.loads(res.text)

pilot_urls = data['pilots']
pilots_data = []

for pilot_url in pilot_urls:
    pilot_result = requests.get(pilot_url)
    pilot_data = json.loads(pilot_result.text)
    pilots_data.append({
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': pilot_data['homeworld'],
        'homeworld_info': requests.get(pilot_data['homeworld']).json()
    })

millennium_falcon_data = {
    'name': data['name'],
    'max_speed': data['max_atmosphering_speed'],
    'class': data['starship_class'],
    'pilots': pilots_data
}

print(json.dumps(millennium_falcon_data, indent=4))

with open('millennium_falcon.json', 'w') as file:
    json.dump(millennium_falcon_data, file, indent=4)
