import requests1

url="https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My new post",
    "body":"This is a post created with Python",
    "Userid": 1
}

response= requests1.post(url, json=payload)

print(response.status_code)
print(response.json())