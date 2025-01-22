import requests

url = "https://real-time-amazon-data.p.rapidapi.com/search"

query = input("")

querystring = {"query":"Phone","page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL","is_prime":"false","deals_and_discounts":"NONE"}