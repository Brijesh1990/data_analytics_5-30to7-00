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
    


   

