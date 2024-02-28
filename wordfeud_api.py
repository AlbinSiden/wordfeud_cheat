import requests
import json
import hashlib

class WordfeudAPI:
    def __init__(self):
        self.base_url = 'https://api.wordfeud.com'
        self.headers = {
            'User-Agent': 'WebFeudClient/3.5.12 (Android 5.1.1)',
            'Content-Type': 'application/json; charset=UTF-8',
            'Connection': 'close',
        }
        self.session = requests.Session()

    def encrypt_password(self, password):
        password += "JarJarBinks9"
        sha1_hash = hashlib.sha1(password.encode()).hexdigest()
        return sha1_hash

    def login(self, email, password):
        url = f'{self.base_url}/wf/user/login/email/'

        hashed_password = self.encrypt_password(password)

        json_data = {
            'email': email,
            'password': hashed_password,
            'language_code': 'en',
            'device_id': '9e368f55b52bfcab',
            'platform': 'android',
        }

        response = self.session.post(url, json=json_data, headers=self.headers, verify=False)
        sessionid = response.cookies.get('sessionid')

        return sessionid

    def get_boards(self, session_id):
        url = f'{self.base_url}/wf/user/games/detail/'
        cookies = {'sessionid': session_id}
        params = {
            'known_tile_points': '',
            'known_boards': ''
        }

        response = self.session.post(url, params=params, headers=self.headers, cookies=cookies, verify=False)
        data = json.loads(response.text)
        boards = data['content']['games']

        return boards

api = WordfeudAPI()

sid = api.login('abbezidde@gmail.com', "Snoddas42!")
print(sid)
boards = api.get_boards(sid)
