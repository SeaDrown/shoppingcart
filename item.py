import requests
import json

url = "https://www.guitarguitar.co.uk"

endpoint = "/products"

try:
    thisRequest = requests.get(url + endpoint)
    data = thisRequest.text()

    print(data)
except ValueError:
    print("Not json bro")


"""
dictt = {
    "Name": 1,
    "ItemType": "Guitar",
    "Price": 1.99,
}cl



def NewItem():
    print("Hello")

"""