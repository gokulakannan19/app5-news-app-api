import os

import requests
from send_email import send_email
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
# Get yesterday date
yesterday = datetime.now().date() - timedelta(1)
date = yesterday.strftime("%Y-%d-%m")

# Api and url
api_key = os.environ["news_app_api_key"]
url = f"https://newsapi.org/v2/everything?q" \
       f"=tesla&from=2024-01-02&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
content = request.json()

# Email Subject and Message
message = f"""\
Subject: News api Email

Date: {datetime.now()}\n
"""
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    message += f"{article['title']}\n{article['description']}\n"

send_email(message.encode("utf-8"))
