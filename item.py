import apiRequests

endpoint = "/products"

def NewItem(sku):
    item = dict()

    itemResponse = apiRequests.request(endpoint, {"SKU_ID": sku})
    

    if itemResponse.status_code != 200:
        print("Request Failed")
        return None
    itemJson = itemResponse.json()

    if len(itemJson) <= 0:
        print("Params return nothing")
        return None
    

    for i in itemJson:
        itemDict = i
        if itemDict["SKU_ID"] == sku:
            item["SKU ID"] = sku
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

thisItem = NewItem("190319340844008")
print(thisItem)






