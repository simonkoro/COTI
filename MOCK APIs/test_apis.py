import requests
from datetime import datetime

class TestingApis:
    def __init__(self, base_url):
        self.BASE_URL = base_url

    def initiate_transaction(self, amount):
        endpoint = f"{self.BASE_URL}/initiate-transaction"
        data = {
            "amount": amount,
            "blockchain": "COTI",
            "time": datetime.now().isoformat()
        }
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        return response

    def verify_transaction(self, transaction_id):
        endpoint = f"{self.BASE_URL}/verify-transaction/{transaction_id}"
        response = requests.get(endpoint)
        response.raise_for_status()
        return response

    def monitor_transaction(self, transaction_id):
        endpoint = f"{self.BASE_URL}/transaction-status/{transaction_id}"
        response = requests.get(endpoint)
        response.raise_for_status()
        return response
