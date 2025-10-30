import csv
import os

def mostrar_productos():
    if not os.path.exists("productos.csv"):
            print("Archivo no encontrado.")
            with open("productos.csv", "w", newline='') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["nombre", "precio"])
            print("Archivo creado.\n")

    with open("productos.csv", "r") as archivo:
        lector = csv.reader(archivo)
        next(lector)

        total = 0
        hay_productos = False

        print("--PRODUCTOS--")
        for fila in lector:
            if fila:
                total += float(fila[1])
                hay_productos = True
                print(f"{fila[0]}: ${fila[1]}")

        if hay_productos:
            print(f"Total de precios: ${total}\n")
        else:
             print("No hay productos registrados.\n")

def agregar_producto():
    try:
        nuevo_producto = input("Nombre del nuevo producto: ")
        precio_nuevo_producto = float(input("Precio del nuevo producto: "))
        print()

        if precio_nuevo_producto <= 0:
            print("El precio debe ser un número positivo.\n")
            return 

    except ValueError:
        print("Inválido - el precio debe ser un número entero o decimal.\n")
        return

    nueva_fila = [nuevo_producto, precio_nuevo_producto]

    with open("productos.csv", "a", newline='') as archivo:
        archivo.write("\n")
        escritor = csv.writer(archivo)
        escritor.writerow(nueva_fila)

    print("Producto agregado.\n")

def eliminar_producto():
    producto_eliminar = input("Ingrese el nombre del producto a eliminar: ")
    encontrado = False

    with open("productos.csv", "r") as archivo:
        lector = csv.reader(archivo)

        encabezado = next(lector)
        nueva_lista = [encabezado]

        for fila in lector:
            if fila and fila[0] != producto_eliminar:
                nueva_lista.append(fila)
            else:
                encontrado = True

    if encontrado:
        with open("productos.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(nueva_lista)
    
        print("Producto eliminado.\n")
    else:
        print("Producto no encontrado.\n")

while True:
    print("===MENÚ===")
    print("|1| Mostrar productos")
    print("|2| Agregar producto")
    print("|3| Eliminar producto")
    print("|4| Salir")

    opt = input("Opción: ")
    print()

    if opt == '1':
        mostrar_productos()
    elif opt == '2':
        agregar_producto()
    elif opt == '3':
        eliminar_producto()
    elif opt == '4':
        print("Saliendo...")
        break
    else:
        print("Opción inválida.")