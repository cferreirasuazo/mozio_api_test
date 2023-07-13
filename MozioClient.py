from BaseRequest import BaseRequest
import requests
import time
class MozioClient(BaseRequest):
    """Custom request class with additional functionality."""
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key

    def search(self, url, data):
        headers = {'API-KEY': self.api_key}
        response = self.post(url, headers=headers,data=data)
        return response

    def poll_search(self,url):
        # Constants
        MAX_POLL_REQUESTS = 30
        SEARCH_TIMEOUT = 10  # Maximum time to poll in seconds
        POLL_INTERVAL = 1  # Polling interval in seconds

        # Perform the initial search request
        # search_url = f'{BASE_URL}/search/{search_id}'
        headers = {'API-KEY': self.api_key}
        response = self.get(url, headers=headers)
        data = response.json()

        # Poll for results
        poll_count = 0
        start_time = time.time()

        while data['more_coming'] and time.time() - start_time < SEARCH_TIMEOUT and poll_count < MAX_POLL_REQUESTS:
            # Wait for the specified interval before making the next poll request
            time.sleep(POLL_INTERVAL)

            # Make the poll request
            headers = {'API-KEY': self.api_key}
            response = self.get(url, headers=headers)
            data = response.json()

            # Process the poll response and handle the results
            # Replace this with your own logic to handle the results as they appear

            poll_count += 1

        # Handle the final results or any remaining data
        # Replace this with your own logic to handle the results
        
        # Check if the maximum poll count has been reached
        if poll_count == MAX_POLL_REQUESTS:
            print("Maximum poll count reached. Consider adjusting the SEARCH_TIMEOUT value.")
            return response
        
        # Check if the timeout has been reached
        if time.time() - start_time >= SEARCH_TIMEOUT:
            print("Timeout reached. Consider adjusting the SEARCH_TIMEOUT value.")
            return response

        return response

    def reservations(self, url,data):
        headers = {'API-KEY': self.api_key}
        response = self.post(url, headers=headers, data=data)
        return response

    def reservations_poll(self,url):
        headers = {'API-KEY': self.api_key}
        response = self.get(url, headers=headers)
        return response

    def cancel_reservation(self, url):
        headers = {'API-KEY': self.api_key}
        response = self.delete(url, headers=headers)
        return response

    def reservations_list(self, url):
        headers = {'API-KEY': self.api_key}
        response = self.get(url, headers=headers)
        return response
