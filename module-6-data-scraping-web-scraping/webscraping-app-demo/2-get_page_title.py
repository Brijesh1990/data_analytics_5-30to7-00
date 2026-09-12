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



