# api url : https://brijeshguru.com/api/get_products.php
"""
data	
id	:"8"
name :	"srug"
photo:	"https://brijeshguru.com/api/uploads/1785931640_srug.jpg"
old_price :	"499.00"
new_price :	"425.00"
description :	"good for mens and confortables"
created_at :	"2026-08-05 17:37:20"

"""
import requests

api_url = "https://brijeshguru.com/api/get_products.php"

headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/139.0.0.0 Safari/537.36"
    ),
    "Referer": "https://brijeshguru.com/",
    "Origin": "https://brijeshguru.com",
}

try:
    response = requests.get(
        api_url,
        headers=headers,
        timeout=20,
    )

    print("HTTP status:", response.status_code)
    print("Response:", response.text[:500])

    response.raise_for_status()

    result = response.json()

    # Your API returns {"status": true, "data": [...]}
    posts = result["data"]

    for data in posts[-5:]:
        print(data["name"])
        print(data["new_price"])
        print(data["description"])

except requests.HTTPError as error:
    print(f"HTTP error {error.response.status_code}: {error}")

except requests.RequestException as error:
    print(f"Request failed: {error}")

except ValueError:
    print("API returned invalid JSON.")
