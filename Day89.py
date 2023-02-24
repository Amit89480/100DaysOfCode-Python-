# import requests
#
# response = requests.get("https://www.google.com")
# print(response.text)


# Here we also saw a basics of web scrapping

from bs4 import BeautifulSoup
import requests

url = "https://www.google.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
