def verificarExcepcionCantidad(input):
    try:
        input = int(input)
    except:
        print("Debes ingresar un número")

    return input

def pedirCategoriasOSubcategorias(tipo, numero):
    valor = ""
    if tipo == "categoria":
        valor = input(f"Categoría número {numero + 1}: ")
    else:
        valor = input(f"Subcategoría número {numero + 1}: ")
    
    return valor


def informacionDeMultiplesProductos(cantidadProductos):
    nombresCategoriasYSubcategorias = {}
    
    for numero in range(cantidadProductos):
        productoNombre = input(f"Producto número {numero + 1}: ")
        categoria = pedirCategoriasOSubcategorias("categoria", numero)
        subcategoria = pedirCategoriasOSubcategorias("subcategoria", numero)
        nombresCategoriasYSubcategorias[productoNombre] = [categoria, subcategoria]
        
    return nombresCategoriasYSubcategorias
