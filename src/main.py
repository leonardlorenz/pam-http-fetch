#!/usr/bin/env python
import requests
from os import environ

DOMAIN              = environ['PAM_HTTP_PROVIDER_DOMAIN']
PORT                = environ['PAM_HTTP_PROVIDER_PORT']
URI                 = environ['PAM_HTTP_PROVIDER_URI']
OUTPUT_FILE_PATH    = environ['PAM_HTTP_OUTPUT_FILE_PATH']
TOKEN               = environ['PAM_HTTP_AUTHENTICATION_TOKEN']

users = requests.get(
        'http://' + DOMAIN + ':' + PORT + '/' + URI,
        headers={'Authorization' : TOKEN})
user_list = users.json()

print(user_list)

with open(OUTPUT_FILE_PATH, 'w') as f:
    f.write("root")
    for user in user_list:
        f.write(str(user['username']) + '\n')
