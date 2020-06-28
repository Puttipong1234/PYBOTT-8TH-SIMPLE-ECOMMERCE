import requests
from config import *

def promptpay(amount,currency,source_type,OMISE_SECRET_KEY):
    data = {
    'amount': amount,
    'currency': currency,
    'source[type]': source_type
    }

    response = requests.post('https://api.omise.co/charges', data=data, auth=(OMISE_SECRET_KEY, ''))

    return response.json()["id"] , response.json()["source"]["scannable_code"]["image"]["download_uri"]