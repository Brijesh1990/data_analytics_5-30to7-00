from selenium import webdriver
from bs4 import BeautifulSoup
import time

# # home page paragraph scrape
# url = "https://www.raviflutes.com/"

# about us page paragraph scrape
url = "https://www.raviflutes.com/about"

# get driver
driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)  # wait for JavaScript to load

soup = BeautifulSoup(driver.page_source, "html.parser")

for p in soup.find_all("p"):
    text = p.get_text(" ", strip=True)  
    # strip(True) removed some unwanted whitespace in paragraph
    if text:
        print(text)

driver.quit()
