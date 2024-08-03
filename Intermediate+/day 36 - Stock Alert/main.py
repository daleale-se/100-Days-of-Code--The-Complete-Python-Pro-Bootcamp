import requests
from datetime import *
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def get_news():
    NEWS_URL = "https://newsapi.org/v2/everything"
    NEWS_APIKEY = os.getenv("NEWS_APIKEY")
    news_parameters = {
        "q": COMPANY_NAME,
        "from": datetime.now().date() - timedelta(days=2),
        "apiKey": NEWS_APIKEY,
    }
    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    data = response.json()
    return [
        {
            "title": data["articles"][0]["title"],
            "description": data["articles"][0]["description"]
        },
        {
            "title": data["articles"][1]["title"],
            "description": data["articles"][1]["description"]
        },
        {
            "title": data["articles"][2]["title"],
            "description": data["articles"][2]["description"]
        }
    ]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_profit():
    ALPHA_URL = "https://www.alphavantage.co/query"
    FUNCTION = "TIME_SERIES_DAILY"
    ALPHA_APIKEY = os.getenv("ALPHA_APIKEY")

    alpha_parameters = {
        "function": FUNCTION,
        "symbol": STOCK,
        "apikey": ALPHA_APIKEY
    }

    response = requests.get(url=ALPHA_URL, params=alpha_parameters)
    response.raise_for_status()
    data = response.json()

    now = datetime.now()
    # except saturday and sunday
    while now.weekday() == 6 or now.weekday() == 5:
        now = now - timedelta(days=1)

    yesterday = now.date() - timedelta(days=1)
    day_before_yesterday = yesterday - timedelta(days=1)
    yesterday = str(yesterday)
    day_before_yesterday = str(day_before_yesterday)

    open_market = float(data["Time Series (Daily)"][yesterday]["1. open"])
    close_market = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
    profit = open_market - close_market
    return round(profit / open_market * 100, 2)


def send_message(title, description):
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_KEY = os.getenv("TWILIO_AUTH_KEY")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_KEY)
    message = client.messages.create(
        body=f"\n{title}\n\n{description}",
        from_='+12517662856',
        to='+541131821946')
    print(message.status)


percentage = 7.89 # get_stock_profit()
if percentage < -5 or 5 < percentage:
    news = get_news()
    for new in news:
        send_message(new["title"], new["description"])
else:
    print("The percentage was: ", percentage)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""