import random
import smtplib
from datetime import *


def main():

    # my_email = "daleale.se@gmail.com"
    # password = "lpad ipnz zavi eahf"
    #
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=my_email, password=password)
    #     connection.sendmail(
    #         from_addr=my_email,
    #         to_addrs="ale.salas271102@gmail.com",
    #         msg="Subject:Hi bitch\n\nI'm Ale from the future"
    #     )

    # now = date.datetime.now()
    # year = now.year
    # month = now.month
    # day = now.day
    # hour = now.hour
    # minute = now.minute
    # second = now.second
    # day_of_week = now.weekday()
    # print(year, month, day, hour, minute, second, day_of_week)
    # date_of_birth = date.datetime(year=2002, month=11, day=27, hour=5)
    # print(date_of_birth)

    message_on_day = "Saturday"
    now = datetime.now()
    if now.strftime("%A") == message_on_day:

        with open("quotes.txt") as file_quotes:
            quotes = file_quotes.readlines()
            quote = random.choice(quotes)

        my_email = "daleale.se@gmail.com"
        password = "lpad ipnz zavi eahf"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="ale.salas271102@gmail.com",
                msg=f"Subject: Quote\n\n{quote}"
            )


main()
