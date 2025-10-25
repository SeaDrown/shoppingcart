import apiRequests

endpoint = "/products"

def NewItem(sku):
    item = dict()

    item["SKU"] = sku
    itemResponse = apiRequests.request(endpoint, {"SKU_ID": sku})

    if itemResponse.status_code != 200:
        print("Request Failed")
        return None
    itemJson = itemResponse.json()
    itemDict = itemJson[0]
    
    item["Name"] = itemDict["ItemName"]
    item["Price"] = itemDict["SalesPrice"]

    return item

def PrintItem(item):
    print(item["Name"])
    print(item["Price"])
    print("SKU : "+ str(item["SKU"]))

thisItem = NewItem(190319340844008)
PrintItem(thisItem)