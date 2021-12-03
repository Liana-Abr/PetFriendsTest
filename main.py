from api import PetFriends

pf = PetFriends()
status, result = pf.get_api_key("vimeko3800@mail.ru", "123456789")
auth_key = result['key']
print(status, result, auth_key)

status, res = pf.get_api_pet_list(auth_key, "my_pets")
pet_id = res['pets'][0]['id']
pet_id2 = res['pets'][1]['id']
pet_id3 = res['pets'][2]['id']
print(status, res, "\n HHHHHHHHHHHH " + pet_id)