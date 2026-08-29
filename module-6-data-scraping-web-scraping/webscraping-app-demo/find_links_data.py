import requests
from bs4 import BeautifulSoup
html="""

<a href="https://www.brijeshguru.com">Brijesh guru</a>
<a href="https://www.tops-int.com">Tops technologies pvt ltd</a>
<a href="https://www.raviflutes.com">ravi flutes</a>

"""

soup=BeautifulSoup(html, "html.parser")
links=soup.find_all("a")

# iterate via loop
for link in links:
    print(link.text)
    print(link.get("href"))

