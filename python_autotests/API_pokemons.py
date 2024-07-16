import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b0c5104a95cc4ac1308b976d6be206ce'
HEADER = {'Content-Type' : 'application/json',
'trainer_token' : 'b0c5104a95cc4ac1308b976d6be206ce'}
# тренер id 4755
body_add_pokemon = {
    "name": "Протозавр",
    "photo_id": -1
}

body_replace = {
    "pokemon_id": "43500",
    "name": "Пивозавр",
    "photo_id": -1
}

body_add_pokeball = {
    "pokemon_id": "43500"
}

#response_add_pokemon = requests.post(url = f'{URL}/pokemons',headers=HEADER,json = body_add_pokemon)
#print(response_add_pokemon.text)

#response_replace = requests.put(url = f'{URL}/pokemons',headers=HEADER,json = body_replace)
#print(response_replace.text)

#response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball',headers=HEADER,json = body_add_pokeball)
#print(response_add_pokeball.text)
