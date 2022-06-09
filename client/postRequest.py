import http.client
import json

conn = http.client.HTTPSConnection("127.0.0.1", 8081)
payload = json.dumps({
  "ime": "branko",
  "prezime": "karlovcan",
  "username": "bkarlovcan17",
  "smer": "RM",
  "predmeti": [
    {
      "ime": "PrimenjeniDistribuiraniSistemi",
      "espb": "6"
    },
    {
      "ime": "DigitalnaObradaSignala",
      "espb": "6"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))