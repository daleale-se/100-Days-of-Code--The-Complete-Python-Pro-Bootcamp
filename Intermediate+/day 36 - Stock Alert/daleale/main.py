import requests
from datetime import *
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news():

    COMPANY_NAME = "Tesla Inc"
    NEWS_URL = "https://newsapi.org/v2/everything"
    NEWS_APIKEY = os.getenv("NEWS_APIKEY")
    news_parameters = {
        "q": COMPANY_NAME,
        "from": datetime.now().date() - timedelta(days=2),
        "apiKey": NEWS_APIKEY,
    }
    response = requests.get(url=NEWS_URL, params=news_parameters)
    response.raise_for_status()
    data = response.json()["articles"]
    return data[:3]


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_stock_profit():

    STOCK = "TSLA"
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
    data = response.json()["Time Series (Daily)"]

    # except saturday and sunday
    now = datetime.now()
    while now.weekday() in [6, 0, 1]:
        now = now - timedelta(days=1)

    yesterday = now.date() - timedelta(days=1)
    day_before_yesterday = yesterday - timedelta(days=1)

    close_yesterday_market = float(data[str(yesterday)]["4. close"])
    close_before_yesterday_market = float(data[str(day_before_yesterday)]["4. close"])
    return abs(round((close_yesterday_market - close_before_yesterday_market) / close_yesterday_market * 100, 2))

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


def send_message(article):

    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_KEY = os.getenv("TWILIO_AUTH_KEY")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_KEY)
    message = client.messages.create(
        body=article,
        from_='+12517662856',
        to='+541131821946')
    print(message.status)


def main():
    percentage = get_stock_profit()
    if 5 < percentage:
        news_articles = [f"{new['title']}\n\n{new['description']}" for new in get_news()]
        for article in news_articles:
            send_message(article)
    else:
        print("The percentage was: ", percentage)


main()
