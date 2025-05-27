# config.py
import os
from dotenv import load_dotenv
load_dotenv()

CLIENT_ID = os.getenv("CRITEO_CLIENT_ID")
CLIENT_SECRET = os.getenv("CRITEO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("CRITEO_REDIRECT_URI")
TOKEN_URL = "https://api.criteo.com/oauth2/token"
AUTH_URL = "https://api.criteo.com/oauth2/authorize"
# API_BASE = "https://api.criteo.com"
API_BASE = "http://localhost:5000"  # Instead of real Criteo API
