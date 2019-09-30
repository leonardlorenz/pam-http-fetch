#!../venv/bin/python3
import requests
import sys
from configparser import ConfigParser

config = ConfigParser()
config.read('../config.ini')
default = config['default']

DOMAIN           = default['PAM_HTTP_PROVIDER_DOMAIN']
PORT             = default['PAM_HTTP_PROVIDER_PORT']
URI              = default['PAM_HTTP_PROVIDER_URI']
OUTPUT_FILE_PATH = default['PAM_HTTP_OUTPUT_FILE_PATH']
TOKEN            = default['PAM_HTTP_AUTHENTICATION_TOKEN']

users = requests.get(
        'http://' + DOMAIN + ':' + PORT + '/' + URI,
        headers={'Authorization' : TOKEN})
user_list = users.json()

print(user_list)

with open(OUTPUT_FILE_PATH, 'w') as f:
    for user in user_list:
        f.write(str(user['username']) + '\n')
