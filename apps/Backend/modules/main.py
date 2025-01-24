from ProductSearchEndpoint import buscarProducto
from ProductDetailsEndpoint import detallesProducto
from db_queries import buscarCategoryID


query = input("Nombre del producto: ")
category = input("Categoría: ")

category_id = buscarCategoryID(category)


#Buscando el producto en Amazon

responseSearching = buscarProducto(query, category_id)

json_response_search = responseSearching.json()

dataSearch = json_response_search

#Obteniendo el ASIN del primer producto de búsqueda en Amazon

relevant_data = dataSearch['data']['products'][0]

asin = relevant_data['asin']

#Obteniendo detalles del producto con su ASIN

responseDetails = detallesProducto(asin)

json_response_details = responseDetails.json()

print(json_response_details['data'])
print(category_id)







