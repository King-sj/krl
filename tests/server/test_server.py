import requests
url = 'http://localhost:5001'

# res = requests.post(url + '/create_user').json()
# print(res)
# user1_id = res['user_id']
user1_id = '8b439ae5-08b4-488c-b97f-af65a412eed2'

res = requests.post(url + f'/{user1_id}/run', json={'input': '3'}).json()
print(res)