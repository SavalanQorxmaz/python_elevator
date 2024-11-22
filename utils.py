import requests

users = requests.get('https://jsonplaceholder.typicode.com/users')
users = users.json()

users = [p['name'] for p in users]

# print(users)