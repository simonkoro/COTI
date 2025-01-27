import time
from unittest import TestCase
from test_apis import TestingApis
import random

class CotiTest(TestCase):
    transaction_id = None
    amount = 0

    def setUp(self):
        self.BASE_URL = "http://127.0.0.1:5000"
        self.apis = TestingApis(self.BASE_URL)

    def test1_making_transaction(self):
        CotiTest.amount = random.randint(1, 99999999)
        response = self.apis.initiate_transaction(CotiTest.amount)
        print(f"TEST1: \ninitiate transaction API response code: {response}")
        print(f"initiate transaction API JSON response: {response.json()} \n")
        CotiTest.transaction_id = response.json()['transaction_id']

        self.assertIsNotNone(CotiTest.transaction_id)
        self.assertEqual(201, response.status_code)

    def test2_verify_transaction(self):
        response = self.apis.verify_transaction(CotiTest.transaction_id)
        print(f"TEST2: \nverify transaction API response: {response}")
        print(f"verify transaction API JSON response: {response.json()} \n")
        self.assertEqual(200, response.status_code)
        self.assertEqual(CotiTest.amount, response.json()['details']['amount'])


    def test3_monitor_transaction(self):
        print("TEST3:\n")
        while True:
            response = self.apis.monitor_transaction(CotiTest.transaction_id)
            api_data = response.json()
            status = api_data.get("status")
            print(api_data)
            print(f"Current Status: {status}")
            if status == "processed":
                print("transaction processed!")
                break
            time.sleep(1)