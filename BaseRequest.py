import requests

class BaseRequest:
    """Base class for making HTTP requests using the requests library."""

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None, headers=None):
        """Send a GET request."""
        response = self.session.get(url, params=params, headers=headers)
        return response

    def post(self, url, data=None, json=None, headers=None):
        """Send a POST request."""
        response = self.session.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, url, data=None, json=None, headers=None):
        """Send a PUT request."""
        response = self.session.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, url, headers=None):
        """Send a DELETE request."""
        response = self.session.delete(url, headers=headers)
        return response
