import requests
import pytest

HOST = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'b0c5104a95cc4ac1308b976d6be206ce'
HEADER = {'Content-Type' : 'application/json',
'trainer_token' : 'b0c5104a95cc4ac1308b976d6be206ce'}
TRAINER_ID = '4755'

def test_status_code():
    response = requests.get(url = f'{HOST}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name','Друид')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{HOST}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value