import requests
url="https://postman-echo.com/get"
querystring= {"test":"123"}
headers= {}
response= requests.request("GET", url, headers=headers, params=querystring)
print(response.status_code)
print (response.text)

url="https://postman-echo.com/post"
payload= "hello devnet"
headers= {"content-type":"text/plain"}
response= requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)
print (response.text)