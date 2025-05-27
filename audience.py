# audience.py
import requests
from throttle import rate_limit

@rate_limit
def create_audience_segment(auth, advertiser_id, name):
    headers = {
        'Authorization': f'Bearer {auth.get_token()}',
        'Content-Type': 'application/json'
    }
    payload = {
        "data": {
            "type": "AudienceSegment",
            "attributes": {
                "name": name,
                "advertiserId": advertiser_id,
                "subType": "ContactList"
            }
        }
    }
    url = f"https://api.criteo.com/2023-10/audiences"
    res = requests.post(url, headers=headers, json=payload)
    if res.status_code != 201:
        raise Exception(f"Create failed: {res.text}")
    segment = res.json()["data"]
    return {segment["id"]: segment["attributes"]["name"]}

@rate_limit
def search_segments_by_advertiser(auth, advertiser_id):
    headers = {'Authorization': f'Bearer {auth.get_token()}'}
    url = f"https://api.criteo.com/2023-10/audiences?advertiserIds={advertiser_id}"
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"Search failed: {res.text}")
    return [
        {
            "id": s["id"],
            "name": s["attributes"]["name"],
            "advertiserId": s["attributes"]["advertiserId"]
        }
        for s in res.json().get("data", [])
    ]
