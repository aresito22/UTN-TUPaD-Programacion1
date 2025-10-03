titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares = [5, 3, 7]

while True:
    print()
    print("1 - Ingresar títulos")
    print("2 - Ingresar ejemplares")
    print("3 - Mostrar catálogo")
    print("4 - Consultar disponibilidad")
    print("5 - Listar agotados")
    print("6 - Agregar título")
    print("7 - Actualizar ejemplares (préstamo/devolución)")
    print("8 - Salir\n")

    opt = input("Opción: ")
    print()

    if opt == '1':
        titulos = []
        ejemplares = []

        while True:
            nuevo_titulo = input("Ingrese el nuevo título o ingrese 0 para salir: ")
            print()

            if nuevo_titulo == '':
                print("Inválido.\n")
            elif nuevo_titulo == '0':
                break
            else:
                titulos.append(nuevo_titulo)
                ejemplares.append(0)
    
    elif opt == '2':
        ejemplares = []
        for titulo in titulos:
            nuevo_ejemplar = int(input(f"Ingrese la cantidad de ejemplares para {titulo}: "))
            if nuevo_ejemplar < 0:
                print("Inválido - los ejemplares no pueden ser menores a 0.")
            else:
                ejemplares.append(nuevo_ejemplar)

    elif opt == '3':
        for i, titulo in enumerate(titulos):
            print(f"{titulo}: {ejemplares[i]} ejemplares")
        
    elif opt == '4':
        titulos_buscar = [titulo.lower() for titulo in titulos]


        titulo_encontrado = False
        titulo_encontrar = input("Escriba el título del libro a buscar: ")
        titulo_encontrar = titulo_encontrar.lower()
        print()

        if titulo_encontrar in titulos_buscar:
            for i, titulo in enumerate(titulos_buscar):
                if titulo_encontrar == titulo:
                    print(f"{titulos[i]}: {ejemplares[i]} copias\n")
                    titulo_encontrado = True
            
        if not titulo_encontrado:
            print("Título no encontrado en el catálogo.\n")

    elif opt == '5':
        print("Libros sin stock:\n")
        for i, titulo in enumerate(titulos):
            if ejemplares[i] == 0:
                print(f"{titulo}")

    elif opt == '6':
        titulo_anadir = input("Ingrese el título a sumar al catálogo: ")
        ejemplar_anadir = int(input("Ingrese la cantidad de ejemplares para el nuevo título: "))

        if titulo_anadir == '':
            print("Inválido - el título no puede estar vacío.")
        elif ejemplar_anadir < 0:
            print("Inválido - los ejemplares no pueden ser menores a 0.")
        elif titulo_anadir in titulos:
            print("Inválido - el título ya está en el catálogo.")
        else:
            titulos.append(titulo_anadir)
            ejemplares.append(ejemplar_anadir)
            print("Añadido.")

    elif opt == '7':
        for i, titulo in enumerate(titulos):
            print(f"{i+1} - {titulo}")

        print()
        titulo_actualizar = int(input("Ingrese el número de título a actualizar: "))
        titulo_actualizar = titulo_actualizar - 1
        modificacion = input("Ingrese 1 para actualizar un préstamo o 2 para actualizar una devolución: ")
        print()
            
        if modificacion == '1':
            if ejemplares[titulo_actualizar] > 0:
                ejemplares[titulo_actualizar] = ejemplares[titulo_actualizar] - 1
                print("Restado.")
            else:
                print("Inválido - no hay copias suficientes.")
        elif modificacion == '2':
            ejemplares[titulo_actualizar] = ejemplares[titulo_actualizar] + 1
            print("Añadido.")
        else:
            print("Opción inválida.")

    elif opt == '8':
        print("Saliendo.")
        break
    
    else:
        print("Opción inválida.")