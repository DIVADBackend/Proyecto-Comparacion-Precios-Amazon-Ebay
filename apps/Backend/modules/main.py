from ProductSearchEndpoint import buscarProducto
from ProductDetailsEndpoint import detallesProducto
from db_queries import buscarCategoryID, buscarSubcategoryID
from main_functions import verificarExcepcionCantidad, informacionDeMultiplesProductos

#Opciones del menú principal

mostrarComo = input('''
Mostrar información como:
1. Comparación de Precios Promedio  
2. Comparación de Múltiples Productos
3. Comparación de Opciones de Producto

opción: ''')

if mostrarComo == "Comparación de Precios Promedio" or mostrarComo == "Comparación de Opciones de Producto":

    query = input("Nombre del producto: ")

    category = input("Categoría: ")

    subcategory = input("Subcategoría: ")
    
else:
    while True:
        cantidadProductos = verificarExcepcionCantidad(input("Cantidad de productos a mostrar: "))
        
        if isinstance(cantidadProductos, int):
            break
        
    informacionProductos = informacionDeMultiplesProductos(cantidadProductos)
    

#Pidiendo las cantidades respectivas para cada opción de "Mostrar información como..."

if mostrarComo == "Comparación de Precios Promedio":
    
    while True:
        cantidadPromedio = verificarExcepcionCantidad(input("Cantidad de un mismo producto para el promedio: "))
        
        if isinstance(cantidadPromedio, int):
            break
        
elif mostrarComo == "Comparación de Opciones de Producto":
    while True:
        cantidadOpciones = verificarExcepcionCantidad(input("Cantidad de opciones del producto: "))
        
        if isinstance(cantidadOpciones, int):
            break

# if mostrarComo == "Comparación de Precios Promedio" or mostrarComo == "Comparación de Opciones de Producto":
# #buscando el ID del producto en la Base de Datos con el nombre de la categoría y la subcategoría respectivamente

#     category_id = buscarCategoryID(category)

#     subcategory_id = buscarSubcategoryID(subcategory)

# # #Buscando el producto en Amazon

#     responseSearching = buscarProducto(query, category_id)

#     json_response_search = responseSearching.json()

#     dataSearch = json_response_search
    
#     productos = dataSearch['data']['products']
    
#     print(productos)
    
#     for productoNumero in range(cantidadPromedio):
#         print(productos[productoNumero]['product_price'])

# #Obteniendo el ASIN del primer producto de búsqueda en Amazon

#     relevant_data = dataSearch['data']['products']

#     asin = relevant_data['asin']

# # #Obteniendo detalles del producto con su ASIN

#     responseDetails = detallesProducto(asin)

#     json_response_details = responseDetails.json()








