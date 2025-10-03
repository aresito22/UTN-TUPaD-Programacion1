titulos = ["El Señor de los Anillos", "Orgullo y Prejuicio", "Matar un Ruiseñor"]
ejemplares = [5, 3, 7]

while True:
    print("")
    print("1 - Ingresar lista de títulos")
    print("2 - Ingresar lista de ejemplares disponibles")
    print("3 - Mostrar catálogo de libros en stock")
    print("4 - Consultar disponibilidad")
    print("5 - Listar agotados")
    print("6 - Agregar título")
    print("7 - Actualizar ejemplares")
    print("8 - Mostrar catálogo total")
    print("9 - Salir")
    print("")

    opt = int(input("Opción: "))
    print("")

    if opt == 1:
        titulos = []
        print("Ingresando nueva lista de títulos")
        print("Ingrese el título o ingrese 0 para salir")
        while True:
            nuevo_titulo = input("Título: ")
            if nuevo_titulo == 0:
                break
            else:
                titulos.append(nuevo_titulo)
                ejemplares.append(0)

    elif opt == 2:
        ejemplares = []
        print("Ingresando ejemplares disponibles")
        for libro in titulos:
            cantidad_ejemplares = int(input(f"{libro}: "))
            ejemplares.append(cantidad_ejemplares)

    elif opt == 3:
        print("Mostrando catálogo de libros en stock:")
        print("")

        for indice, libro in enumerate(titulos):
            if ejemplares[indice] >= 1:
                print(libro)

    elif opt == 4:
        titulos_buscar = [libro.lower() for libro in titulos]
        while True:
            libro_a_buscar = input("Ingrese el título del libro por el que quiere consultar o ingrese 0 para salir: ")
            print("")
            libro_a_buscar = libro_a_buscar.lower()

            if libro_a_buscar == "0":
                break

            for indice, libro in enumerate(titulos_buscar):
                if libro == libro_a_buscar:
                    print(f"{titulos[indice]} disponible con {ejemplares[indice]} copias")
                    print("")
                
            if libro_a_buscar not in titulos_buscar:
                print("No disponible.")
                print("")

    elif opt == 5:
        print("Mostrando agotados:")
        for indice, libro in enumerate(titulos):
            if ejemplares[indice] == 0:
                print(libro)

    elif opt == 6:
        print("Agregando títulos")
        print("")        
        while True:
            print("")
            titulo_a_ingresar = input("Ingrese el título a ingresar: ")
            copias_del_titulo = int(input("Ingrese la cantidad de copias a ingresar de ese título"))

            titulos.append(titulo_a_ingresar)
            ejemplares.append(copias_del_titulo)

            print("Añadido.")
            print("")
            
            sub_opt = int(input("Ingrese 0 para salir o cualquier otra tecla para añadir otro título: "))

            if sub_opt == 0:
                break
            else:
                pass

    elif opt == 7:
        while True:
            for indice, libro in enumerate(titulos):
                print(f"{indice + 1} - {libro}: {ejemplares[indice]} copias")

            print("")
            print("Ingrese 1 para actualizar un prestamo, 2 para una devolución, o 0 para salir:")
            cambio = int(input("Opción: "))
            print("")

            if cambio == 1:
                libro_a_actualizar = int(input("Ingrese el número de libro a actualizar: "))
                print("")

                ejemplares[libro_a_actualizar - 1] = ejemplares[libro_a_actualizar - 1] - 1
                print("")
                print(f"Actualizado: restada una copia de {titulos[libro_a_actualizar - 1]}")
                print("")

            elif cambio == 2:
                libro_a_actualizar = int(input("Ingrese el número de libro a actualizar: "))
                print("")

                ejemplares[libro_a_actualizar - 1] = ejemplares[libro_a_actualizar - 1] + 1
                print("")
                print(f"Actualizado: sumada una copia de {titulos[libro_a_actualizar - 1]}")
                print("")
            
            elif cambio == 0:
                break
    
    elif opt == 8:
        print("Mostrando catálogo total")
        print("")

        for indice, libro in enumerate(titulos):
            print(f"{libro}: {ejemplares[indice]} copias")
    
    elif opt == 9:
        print("Saliendo del programa.")
        break