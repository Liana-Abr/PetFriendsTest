import pytest
from api import PetFriends
from main import auth_key, pet_id, pet_id2, pet_id3

pf = PetFriends()

def test_get_api_for_valid_user(email="vimeko3800@mail.ru", password="123456789"):
    status, result = pf.get_api_key(email, password)
    assert 'key' in result
    assert status == 200
    
def test_get_api_for_invalid_user(email="", password=""):
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_get_api_pet_list_for_valid_key(auth_key= auth_key, filter = "my_pets"):
    status, result = pf.get_api_pet_list(auth_key, filter)
    assert status == 200
    assert 'pets' in result

def test_get_api_for_pet_list_invalid_key(auth_key= "hhh", filter = "my_pets"):
    status, result = pf.get_api_pet_list(auth_key, filter)
    assert status == 403

def test_post_api_pet_for_valid_key_data(auth_key= auth_key, name="kot", animal_type="кот", age='1'):
    status, result = pf.post_api_create_pet(auth_key, name, animal_type, age)
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert status == 200

def test_post_api_pet_for_invalid_key(auth_key= "hhh", name="kkk", animal_type="кот", age=-5):
    status, result = pf.post_api_create_pet(auth_key, name, animal_type, age)
    assert status == 403

def test_post_api_pet_for_invalid_data(auth_key= auth_key, name= None, animal_type=7, age="hh"):
    status, result = pf.post_api_create_pet(auth_key, name, animal_type, age)
    assert status == 400

def test_post_api_delete_pet_for_valid_key(auth_key= auth_key, pet_id = pet_id):
    status, result = pf.delete_api_pet(auth_key, pet_id)
    assert status == 200

def test_post_api_delete_pet_for_invalid_key(auth_key= "hhh", pet_id = pet_id):
    status, result = pf.delete_api_pet(auth_key, pet_id)
    assert status == 403

def test_put_api_pet_for_valid_key_data(auth_key= auth_key, pet_id = pet_id2, name="Hhh", animal_type="кот", age='-5-'):
    status, result = pf.put_api_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 200

def test_put_api_pet_for_invalid_key(auth_key= "hhh", pet_id = pet_id2, name="Hhh", animal_type="кот", age=-5):
    status, result = pf.put_api_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 403

def test_put_api_pet_for_invalid_data(auth_key= auth_key, pet_id = 'hhh', name= False, animal_type=7, age="hh"):
    status, result = pf.put_api_pet(auth_key, pet_id, name, animal_type, age)
    assert status == 400

