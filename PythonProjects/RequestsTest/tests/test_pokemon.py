import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'  #задаем переменные
TOKEN = 'c4b8e0bb9837c89bad3d19caf6b2b1940'
HEADER = {'Content-Type':'application/json', "trainer_token":TOKEN}
TRAINER_ID = '4430'

#проверка, что в ответе co списком тренеров приходит статус код 200 ОК
def test_status_code():
    response_trainers = requests.get(url = f'{URL}/trainers')
    assert response_trainers.status_code == 200

#проверка, что в ответе приходит строчка с именем твоего тренера
def test_part_of_response():
    response_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_trainers.json()['data'][0]['trainer_name'] == 'Ash'
