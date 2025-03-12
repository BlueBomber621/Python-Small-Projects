import requests
import os

class DealsSheet:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.auth = os.environ['SHEET_AUTH']
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": self.auth
        }

    def get_info(self):
        sheet_response = requests.get(self.endpoint, headers=self.headers)
        sheet_response.raise_for_status()
        sheet_data = sheet_response.json()
        return sheet_data
    
    def post_info(self, data):
        sheet_response = requests.post(self.endpoint, headers=self.headers, json=data)
        sheet_response.raise_for_status()
    
    def put_info(self, data, row):
        sheet_response = requests.put(self.endpoint + f"/{row}", headers=self.headers, json=data)
        sheet_response.raise_for_status()