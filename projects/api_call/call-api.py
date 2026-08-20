# fetch api data 
# fetch data from https://jsonplaceholder.typicode.com/posts
# fetch api data in python using request module 
# json stands for javascript object notation

import requests
response=requests.get("https://jsonplaceholder.typicode.com/posts")
response.raise_for_status()
# status display via its code 404 not found | 200 success
posts=response.json() 

# api will iterate here 
for post in posts[-5:]:
    # print(post["title"], end="\n \n")
    # print(post["body"], end="\n \n")
    print(post["userId"], end="\n \n")
    print(post["title"], end="\n \n")
    print(post["body"], end="\n \n")