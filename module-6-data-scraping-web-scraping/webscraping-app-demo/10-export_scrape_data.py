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
    
    #csv formate scrape data
    #df.to_csv('products_list.csv', index=False)
    
    # save data in excel
    #df.to_excel("products_list_data_excel.xlsx", index=False)
    
    # save data in json 
    df.to_json("products_list_api_json.json",orient="records",indent=4)

else:
    print("Unable to access website")