import requests
from bs4 import BeautifulSoup

req = requests.get("https://twitter.com/i/status/1686395695182331904")
soup = BeautifulSoup(req.content, "html.parser")
# res= soup.title

print(soup.prettify())