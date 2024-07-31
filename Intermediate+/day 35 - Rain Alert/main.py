import requests

API_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7bbbefd378e812c98189b09e0a016fcc"
LAT = 25.761681
LONG = -80.191788

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
    print("Bring an Umbrella!")
