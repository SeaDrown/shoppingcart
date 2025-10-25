import requests
import json

api_url = "https://www.guitarguitar.co.uk"

def request(endpoint):
    endpoint = endpoint or "/"
    
    return requests.get(api_url + endpoint)

