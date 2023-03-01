import requests
import json

query = input("What news you want to have ?  ")
url = f"https://newsapi.org/v2/top-headlines?country=us&category={query}&apiKey=bc87370a2dc64d6da21a396f00cc643c"

r = requests.get(url)
news = json.loads(r.text)
print(news)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------------")
