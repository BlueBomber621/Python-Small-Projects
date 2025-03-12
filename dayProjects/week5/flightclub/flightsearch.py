import requests
import os
from datetime import datetime, timedelta

class FlightSearcher:
    def __init__(self):
        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_API_SECRET"]
        self._api_token = self._get_new_token()

    def _get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=headers, data=body)
        return response.json()['token_type'] + " " + response.json()['access_token']

    def search_flight_deals(self, data):
        headers = {
            "accept": "application/vnd.amadeus+json",
            "Authorization": self._api_token
        }
        params = {
            "originLocationCode": "SLC", # Salt Lake City
            "destinationLocationCode": data["iataCode"],
            "departureDate": (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d'),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 250
        }
        response = requests.get(url="https://test.api.amadeus.com/v2/shopping/flight-offers", params=params, headers=headers)
        response.raise_for_status()
        return [item["price"]["grandTotal"] for item in response.json()["data"]]
