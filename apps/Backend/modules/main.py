import ProductSearchEndpoint as PSE
import ProductDetailsEndpoint as PDE

query = input("Nombre del producto: ")
category = int(input("Categoría: "))


#Buscando el producto en Amazon

responseSearching = PSE.buscarProducto(query, category)

json_response_search = responseSearching.json()

dataSearch = json_response_search

#Obteniendo el ASIN del primer producto de búsqueda en Amazon

relevant_data = dataSearch['data']['products'][0]

asin = relevant_data['asin']

#Obteniendo detalles del producto con su ASIN

responseDetails = PDE.detallesProducto(asin)

json_response_details = responseDetails.json()

print(json_response_details['data']['product_price'])







