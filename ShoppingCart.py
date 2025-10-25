import json

import requests
def GetProducts():
    url = "https://www.guitarguitar.co.uk/products"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        

GetProducts()