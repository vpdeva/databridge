
import requests

def fetch_api_data(url, params=None):
    """
    Fetch data from an API and return the JSON response.
    """
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
            