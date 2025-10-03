clases = ["Yoga", "Funcional", "Zumba"]
cupos = [10, 15, 20]

while True:
    print()
    print("1 - Ingresar lista de clases")
    print("2 - Ingresar cupos por clase")
    print("3 - Listar clases")
    print("4 - Consultar cupos de una clase")
    print("5 - Mostrar clases sin cupos")
    print("6 - Agregar clase")
    print("7 - Inscribir o dar de baja a un alumno")
    print("8 - Salir\n")

    opt = input("Opción: ")
    print()

    if opt == '1':
        clases = []
        cupos = []
        while True:
            clase = input("Ingrese la clase o ingrese 0 para salir: ")
            print()
            if clase == '0':
                break
            elif clase == "":
                print("Inválido.")
                print()
            elif clase in clases:
                print("La clase ya existe.")
                print()
            else:
                clases.append(clase)
                cupos.append(0)
                print("Añadida.")
                print()

    elif opt == '2':
        cupos = []
        for i, clase in enumerate(clases):
            cupo = int(input(f"Cupos para {clase}: "))
            cupos.append(cupo)

    elif opt == '3':
        for i, clase in enumerate(clases):
            print(f"{clase}: {cupos[i]} cupos\n")

    elif opt == '4':
        clases_buscar = [clase.lower() for clase in clases]

        clase_consultada = input("Ingrese la clase a consultar: ")
        clase_consultada = clase_consultada.lower()
        print()

        clase_encontrada = False
        for i, clase in enumerate(clases_buscar):
            if clase == clase_consultada:
                clase_encontrada = True
                cupos_para_clase = cupos[i]
                break

        if clase_encontrada:
            print(f"La clase tiene {cupos_para_clase} cupos\n")
        else:
            print("No se encontró la clase.\n")

    elif opt == '5':
        for i, clase in enumerate(clases):
            if cupos[i] == 0:
                print(f"{clase}: sin cupos.")

    elif opt == '6':
        clase_agregar = input("Ingrese la clase a agregar: ")
        cupos_agregar = int(input("Ingrese la cantidad de cupos: "))
        clases.append(clase_agregar)
        cupos.append(cupos_agregar)

    elif opt == '7':
        for i, clase in enumerate(clases):
            print(f"{i} - {clase}")
        print()

        clase_modificar = int(input("Ingrese el número de clase a modificar: "))
        accion = int(input("Quiére inscribir o dar de baja a un alumno? 1/2: "))
        print()

        if accion == 1:
            if cupos[clase_modificar] > 0:
                cupos[clase_modificar] = cupos[clase_modificar] - 1
            else:
                print("Sin cupos")
        elif accion == 2:
            cupos[clase_modificar] += 1
        else:
            print("Opción inválida.")
        
    elif opt == '8':
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida.")                    