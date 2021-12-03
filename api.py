import json
import requests
from requests_toolbelt import MultipartEncoder

class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends1.herokuapp.com/"

    def get_api_key(self,
                    email: str,
                    password: str) -> json:
        
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def get_api_pet_list(self,
                    auth_key: str,
                    filter: str) -> json:
        headers = { 'auth_key' : auth_key }
        filter = {'filter': filter}
        res = requests.get(self.base_url+'api/pets', headers=headers, params = filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def post_api_create_pet(self,
                    auth_key: str,
                    name: str, 
                    animal_type: str,
                    age: int) -> json:
        headers = { 'auth_key' : auth_key }
        formData = {'name': name, 
                    'animal_type': animal_type,
                    'age': age}
        res = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data = formData)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def delete_api_pet(self,
                    auth_key: str,
                    pet_id: str) -> json:
        headers = { 'auth_key' : auth_key }
        res = requests.delete(self.base_url+f'api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def put_api_pet(self,
                    auth_key: str,
                    pet_id: str,
                    name: str,
                    animal_type: str,
                    age: int) -> json:
        headers = { 'auth_key' : auth_key }
        formData = {'name': name, 
                    'animal_type': animal_type,
                    'age': age}
        res = requests.put(self.base_url+f'api/pets/{pet_id}', data=formData, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def post_api_create_photo_pet(self,
                    auth_key: str,
                    name: str, 
                    animal_type: str,
                    age: int,
                    pet_photo: str) -> json:
        data = MultipartEncoder(
          fields = {'name': name, 
                    'animal_type': animal_type,
                    'age': age,
                    'pet_photo': (pet_photo, open("images/"+ pet_photo, 'rb'), 'image/jpeg')})
        headers = { 'auth_key' : auth_key, 'Content-Type': data.content_type}
        res = requests.post(self.base_url+'api/pets', headers=headers, data = data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
    def post_api_add_photo_pet(self,
                    auth_key: str,
                    pet_id:str, 
                    pet_photo: str) -> json:
        data = MultipartEncoder(
          fields = {'pet_photo': (pet_photo, open("images/" + pet_photo, 'rb'), 'image/jpeg')})
        headers = { 'auth_key' : auth_key, 'Content-Type': data.content_type}
        res = requests.put(self.base_url+ f'api/pets/set_photo/{pet_id}', data=data, headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
