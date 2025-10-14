def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea_buscar = linea.strip()
            linea_buscar = linea_buscar.split(',')
            print(f"Producto: {linea_buscar[0]} | Precio: {linea_buscar[1]} | Cantidad: {linea_buscar[2]}")

def anadir_productos():
    while True:
        try:
            nuevo_producto = input("Nombre del producto: ")
            nuevo_precio = float(input("Precio: "))
            nueva_cantidad = int(input("Cantidad: "))
        except ValueError:
            print()
            print("Valor(es) inválido(s): El precio debe ser un número entero o decimal y la cantidad debe ser un número entero.")
        else:
            break

    nueva_fila = f"{nuevo_producto},{nuevo_precio},{nueva_cantidad}"

    with open("productos.txt", "a") as archivo:
        archivo.write("\n")
        archivo.write(nueva_fila)
        print()
        print("Producto añadido con éxito.")

def crear_diccionario():
    diccionarios_productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            nueva_linea = linea.strip()
            nueva_linea = nueva_linea.split(',')

            diccionario = dict()
            diccionario["Producto"] = nueva_linea[0]
            diccionario["Precio"] = nueva_linea[1]
            diccionario["Cantidad"] = nueva_linea[2]

            diccionarios_productos.append(diccionario)
    print("Diccionario creado con éxito.")
    return diccionarios_productos

def mostrar_diccionarios(diccionarios):
    for diccionario in diccionarios:
        print(diccionario)

def buscar_producto():
    with open("productos.txt", "r") as archivo:
        producto_buscar = input("Ingrese el nombre del producto a buscar: ")
        print()

        encontrado = False

        for linea in archivo:
            linea_buscar = linea.strip()
            linea_buscar = linea_buscar.split(',')

            if linea_buscar[0] == producto_buscar:
                print(f"Producto: {linea_buscar[0]} | Precio: {linea_buscar[1]} | Cantidad: {linea_buscar[2]}")
                encontrado = True
                break

            if encontrado == False:
                print("Producto no encontrado.")

def guardar_en_archivo():
    diccionarios = crear_diccionario()

    with open("productos.txt", "w") as archivo:
        for diccionario in diccionarios:
            linea = f"{diccionario['Producto']},{diccionario['Precio']},{diccionario['Cantidad']}\n"
            archivo.write(linea)

    print("Guardado.")

while True:
    print("|1| Mostrar productos")
    print("|2| Añadir productos")
    print("|3| Crear diccionario de productos")
    print("|4| Buscar producto")
    print("|5| Guardar cambios")
    print("|6| Salir\n")

    opt = input("Opción: ")
    print()

    if opt == '1':
        mostrar_productos()
        print()
    elif opt == '2':
        anadir_productos()
        print()
    elif opt == '3':
        mostrar_diccionarios(crear_diccionario())
        print()
    elif opt == '4':
        buscar_producto()
        print()
    elif opt == '5':
        guardar_en_archivo()
    elif opt == '6':
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")