import requests

url = "https://brijeshguru.com/api/get_products.php"

product = {
    "name": "Keyboard",
    "photo": "https://brijeshguru.com/api/uploads/1785761869_samsung_guru.jpg",
    "old_price": 1250,
    "new_price": 1050,
    "description": "hi"
}

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(
    url,
    json=product,
    headers=headers,
    timeout=20
)

print("Status:", response.status_code)
print("Headers:", response.headers)
print("Response:", response.text)

if response.ok:
    print(response.json())
