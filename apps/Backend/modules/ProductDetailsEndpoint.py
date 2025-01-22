import requests

url = "https://real-time-amazon-data.p.rapidapi.com/product-details"

querystring = {"asin":"B0DK2BDVDP", "country": "US"}

headers = {
    "x-rapidapi-key": "7eff510885msh1aebe1be7a09d6ap11dcdajsn1a6b5ac05529",
	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
}


response = requests.get(url, headers=headers, params=querystring)

json_response = response.json()

data = json_response['data']

for category in data:
    if category == "category_path":
        print(data[category])
