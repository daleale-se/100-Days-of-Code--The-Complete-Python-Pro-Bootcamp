import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -34.757385
MY_LONG = -58.596478


#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hour = time_now.hour

    if sunset < now_hour < sunrise:
        return True
    return False


def send_email():
    my_email = "daleale.se@gmail.com"
    password = "lpad ipnz zavi eahf"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: ISS\n\n Head up amigo!")


# If the ISS is close to my current position
# ,and it is currently dark
# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(1)
    if is_iss_overhead() and is_night():
        send_email()
        print("email sent")
    else:
        print("nothing happen")
