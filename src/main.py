import requests
import json
import sys
import os

DOMAIN = os.environ['PAM_HTTP_PROVIDER_DOMAIN']
PORT = os.environ['PAM_HTTP_PROVIDER_PORT']
URI = os.environ['PAM_HTTP_PROVIDER_URI']
OUTPUT_FILE_PATH = os.environ['PAM_HTTP_OUTPUT_FILE_PATH']
TOKEN = os.environ['PAM_HTTP_AUTHENTICATION_TOKEN']

users = requests.get(
        'http://' + DOMAIN + ':' + PORT + '/' + URI,
        headers={'Authorization' : TOKEN})
user_list = users.json()

print(user_list)

with open(OUTPUT_FILE_PATH, 'w') as f:
    for user in user_list:
        f.write(str(user['username']) + '\n')
