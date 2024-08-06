from datetime import datetime

import requests

USERNAME = "daleale"
TOKEN = "Eeoodd123789@"
GRAPH_ID ="test-graph-01"

pixila_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixila_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixila_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Drink water",
    "unit": "Lt",
    "type": "float",
    "color": "kuro"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixila_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_pixel_body = {
    "date": "20240705",
    "quantity": "3",
}

# response = requests.post(url=post_pixel_endpoint, json=post_pixel_body, headers=headers)
# print(response.text)

put_pixel_body = {
    "quantity": "6",
}

edit_day = "20240805"
put_pixel_endpoint = f"{pixila_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{edit_day}"

# response = requests.put(url=put_pixel_endpoint, json=put_pixel_body, headers=headers)
# print(response.text)

erase_day = "20240705"
delete_pixel_endpoint = f"{pixila_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{erase_day}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
