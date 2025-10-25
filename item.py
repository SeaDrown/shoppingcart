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
    item = itemDict
    if itemDict["Category"] == "GUEG_1": #for guitars
        item["Name"] = itemDict["ItemName"]
        item["Price"] = itemDict["SalesPrice"]
        item["Category"] =  itemDict["Category"]
        item["Brand Name"] = itemDict["BrandName"]
        item["Rating"] = itemDict["Rating"]
        item["Quantity in stock"] = itemDict["QtyInStock"]
    return item

def PrintItem(item):
    print("SKU : "+ str(item["SKU"]))
    print("Category : "+ str(item["Category"]))
    print("Name : " + item["Name"])
    print("Brand Name : " + item["Brand Name"])
    print("Price : " + str(item["Price"]))
    print("Quantity in stock : " + item["Quantity in stock"])
    print("Rating : " + item["Rating"])

thisItem = NewItem(220302382185027)
print(thisItem)






