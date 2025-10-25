import json

import apiRequests
def GetProducts():
        url = "https://www.guitarguitar.co.uk/hackathon"
        endpoint = "/products"
        response = apiRequests.requests(endpoint)
        products = response.json()

        if response.status_code == 200:
            firstitem = products[0]
            for key,value in firstitem.items():
                  print(key + ":" + str(value))

GetProducts()