import requests
from datetime import datetime, timedelta
import json

# Define the base API endpoint
url = "https://pro-api.solscan.io/v2.0/token/price"

# Define your API token
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjcmVhdGVkQXQiOjE3Mzk5NjIzNTgzOTUsImVtYWlsIjoiYWhtLm1vbnRhc3NlckBob3RtYWlsLmNvbSIsImFjdGlvbiI6InRva2VuLWFwaSIsImFwaVZlcnNpb24iOiJ2MiIsImlhdCI6MTczOTk2MjM1OH0.lW7tBi2CLyNrWU88xco2g16a4MAwSzMwu1QgCJNrvko"



def check_data():
    try:
        # Set up headers with the API token
        headers = {
            "token": api_token
        }

        # Set up parameters
        params = {
            "address": "AxriehR6Xw3adzHopnvMn7GcpRFcD41ddpiTWMg6pump",
            "time[]": ["20250224", "20250226"]
        }

        # Make the GET request with parameters
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print("Success! Data received:")
            print(data)
            
            # Check data length and return boolean
            return len(data) != 3
        else:
            print(f"Error: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage
result = check_data()
print(f"Result: {result}")