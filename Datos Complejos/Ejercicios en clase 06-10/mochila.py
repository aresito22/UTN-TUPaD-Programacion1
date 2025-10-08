try:
    print()
    tamano_mochila = int(input("Ingrese el tamaño de la mochila: "))
except ValueError:
    print()
    print("El tamaño debe ser un número entero.\n")
else:
    mochila = ["---vacío---" for i in range(tamano_mochila)]

while True:
    print()
    print("1 - Guardar objeto")
    print("2 - Ver mochila")
    print("3 - Salir\n")

    opt = input("Opción: ")
    print()

    if opt == '1':
        try:
            posicion = int(input(f"Posición de mochila para nuevo objeto (0-{tamano_mochila-1}): "))
        except ValueError:
            print()
            print("La posición debe ser un número entero.")
        else:
            try:
                objeto = input("Objeto: ")
                mochila[posicion] = objeto
            except IndexError:
                print()
                print("Indice inválido.")
            else:
                print()
                print("Objeto añadido.")

    elif opt == '2':
        for i, objeto in enumerate(mochila):
            print(f"Posición {i}: {objeto}")

    elif opt == '3':
        print("Saliendo...")
        break

    else:
        print("Opción inválida.\n")