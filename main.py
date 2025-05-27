# main.py
from auth import CriteoAuth
from portfolio import get_portfolio
from audience import create_audience_segment, search_segments_by_advertiser

def main():
    criteo = CriteoAuth()

    # TEMP: Simulate getting token manually
    print("Go to the following URL to get your auth code:")
    print("https://api.criteo.com/oauth2/authorize?response_type=code&client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI")
    auth_code = input("Paste the auth code here: ")
    criteo.authenticate(auth_code)

    print("Getting portfolio...")
    portfolios = get_portfolio(criteo)
    print("Advertisers:", portfolios)

    if portfolios:
        advertiser_id = list(portfolios.keys())[0]
        print("Creating audience...")
        segment = create_audience_segment(criteo, advertiser_id, "Test Segment")
        print("Segment Created:", segment)

        print("Searching for audience segments...")
        segments = search_segments_by_advertiser(criteo, advertiser_id)
        print("Segments Found:", segments)

if __name__ == "__main__":
    main()
