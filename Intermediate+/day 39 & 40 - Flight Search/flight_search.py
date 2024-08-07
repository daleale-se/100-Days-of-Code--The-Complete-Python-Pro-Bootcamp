import os
import requests
from dotenv import load_dotenv
from datetime import *

load_dotenv()

# This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self):
        self.flights = None

    def cheapest_flights(self, destination):

        ORIGIN = "MAD"

        date_now = datetime.now()
        from_day = date_now.strftime("%Y-%m-%d")
        to_day = date_now + timedelta(days=180)
        to_day = to_day.strftime("%Y-%m-%d")

        amadeus_api = "https://test.api.amadeus.com/v1/shopping/flight-dates"
        amadeus_headers = {
            "Authorization": os.getenv("AMADEUS_TOKEN")
        }
        amadeus_parameters = {
            "origin": ORIGIN,
            "destination": destination["iataCode"],
            # "departureDate": f"{from_day},{to_day}"
        }

        print(destination["city"], destination["iataCode"], destination["lowestPrice"])
        res = requests.get(url=amadeus_api, headers=amadeus_headers, params=amadeus_parameters)
        print(res.json())
