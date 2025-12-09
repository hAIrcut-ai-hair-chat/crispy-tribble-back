import requests

url = "http://localhost:8000/api/user/"

data = {
    "email": "teste@example.com",
    "name": "Kaua",
    "password": "123456"
}

r = requests.post(url, json=data)
print(r.status_code)
print(r.json())
