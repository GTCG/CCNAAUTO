import requests1

url="https://jsonplaceholder.typicode.com/posts/1"

try:
    response=requests1.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)


except requests1.exceptions.HTTPError as http_err:
    print(f"http error occured: {http_err}")

except requests1.exceptions.ConnectionError:
    print(f"connection error. Check network connectivity.")

except requests1.exceptions.Timeout:
    print(f"request timed out.")

except requests1.exceptions.RequestException as err:
    print(f"an error occured:{err}")
    