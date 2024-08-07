import os
import requests
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()

# This class is responsible for talking to the Google Sheet.

class DataManager:
    def __init__(self):
        self.destinations = None
        self.do_fetch()

    def do_fetch(self):

        sheety_api = "https://api.sheety.co/f2cc9daa00cc57ef59fe38c1ed2ebd85/flightDeals/prices"
        sheety_headers = {
            "Authorization": os.getenv("SHEETY_TOKEN")
        }

        res = requests.get(url=sheety_api, headers=sheety_headers)
        self.destinations = res.json()["prices"]

    def do_search(self, flight_search: FlightSearch):
        for destiny in self.destinations:
            flight_search.cheapest_flights(destiny)
