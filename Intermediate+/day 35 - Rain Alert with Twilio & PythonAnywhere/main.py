import requests
import os
from twilio.rest import Client

# I use export to set env variables but didn't work
# I have to add environment variables in the run configurations at this file

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

API_KEY = os.environ.get("OWM_API_KEY")
API_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"

# Miami
# LAT = 25.761681
# LONG = -80.191788

# Gonzalez Catan
LAT = -34.75
LONG = -58.6

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "cnt": 4
}


def gonna_rain(weather_forecast):
    for forecast in weather_forecast:
        if int(forecast["weather"][0]["id"]) < 700:
            return True
    return False


response = requests.get(url=API_END_POINT, params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data["list"]

if gonna_rain(weather_list):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella bro",
        from_='+12517662856',
        to='+541131821946')
    print(message.status)
else:
    print("nothing happen")
