import apiRequests
import requests

endpoint = "/products"
data = ""


thisRequest = apiRequests.request(endpoint)

data = thisRequest.content
print(data)

"""
dictt = {
    "Name": 1,
    "ItemType": "Guitar",
    "Price": 1.99,
}cl



def NewItem():
    print("Hello")

"""