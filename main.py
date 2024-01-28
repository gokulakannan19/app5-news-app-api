import requests
from send_email import send_email
from datetime import datetime

api_key = "7ab04be9c08a40c398cb38465379f129"
url = f"https://newsapi.org/v2/everything?q" \
       f"=tesla&from=2023-12-15&sortBy=publishedAt&apiKey={api_key}"

request = requests.get(url)
print(request)

content = request.json()
print(content)

message = f"""\
Subject: News api Email

Date: {datetime.now()}\n
"""
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
    message += f"{article['title']}\n{article['description']}\n"

send_email(message.encode("utf-8"))
