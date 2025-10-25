import requests
import json

api_url = "https://www.guitarguitar.co.uk/hackathon"

def request(endpoint):
    endpoint = endpoint or "/"

    return requests.get(api_url + endpoint)

