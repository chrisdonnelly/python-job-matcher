import requests
import logging

logger = logging.getLogger("HTTP Client")


def fetch_json_data(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            logger.error(f"Failed to fetch data.  Status Code: {response.status_code}")
            return None
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return None
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error occurred: {req_err}")
        return None
    except ValueError as json_err:
        logger.error(f"JSON decoding error: {json_err}")
        return None
