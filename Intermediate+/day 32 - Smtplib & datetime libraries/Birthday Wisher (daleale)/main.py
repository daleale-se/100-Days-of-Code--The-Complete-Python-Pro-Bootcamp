##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import random
import datetime as dt


def generate_letter_to(name):
    all_letter = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter = random.choice(all_letter)
    with open(f"./letter_templates/{random_letter}", "r") as letter_file:
        message = letter_file.read()
        message = message.replace("[NAME]", name)
        return f"Subject: Happy Birthday!\n\n{message}"


def send_email(letter: str, destiny_email: str):
    my_email = "daleale.se@gmail.com"
    password = "lpad ipnz zavi eahf"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=destiny_email,
            msg=letter)


def main():

    now = dt.datetime.now()
    now_month = now.month
    now_day = now.day

    df = pandas.read_csv("birthdays.csv")
    df = df[df.month == now_month]
    df = df[df.day == now_day]

    for (_, row) in df.iterrows():
        letter = generate_letter_to(row["name"])
        send_email(letter, row["email"])


main()
