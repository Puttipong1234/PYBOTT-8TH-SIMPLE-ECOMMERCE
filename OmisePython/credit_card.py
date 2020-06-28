import requests
from config import *

def create_token(name,number,expiration_month,expiration_year,OMISE_KEY_PUBLIC):
    data = {
    'card[name]': name,
    'card[number]': number,
    'card[expiration_month]': expiration_month,
    'card[expiration_year]': expiration_year
    }

    response = requests.post('https://vault.omise.co/tokens', data=data, auth=(OMISE_KEY_PUBLIC,''))
    
    return response.json()["id"]


def create_charge(description,amount,currency,token_id):

    data = {
    'description': description,
    'amount': amount,
    'currency': currency,
    'card': token_id
    }

    response = requests.post('https://api.omise.co/charges', data=data, auth=(OMISE_SECRET_KEY,''))
    
    return response.json()["status"]


if __name__ == '__main__':
    
    token = create_token( name = "PYBOTT-TH",
                         number="4111111111140011",
                         expiration_month="12",
                         expiration_year="23",
                         OMISE_KEY_PUBLIC=OMISE_PUBLIC_KEY)
    
    print(token)
    
    res = create_charge(description="PAY FOR PYBOTT",amount=100000,currency="thb",token_id=token)
    print(res)
    
    
