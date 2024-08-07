import os
import requests
from dotenv import load_dotenv

load_dotenv()


def get_iata_codes():

    sheety_api = "https://api.sheety.co/f2cc9daa00cc57ef59fe38c1ed2ebd85/flightDeals/prices"
    sheety_headers = {
        "Authorization": os.getenv("SHEETY_TOKEN")
    }

    amadeus_api = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
    amadeus_headers = {
        "Authorization": os.getenv("AMADEUS_TOKEN")
    }

    sheety_response = requests.get(url=sheety_api, headers=sheety_headers)
    cities_list = sheety_response.json()["prices"]

    i = 2
    for location in cities_list:
        amadeus_parameters = {
            "keyword": location["city"]
        }
        amadeus_response = requests.get(url=amadeus_api, headers=amadeus_headers, params=amadeus_parameters)
        city_code = amadeus_response.json()["data"][0]["iataCode"]
        body = {
            "price": {
                "city": location["city"],
                "iataCode": city_code,
                "lowestPrice": 50
            }
        }
        sheety_put_res = requests.put(url=f"{sheety_api}/{i}", headers=sheety_headers, json=body)
        print(sheety_put_res.text)
        i += 1


def get_new_token():
    amadeus_token_api = "https://test.api.amadeus.com/v1/security/oauth2/token"
    amadeus_headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    amadeus_parameters = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("AMADEUS_API_KEY"),
        "client_secret": os.getenv("AMADEUS_API_SECRET")
    }
    res = requests.post(url=amadeus_token_api, headers=amadeus_headers, data=amadeus_parameters)
    print(res.json())
