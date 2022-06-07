import requests
import json

url = "http://localhost:8081/"

payload = json.dumps({
  "ime": "aca",
  "prezime": "acic",
  "smer": "RI",
  "predmeti": [
    {
      "ime": "predmet1",
      "espb": "5"
    },
    {
      "ime": "predmet2",
      "espb": "8"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
