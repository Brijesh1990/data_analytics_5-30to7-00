import requests
from bs4 import BeautifulSoup
# get url
url="https://www.meesho.com/"
# get resposnse 
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
}

response = requests.get(url, headers=headers, timeout=20)
# get response 
print(response.status_code)
# get the information or data scrape of meesho
soup=BeautifulSoup(response.text,"html.parser")
title=soup.title
# title tags information
print(soup.title)
# title text formate 
print(title.text)

