"""Global parameters"""
WEBEX_TOKEN= "NTdjMGRiZTItYjU3My00YjdlLWE2YWEtM2FjNDJjMDNiODRlN2RlMTIyYTMtN2Vh_PE93_c8b056ff-2097-4f20-987c-5bdaeff74d03"
import json
import requests
rooms = "https://webexapis.com/v1/rooms/"
messages= "https://webexapis.com/v1/messages/"
webhook= "https://webexapis.com/v1/webhooks"
roomID = "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vN2QwZjUyMDAtYjExZC0xMWYxLWE1NGMtODFhZTU1NDc0MWQ3"
webhookurl= "https://webhook.site/07cfd0cf-da25-4d17-aa95-0874f5686176"




#payload = {"title":"testroom1"}
payload = {"text": "balls yeah man!",
           "roomId": roomID 
           }

#webhook_payload = {
  #"name": "My Test Webhook",
  #"targetUrl": webhookurl,
  #"resource": "messages",
  #"event": "created",
  #"filter": f"roomId={roomID}"
#}
headers = {
  "Authorization":f"Bearer {WEBEX_TOKEN}",
  "Accept": "application/json"
}

#response = requests.request("POST", webhook, headers=headers, json=webhook_payload)
response = requests.request("POST", messages, headers=headers, json=payload)

print(response.status_code)
print(response.text)
#print(json.dumps(response.json(), indent=2))