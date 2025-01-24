import requests

def detallesProducto(asin):
    
    url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

    querystring = {"asin":asin, "country": "US", "more_info_query": "category"}

    headers = {
    "x-rapidapi-key": "7eff510885msh1aebe1be7a09d6ap11dcdajsn1a6b5ac05529",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    return response



