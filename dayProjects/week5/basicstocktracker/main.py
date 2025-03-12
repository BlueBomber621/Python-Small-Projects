import requests
import html
import smtplib
from email.mime.text import MIMEText

# Constants & Values
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_API_KEY = "Your Alpha API Key"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "Your NewsAPI API Key"

sender_user = "username@example.com"
recipiant_user = "username@example.com"
app_password = "Your sender's app password"

alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY
}

# Response & Data
response = requests.get(ALPHA_ENDPOINT, params=alpha_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
## Get values from response for yesterday (or the data's latest day) and the day before
yesterday_data = data_list[0]
yesterday_closing_value = yesterday_data['4. close']
yesterday_yesterday_data = data_list[1]
yesterday_yesterday_closing_value = yesterday_yesterday_data['4. close']
## Find the difference between the values and the percentage of the difference
value_difference = abs(round(float(yesterday_closing_value) - float(yesterday_yesterday_closing_value), 4))
difference_percent = round((value_difference / float(yesterday_closing_value)) * 100, 4)
## Find if the difference is over 5% of the latest day's value.
if difference_percent > 0.01:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()['articles'][:3]
    article_messages = [{"source": article['source']['name'], "content": article['title']} for article in articles]
    for message in article_messages:
        try:
            msg = MIMEText(message["content"])
            msg["Subject"] = f"News from {message["source"]}"
            msg["From"] = sender_user
            msg["To"] = recipiant_user

            # Connect to Gmail's SMTP server
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(sender_user, app_password)
            
            # Send the email
            server.sendmail(sender_user, recipiant_user, msg.as_string())
            server.quit()

            print("✅ Email sent successfully!")
        except Exception as e:
            print(f"❌ Error: {e}")
