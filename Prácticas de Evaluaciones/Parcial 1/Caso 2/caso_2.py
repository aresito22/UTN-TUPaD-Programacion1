#especialidades = ["Cardiología", "Dermatología", "Pediatría"]
especialidades = ["cardio", "dermato", "pedia"]
cupos = [5, 3, 10]

while True:
    print()
    print("1 - Ingresar lista de especialidades")
    print("2 - Ingresar lista de cupos por especialidad")
    print("3 - Mostrar agenda")
    print("4 - Consultar cupos de una especialidad")
    print("10 - Salir\n")

    opt = int(input("Opción: "))
    print()

    if opt == 1:
        especialidades = []

        print("Ingresando nueva lista de especialidades - Ingrese 0 para salir.\n")

        while True:
            especialidad = input("Especialidad: ")

            if especialidad == "0":
                break
            elif especialidad == "":
                print("Inválido.")
            elif especialidad in especialidades:
                print("La especialidad ya existe.\n")
            elif opt == 0:
                break
            else:
                especialidades.append(especialidad)
                print("Añadido\n")

    elif opt == 2:
        cupos = []

        print("Ingresando disponibilidad de cupos por especialidad.\n")

        for i, especialidad in enumerate(especialidades):
            while True:
                cupo = int(input(f"Cupos de {especialidad}: "))

                if cupo < 0:
                    print("Opción inválida, no puede ser un número menor a 0.\n")
                elif type(cupo) != int:
                    print("Opción inválida, debe ingresar un número entero.\n")
                else:
                    cupos.append(cupo)
                    print("Añadido\n")
                    break

    elif opt == 3:
        print("Agenda:")

        for i, especialidad in enumerate(especialidades):
            print(f"{especialidad}: {cupos[i]} cupos.")

    elif opt == 4:
        especialidades_buscar = [especialidad.lower() for especialidad in especialidades]

        while True:
            especialidad_consultar = input("Especialidad a consultar: ")
            especialidad_consultar = especialidad_consultar.lower()

            if especialidad_consultar in especialidades_buscar:
                for i in range(len(especialidades_buscar)):
                    if especialidad_consultar == especialidades_buscar[i]:
                        print(f"{especialidad[i]}: {cupos[i]} cupos.")

    elif opt == 10:
        break

    else:
        print("Opción inválida.")