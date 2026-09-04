import requests

url="https://jsonplaceholder.typicode.com/posts/1"

try:
    response=requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)


except requests.exceptions.HTTPError as http_err:
    print(f"http error occured: {http_err}")

except requests.exceptions.ConnectionError:
    print(f"connection error. Check network connectivity.")

except requests.exceptions.Timeout:
    print(f"request timed out.")

except requests.exceptions.RequestException as err:
    print(f"an error occured:{err}")
    