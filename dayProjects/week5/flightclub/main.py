from spreadsheet import DealsSheet
from flightsearch import FlightSearcher
import os

SHEET_ENDPOINT = "Your Sheety Endpoint"
os.environ["SHEET_AUTH"] = "Your Sheety Auth (Include 'Basic '/'Bearer '/'... ')"
os.environ["AMADEUS_API_KEY"] = "Your Amadeus API Key"
os.environ["AMADEUS_API_SECRET"] = "Your Amadeus API Secret"

deals_sheet = DealsSheet(SHEET_ENDPOINT)
data = deals_sheet.get_info()['sheet1']
flight_searcher = FlightSearcher()

def get_flight(city):
    print(f"Getting flight prices for {city['city']}")
    prices = flight_searcher.search_flight_deals(city)
    if len(prices) > 0:
        prices = min(prices)
        deals_sheet.put_info({'sheet1': {'city': city['city'], 'iataCode': city['iataCode'], 'lowestPrice': round(float(prices), 2)}}, city['id'])
        print(f"{city['city']}: {prices}")
    else:
        print(f"No flights found for {city['city']}")

# Too many calls, unreliable, a timeframe no longer works for the API allowing only one day to be used, 
# providing little data, and additionally makes too many calls for few cities often.
[get_flight(item) for item in deals_sheet.get_info()['sheet1']]
