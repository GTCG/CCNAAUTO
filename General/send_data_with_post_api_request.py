import requests

url="https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My new post",
    "body":"This is a post created with Python",
    "Userid": 1
}

response= requests.post(url, json=payload)

print(response.status_code)
print(response.json())