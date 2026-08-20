 # What Is a REST API and How Is It Used in Python?

## What Is an API?

API means **Application Programming Interface**. An API is a set of rules that allows one application to communicate with another application.

For example, a Python program can request product data from a web server. The server processes the request and sends a response, usually in JSON format.

```text
Python application -> HTTP request -> REST API -> HTTP response -> Python application
```

## What Is REST?

REST means **Representational State Transfer**. REST is an architectural style for designing web APIs that use HTTP.

A REST API usually:

- Uses URLs to identify resources.
- Uses HTTP methods to perform operations.
- Sends data in JSON format.
- Uses HTTP status codes to describe the result.
- Is stateless, meaning each request contains the information needed to process it.

## Resources and Endpoints

A resource is data managed by an API. Examples include products, users, orders, and posts.

An endpoint is a URL used to access a resource:

```text
https://example.com/api/products
https://example.com/api/products/8
```

The product API used in this project is:

```text
https://brijeshguru.com/api/get_products.php
```

## HTTP Methods and CRUD

CRUD means Create, Read, Update, and Delete.

| HTTP method | Purpose | CRUD operation |
| --- | --- | --- |
| GET | Read data | Read |
| POST | Create data | Create |
| PUT | Replace a resource | Update |
| PATCH | Update part of a resource | Update |
| DELETE | Delete data | Delete |

Typical REST endpoints are:

```text
GET     /products       Get all products
POST    /products       Create a product
GET     /products/8     Get product 8
PUT     /products/8     Replace product 8
PATCH   /products/8     Update part of product 8
DELETE  /products/8     Delete product 8
```

## Installing the Python Library

The `requests` library is commonly used to call REST APIs from Python:

```bash
pip install requests
```

Import it in a Python file:

```python
import requests
```

## Sending a GET Request

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url, timeout=20)

print(response.status_code)
print(response.text)
```

`response.status_code` contains the HTTP status code and `response.text` contains the response as text.

## Reading JSON Data

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url, timeout=20)
response.raise_for_status()

posts = response.json()

for post in posts[:5]:
	print(post["id"])
	print(post["title"])
```

`response.json()` converts JSON into Python lists and dictionaries.

JSON:

```json
{
  "id": 8,
  "name": "Keyboard",
  "price": 150
}
```

Equivalent Python dictionary:

```python
{
	"id": 8,
	"name": "Keyboard",
	"price": 150
}
```

## Query Parameters

Query parameters filter or customize a request. For example:

```text
/products?category=mobile&page=2
```

In Python:

```python
import requests

url = "https://example.com/api/products"
parameters = {"category": "mobile", "page": 2}

response = requests.get(url, params=parameters, timeout=20)
response.raise_for_status()

print(response.url)
print(response.json())
```

## Request Headers

Headers send extra information to the server:

```python
import requests

headers = {
	"Accept": "application/json",
	"User-Agent": "MyPythonApp/1.0"
}

response = requests.get(
	"https://example.com/api/products",
	headers=headers,
	timeout=20
)
response.raise_for_status()
```

Common headers include:

- `Accept`: response format expected by the client.
- `Content-Type`: format of data being sent.
- `Authorization`: login token or API key.
- `User-Agent`: information about the client application.

## POST Request

Use `POST` to create a resource:

```python
import requests

url = "https://example.com/api/products"
product = {"name": "Keyboard", "price": 150}

response = requests.post(url, json=product, timeout=20)
response.raise_for_status()

print(response.status_code)
print(response.json())
```

The `json=` argument converts the Python dictionary to JSON.

## PUT, PATCH, and DELETE Requests

```python
import requests

url = "https://example.com/api/products/8"

requests.put(url, json={"name": "New Keyboard", "price": 175}, timeout=20)
requests.patch(url, json={"price": 180}, timeout=20)
requests.delete(url, timeout=20)
```

Use `PUT` to replace the complete resource and `PATCH` to update selected fields.

## HTTP Status Codes

| Code | Meaning |
| --- | --- |
| 200 | Request succeeded |
| 201 | Resource was created |
| 204 | Succeeded with no response body |
| 400 | Bad request |
| 401 | Authentication required or failed |
| 403 | Access forbidden |
| 404 | Resource not found |
| 405 | HTTP method is not allowed |
| 429 | Too many requests |
| 500 | Server error |
| 503 | Service unavailable |
| 504 | Gateway timeout |

`response.raise_for_status()` raises an exception for HTTP 4xx and 5xx responses.

HTTP `444` is a non-standard status commonly generated by Nginx or LiteSpeed security rules. It usually means the server or firewall rejected the request without returning a normal response body. This must normally be fixed in the hosting, firewall, WAF, or server configuration rather than in Python.

## Error Handling

```python
import requests

url = "https://example.com/api/products"

try:
	response = requests.get(url, timeout=20)
	response.raise_for_status()
	products = response.json()

except requests.Timeout:
	print("The API took too long to respond.")
except requests.ConnectionError:
	print("Could not connect to the API.")
except requests.HTTPError as error:
	print(f"HTTP error: {error}")
except ValueError:
	print("The API returned invalid JSON.")
else:
	for product in products:
		print(product)
```

Always use a timeout. Without one, a program can wait indefinitely.

## Authentication

Many APIs require an API key or bearer token:

```python
import os
import requests

api_key = os.getenv("API_KEY")
headers = {
	"Authorization": f"Bearer {api_key}",
	"Accept": "application/json"
}

response = requests.get(
	"https://example.com/api/products",
	headers=headers,
	timeout=20
)
response.raise_for_status()
print(response.json())
```

Do not publish real API keys in source code. Store them in environment variables or a secret manager.

## Complete Product API Example

```python
import requests

api_url = "https://example.com/api/products"

try:
	response = requests.get(
		api_url,
		headers={
			"Accept": "application/json",
			"User-Agent": "ProductClient/1.0"
		},
		timeout=20
	)
	response.raise_for_status()
	products = response.json()

	for product in products[-5:]:
		print(product.get("name"))

except requests.RequestException as error:
	print(f"API request failed: {error}")
except ValueError:
	print("The API returned invalid JSON.")
```

List slicing examples:

```python
products[:5]    # first five products
products[-5:]   # last five products
products[5:]    # products from index 5 onward
```

`products[5:0]` normally returns an empty list because the start index is after the stop index.

## Creating a REST API with Flask

Install Flask:

```bash
pip install flask
```

Example server:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
	{"id": 1, "name": "Keyboard", "price": 150},
	{"id": 2, "name": "Mouse", "price": 75}
]

@app.get("/products")
def get_products():
	return jsonify(products)

@app.post("/products")
def create_product():
	new_product = request.get_json()
	new_product["id"] = len(products) + 1
	products.append(new_product)
	return jsonify(new_product), 201

@app.get("/products/<int:product_id>")
def get_product(product_id):
	for product in products:
		if product["id"] == product_id:
			return jsonify(product)
	return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
	app.run(debug=True)
```

Run it with:

```bash
python app.py
```

Call it from Python:

```python
import requests

response = requests.get("http://127.0.0.1:5000/products", timeout=20)
response.raise_for_status()
print(response.json())
```

## REST API Request Flow

```text
1. Python builds a URL, method, headers, parameters, and body.
2. Python sends the HTTP request.
3. The server authenticates and validates the request.
4. The server performs the requested operation.
5. The server returns a status code and usually JSON.
6. Python checks the status and parses the response.
7. The application uses the resulting Python data.
```

In summary, using a REST API in Python means sending an HTTP request, checking the response status, converting JSON into Python data, and handling errors appropriately.
