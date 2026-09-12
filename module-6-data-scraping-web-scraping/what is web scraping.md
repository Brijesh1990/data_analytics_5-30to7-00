# what is web scraping ?

- web scraping is used to collecting data from website automatically using a programme(python) i.e called web scarping.

- web scraping is an process that is used to manually copying instead of data from any external resource  we did web scarping to automatically using a programmes to scrape a data.

- for examples how scraping is work (or collect data from any website)

1.  categoryname
2.  productname
3.  price
4.  qty
5.  employee information 
6.  weather information
7.  products details 
8.  rating details 


# simple workflow of web scarping

website
   |
send http request
   |
Recieve in HTMl(hypertext markup language) | Json(javascript object notation) | XML(xtensible markup language) 
   |
Parse HTML or json data
   |
find required element 
   |
Extract data 
   |
clean Data
   |
save CSV | Excel | json | database  
   
**note : web scraping we create any data scraping or web scraping to used python programming language**



# web scraping which libraries or packages are used of python 

|  package name(library)       |             descriptions                      |
|------------------------------|--------------------------------------         |
|requests                      | download webpage HTML                         |
|BeautifulSoup                 | parse and extract html data                   |
|lxml                          | Fast html/xml parsing                         |
|pandas                        | store and analize scarped data in data frames |
|selenium                      | scrape javascript-rendered websites           |
|Scrapy                        | Build large-scale web crawlers                |
|re                            | Extract data using regular expressions(re)    |
|openpyxl                      | save data inside of CSV or excel via python   | 


# every libraries install via pip 
# pip install requests beutifulsoup4 lxml pandas selenium Scrapy re openpyxl
# pip show pandas | openpyxl | selenium | lxml | beautifulsoup4 

# what is SOUP ?

You likely mean SOAP API (Simple Object Access Protocol), an XML-based protocol used for exchanging structured information across computer networks. It is highly structured, strictly regulated by rules, and widely used in enterprise, financial, and healthcare systems

# what is beutifulsoup4  ?

If you meant Beautiful Soup, that is a Python library used for parsing data out of HTML and XML files rather than a standard web API framework.


# create a simple webs scraping concepts in python ?

   
# create an projects of web-scraping-demo-app using my venv
   
   1. pip install virtualenv
   2. pip show virtualenv
   3. virtualenv web-scraping-demo-app
   4. cd web-scraping-demo-app
   5. Scripts\activate
   6. install all dependnecies of libraries
   7. deactivate


# install all libraries for web scraping 

  1.  after activate a virtualenv install all dpendencies of libraries 

  ```
   pip install requests beutifulsoup4 lxml pandas selenium Scrapy re openpyxl
   or 
   pip install requests beautifulsoup4
  ```  
    

# how to create examples for web scraping 


```

import requests
from bs4 import BeautifulSoup
# for scraping data website URL
url="https://www.tops-int.com/"
# get resposnse from server
response=requests.get(url) # sends a request to the website
# print the response
print(response.status_code) # tell us whether the request was successfull or not
# response status code 
# 200-> success 
# 403-> forbidden
# 500-> server error
# 404->page not found  
# 301->redirect
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title.text)

```

# how to get page title text for particular page

```
import requests
from bs4 import BeautifulSoup
# for scraping data website URL
url="https://www.tops-int.com/data-science-training-course"
# get resposnse from server
response=requests.get(url) # sends a request to the website
# print the response
print(response.status_code) # tell us whether the request was successfull or not
# response status code 
# 200-> success 
# 403-> forbidden
# 500-> server error
# 404->page not found  
# 301->redirect

soup=BeautifulSoup(response.text,"html.parser")
title=soup.title
# print(title)
print(title.text)

```
   
# scrape product list with title and price from any website and also import its data in csv | excel | json formate

```
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://www.raviflutes.com/products"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers, timeout=20)

print("Status Code:", response.status_code)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    # Find all h3 elements
    titles = soup.find_all("h3")

    print("Total H3 found:", len(titles))

    for title in titles:

        product_title = title.get_text(" ", strip=True)

        # Find nearest parent that contains price information
        parent = title

        for _ in range(5):

            if parent.parent:
                parent = parent.parent

            text = parent.get_text(" ", strip=True)

            if "₹" in text:
                break

        # Find prices from the product card
        price_matches = re.findall(
            r"₹\s*[\d,]+(?:\.\d+)?",
            text
        )

        # Remove duplicate prices
        price_matches = list(dict.fromkeys(price_matches))

        if price_matches:
            price = price_matches[-1]
        else:
            price = "N/A"

        data.append({
            "Title": product_title,
            "Price": price
        })

    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df.to_string(index=False))
    
    # csv formate scrape data
    # df.to_csv('products_list.csv', index=False)
    
    # save data in excel
    # df.to_excel("products_list_data.xlsx", index=False)
    
    # save data in json 
    
    df.to_json("products_list.json",orient="records",indent=4)

else:
    print("Unable to access website")

```
