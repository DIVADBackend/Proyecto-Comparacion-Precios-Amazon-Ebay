import requests

def buscarProducto(query, category):

    url = "https://real-time-amazon-data.p.rapidapi.com/search"

    querystring = {"query": query ,"page":"1","country":"US","sort_by":"REVIEWS","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE", 'category': category}

    headers = {
        "x-rapidapi-key": "7eff510885msh1aebe1be7a09d6ap11dcdajsn1a6b5ac05529",
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    return response