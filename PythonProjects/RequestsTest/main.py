import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b8e0bb9837c89bad3d19caf6b2b1940'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '4430'

body_create = {
    "name": "Boo",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}


#Создание покемона
response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id'] #сохраняем в переменную pokemon_id id созданного покемона

#Смена имени покемона
body_name = {
    "pokemon_id": pokemon_id,
    "name": "Pikachu",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)

#Поймать покемона в покебол
body_add_pokeball = {
    "pokemon_id": pokemon_id,
}
response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)



