# portfolio.py
import requests
from throttle import rate_limit
from config import API_BASE


@rate_limit
def get_portfolio(auth):
    headers = {'Authorization': f'Bearer {auth.get_token()}'}
    # url = f"https://api.criteo.com/2023-10/marketing-solutions/portfolios"
    url = f"{API_BASE}/2023-10/marketing-solutions/portfolios"
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"Failed to fetch portfolio: {res.text}")
    portfolios = res.json().get("data", [])
    return {p["id"]: p["attributes"]["name"] for p in portfolios}
