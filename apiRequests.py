import requests
import json

api_url = "https://www.guitarguitar.co.uk/hackathon"

def request(endpoint, param):
    endpoint = endpoint or "/"
    param = param or {}

    return requests.get(api_url + endpoint, params=param)

