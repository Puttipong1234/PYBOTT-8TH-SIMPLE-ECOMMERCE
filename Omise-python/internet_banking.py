import requests
from config import *

#create source & charge
def net_banking_create_source_and_charge(amount,currency,return_uri,_type,OMISE_SECRET_KEY):
    data = {
    'amount': amount,
    'currency': currency,
    'return_uri': return_uri,
    'source[type]': _type
    }

    response = requests.post('https://api.omise.co/charges', data=data, auth=(OMISE_SECRET_KEY, ''))
    
    # charge id and auth uri    send auth uri to user
    return response.json()["id"] , response.json()["authorize_uri"]

if __name__ == '__main__':
    res = net_banking_create_source_and_charge(amount=45000,currency="thb",return_uri="https://www.facebook.com/Pybott/",_type="internet_banking_bbl",OMISE_SECRET_KEY=OMISE_SECRET_KEY)
    
    print(res)
    #update to firebase user