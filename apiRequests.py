import requests
import json

api_url = "https://www.guitarguitar.co.uk/hackathon"

def request(endpoint, params):
    endpoint = endpoint or "/"
    params = params or {}

    return requests.get(api_url + endpoint, params)

