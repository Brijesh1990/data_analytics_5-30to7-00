import requests
from bs4 import BeautifulSoup
# get url for scrap data 
url="https://examples-app-eta.vercel.app"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")
# get text of urls 
headings=soup.find_all("p")
for heading_data in headings:
    print(heading_data.get_text(strip=True))
    # print(response.status_code)
    # print(response.text[:2000])
    
    


