# https://petstore.swagger.io/v2/
import requests

response = requests.post("https://petstore.swagger.io/v2/pet",json={
  "id": 788,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Yasmina",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.put("https://petstore.swagger.io/v2/pet",json={
  "id": 788,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Jasmina",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

response = requests.get(f'https://petstore.swagger.io/v2/pet/{788}')
print(response.text)