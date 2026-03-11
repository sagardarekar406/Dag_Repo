import requests
from config.constants import CUSTOMER_API

def fetch_customer_data():
    response = requests.get(CUSTOMER_API)
    print(response.status_code)
