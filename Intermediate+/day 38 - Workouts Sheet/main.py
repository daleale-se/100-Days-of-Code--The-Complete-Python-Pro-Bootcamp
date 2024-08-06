from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")

nutritionix_api = "https://trackapi.nutritionix.com"
post_exercise = "/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Tell me which exercises you did: ")

body = {
    "query": query
}

res = requests.post(url=f"{nutritionix_api}{post_exercise}", json=body, headers=nutritionix_headers)
list_exercises = res.json()["exercises"]

date_now = datetime.now()
today_format = date_now.strftime("%d/%m/%Y")
time_format = date_now.strftime("%H:%M:%S")

list_workout = []

for exercise in list_exercises:
    workout = {
        "date": today_format,
        "time": time_format,
        "exercise": exercise["name"].capitalize(),
        "calories": exercise["nf_calories"],
        "duration": int(exercise["duration_min"])
    }
    list_workout.append(workout)

sheety_post_api = "https://api.sheety.co/f2cc9daa00cc57ef59fe38c1ed2ebd85/workoutTracking/workouts"
SHEETY_AUTHORIZATION = os.getenv("SHEETY_TOKEN")

sheety_headers = {
    "Authorization": SHEETY_AUTHORIZATION
}

for workout in list_workout:
    body = {"workout": workout}
    res = requests.post(url=sheety_post_api, json=body, headers=sheety_headers)
    print(res.text)
