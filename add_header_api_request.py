import requests

url="https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "accept": "application/json"
}

response= requests.get(url, headers=headers)

print(response.status_code)
print(response.json())


    