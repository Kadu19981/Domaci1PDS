import requests
import json

url = "http://192.168.0.25:8081/users"

payload = json.dumps({
  "ime": "Dusan",
  "prezime": "Djurovic",
  "smer": "RI",
  "predmeti": [
    {
      "ime": "Operativni sistemi",
      "espb": "6"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
