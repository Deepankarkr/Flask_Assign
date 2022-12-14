import configparser
import json

from flask_httpauth import HTTPBasicAuth

config = configparser.ConfigParser()
config.read('config.ini')

users= json.loads(config.get('credentials', 'key_value_pair'))

auth = HTTPBasicAuth()
@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None
