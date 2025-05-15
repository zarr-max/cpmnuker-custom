import requests

class CPMNuker:
    def __init__(self, api_url="https://maldavo.squareweb.app/api"):
        self.api_url = api_url
        self.token = None

    def login(self, username, password):
        data = {"username": username, "password": password}
        r = requests.post(f"{self.api_url}/login", json=data)
        if r.status_code == 200 and "token" in r.json():
            self.token = r.json()["token"]
            return r.json()
        return r.json()

    def change_id(self, new_id):
        if not self.token:
            return {"error": "You must login first."}
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"new_id": new_id}
        r = requests.post(f"{self.api_url}/change_id", json=data, headers=headers)
        return r.json()

    def set_money(self, money):
        if not self.token:
            return {"error": "You must login first."}
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"money": money}
        r = requests.post(f"{self.api_url}/set_money", json=data, headers=headers)
        return r.json()

    def ban_account(self):
        if not self.token:
            return {"error": "You must login first."}
        headers = {"Authorization": f"Bearer {self.token}"}
        r = requests.post(f"{self.api_url}/ban", headers=headers)
        return r.json()
