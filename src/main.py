import requests
import json

DOMAIN='localhost'
PORT='8000'
URI='users/'

users = requests.get('http://' + DOMAIN + ':' + PORT + '/' + URI)

print(users.json())
