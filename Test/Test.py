import json

import requests

class API_Tester():
    def __init__(self, ip, port):
        self.host = f"http://{ip}:{port}/"

    def call_me(self, data):
        endpoint = "call_me"
        url = self.host + endpoint

        headers = {"Content-type": "application/json"}

        payload = json.dumps(data)
        print(type(payload), payload)
        result = requests.post(url,  data=payload, headers=headers)
        print(json.loads(result.text))


api = API_Tester("127.0.0.1", 8000)

data = {
    "phone": "+79758889900",
    "name": "New Lead"
}
api.call_me(data)

data = {
    "phone": "+79658889911",
    "name": "Admin"
}
api.call_me(data)