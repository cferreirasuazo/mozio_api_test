import unittest
import requests
from MozioClient import MozioClient
from api_helpers import search_url

class TestMozioClient(unittest.TestCase):
    def get_result_id(self,result):
        return result.get("result_id")

    def setUp(self):
        self.data = {
            "start_address": "44 Tehama Street, San Francisco, CA, USA",
            "end_address": "SFO",
            "mode": "one_way",
            "pickup_datetime": "2023-12-01 15:30",
            "num_passengers": 2,
            "currency": "USD",
            "campaign": "Cristhian Ferreira"
        }

        self.reservation_data = {
            "email": "cristhian@mail.com",
            "country_code_name": "US",
            "phone_number": "8776665541",
            "first_name": "Happy",
            "last_name": "Traveler",
            "airline": "AA",
            "flight_number": "123",
            "customer_special_instructions": "My doorbell is broken, please yell"
        }

        self.client = MozioClient("6bd1e15ab9e94bb190074b4209e6b6f9")
    def search(self):
        response = self.client.search(search_url, self.data)
        self.assertEqual(response.status_code, 201)

    def search_poll(self):
        search_response = self.client.search(search_url, self.data)
        search_data = search_response.json()
        search_id = search_data.get("search_id")
        url = f"https://api-testing.mozio.com/v2/search/{search_id}/poll/"
        poll_search_response = self.client.poll_search(url)
        print(poll_search_response.json()["results"])
        self.assertEqual(poll_search_response.status_code, 200)
    
    def test_integration(self):
        search_response = self.client.search(search_url, self.data)
        search_data = search_response.json()
        search_id = search_data.get("search_id")
        poll_search_url = f"https://api-testing.mozio.com/v2/search/{search_id}/poll/"
        poll_search_response = self.client.poll_search(poll_search_url)

        self.assertEqual(poll_search_response.status_code, 200)

        results = poll_search_response.json()["results"]
        result_ids = list(map(self.get_result_id, results))
        create_reservations_url = "https://api-testing.mozio.com/v2/reservations/"
        
        self.reservation_data["search_id"] = search_id
        self.reservation_data["result_id"] = "f4033c2f7cd3b656dcbb322bbf169013"
        print(self.reservation_data)
        reservation_response = self.client.reservations(create_reservations_url,self.reservation_data)
        self.assertEqual(reservation_response.status_code, 201)

        reservations_poll_url = f"https://api-testing.mozio.com/v2/reservations/{search_id}/poll/"

        reservations_poll_response = self.client.reservations_poll(reservations_poll_url)
        self.assertEqual(reservations_poll_response.status_code, 202)

        reservation_id = reservations_poll_response.json()[0].get("id")

        cancel_reservation_url = f"https://api-testing.mozio.com/v2/reservations//v2/reservations/{reservation_id}/"

        cancel_reservation_response = self.client.cancel_reservation(url=cancel_reservation_url)
        self.assertEqual(cancel_reservation_response.status_code, 202)






        


