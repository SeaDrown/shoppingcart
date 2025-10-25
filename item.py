import apiRequests

endpoint = "/products"
data = ""

#try:
thisRequest = apiRequests.request(endpoint)

data = thisRequest.json()
firstItem = data[0]

for k, v in firstItem.items():
    print(k +" : " + str(v))
    
print(type(data))
#except Exception:
print("Failed")