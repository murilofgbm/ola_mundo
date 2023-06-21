import requests

login = input()

req = requests.get("https://api.github.com/users/{login}")

if (req.status_code == 200):
    print("sucesso")
    user = req.json()
    print(user["name"])

else:
    print(req.status_code)
    print("deu ruim")

