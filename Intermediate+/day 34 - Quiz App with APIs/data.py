import requests

AMOUNT = 10
TYPE = "boolean"

parameters = {
    "amount": AMOUNT,
    "type": TYPE
}

trivia_api = "https://opentdb.com/api.php"

response = requests.get(url=trivia_api, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
