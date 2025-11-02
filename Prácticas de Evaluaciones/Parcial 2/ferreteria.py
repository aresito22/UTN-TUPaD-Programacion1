import csv

def cargar_herramienta():
    nueva_herramienta = input("Nombre: ")
    nueva_herramienta_stock = int(input("Stock: "))
    nueva_herramienta_precio = float(input("Precio: "))

    nueva_fila = {"nombre":nueva_herramienta, "stock":nueva_herramienta_stock, "precio":nueva_herramienta_precio}

    with open("inventario.csv", "a", newline='') as archivo:
        fieldnames = ["nombre","stock","precio"]
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)  
        archivo.write("\n")
        escritor.writerow(nueva_fila)

        print("\nHerramienta añadida.\n")

def mostrar_herramientas():
    with open("inventario.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        next(lector)
        for fila in lector:
            print(f"{fila[0]} | Stock: {fila[1]} unidades | Precio: ${fila[2]}")

def modificar_herramienta():
    herramienta_modificar = input("Nombre de la herramienta a modificar: ")
    encontrada = False

    nueva_lista = []

    with open("inventario.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[0] != herramienta_modificar:
                nueva_lista.append(fila)
            else:
                encontrada = True
                stock_modificar = input(f"Nuevo stock para {herramienta_modificar}: ")
                precio_modificar = input(f"Nuevo precio para {herramienta_modificar}: ")
                
                fila_modificada = [herramienta_modificar, stock_modificar, precio_modificar]
                nueva_lista.append(fila_modificada)

    if encontrada:
        with open("inventario.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(nueva_lista)

            print("\nHerramienta modificada.\n")
    else:
        print("\nHerramienta no encontrada.\n")

def eliminar_herramienta():
    herramienta_eliminar = input("Nombre de herramienta a eliminar: ")
    encontrada = False

    nueva_lista = []

    with open("inventario.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[0] != herramienta_eliminar:
                nueva_lista.append(fila)
            else:
                encontrada = True

    if encontrada:
        with open("inventario.csv", "w", newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(nueva_lista)

        print("\nHerramienta eliminada.\n")
    else:
        print("\nHerramienta no encontrada.\n")

def consultar_disponibilidad():
    herramienta_consultar = input("Nombre de herramienta a consultar: ")
    encontrada = False

    with open("inventario.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[0] == herramienta_consultar:
                encontrada = True
                print(f"\n{fila[0]} | Stock: {fila[1]} unidades | Precio: ${fila[2]}\n")

    if not encontrada:
        print("\nHerramienta no encontrada.\n")

def mostrar_sin_stock():
    hay_herramientas_sin_stock = False
    herramientas_sin_stock = []

    with open("inventario.csv", "r", newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila and fila[1] == '0':
                hay_herramientas_sin_stock = True
                herramientas_sin_stock.append(fila[0])

    if not hay_herramientas_sin_stock:
        print("\nTodas las herramientas están en stock.\n")
    else:
        print("\nHERRAMIENTAS SIN STOCK: ")
        for herramienta in herramientas_sin_stock:
            print(f"    {herramienta}")
        print()

while True:
    print("===MENÚ===")
    print("|1| Cargar herramienta")
    print("|2| Mostrar herramientas")
    print("|3| Modificar herramienta")
    print("|4| Eliminar herramienta")
    print("|5| Consultar disponibilidad de herramienta")
    print("|6| Mostrar herramientas sin stock")
    print("|7| Salir\n")

    opt = input("Opción: ")

    if opt == '1':
        cargar_herramienta()
    elif opt == '2':
        mostrar_herramientas()
    elif opt == '3':
        modificar_herramienta()
    elif opt == '4':
        eliminar_herramienta()
    elif opt == '5':
        consultar_disponibilidad()
    elif opt == '6':
        mostrar_sin_stock()
    elif opt == '7':
        print("\nSaliendo...")
        break
    else:
        print("\nOpción inválida.\n")