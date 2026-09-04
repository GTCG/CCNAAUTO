import requests

url="https://jsonplaceholder.typicode.com/posts/1"

response= requests.get(url)

if response.status_code == 200:
    data=response.json()
    print("request was succesful")
    print(f"post ID: {data['id']}")
    print(f"title: {data['title']}")
else:
    print (f"request failed with status code: {response.status_code}")
    