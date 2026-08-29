import requests
from bs4 import BeautifulSoup
html="""

<h1>Python data are scrapped of heading</h1>

<h2>Python is a language</h2>

<h3>Python requests are used to scrape data</h3>

<h4>Python is best for data analytics</h4>

<h5>Python provdes many modules and library</h5> 

<h6>Python is interprete based language</h6>

"""

soup=BeautifulSoup(html, "html.parser")
print(soup.h1.text)

# iterate via loop
for heading in soup.find_all(["h2","h3","h4","h5","h6"]):
    print(heading.text)

