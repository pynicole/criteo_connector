# auth.py
import requests, time
from config import CLIENT_ID, CLIENT_SECRET, TOKEN_URL, REDIRECT_URI

class CriteoAuth:
    def __init__(self):
        self.token = None
        self.token_expiry = 0

    def is_token_expired(self):
        return time.time() >= self.token_expiry

    def authenticate(self, auth_code):
        data = {
            'grant_type': 'authorization_code',
            'code': auth_code,
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        # response = requests.post(TOKEN_URL, data=data)
        #  self._process_response(response)
        self._process_response(None)  # Directly call with mock

    def refresh_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }
        # response = requests.post(TOKEN_URL, data=data)
        # self._process_response(response)
        self._process_response(None)  # Directly call with mock

    def _process_response(self, response):
        # MOCK response to simulate success
        self.token = "mock_access_token"
        self.token_expiry = time.time() + 3600

    def get_token(self):
        if self.is_token_expired():
            raise Exception("Token expired. Refresh required.")
        return self.token
    
