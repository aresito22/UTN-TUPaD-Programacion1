tarjetas = ["1234567890123456", "9876543210987654", "5555666677778888"]
saldos = [150.50, 25.00, -10.00]

while True:
    print()
    print("1 - Ingresar números de tarjeta")
    print("2 - Asignar saldos a tarjetas")
    print("3 - Mostrar todas las tarjetas y sus saldos")
    print("4 - Consultar saldo por número")
    print("5 - Listar saldos negativos o en 0")
    print("6 - Agregar tarjeta")
    print("7 - Cargar debito o saldo")

    opt = input("Opción")

    if opt == "1":
        tarjetas = []
        saldos = []

        while True:
            num_tarjeta = input("Ingrese un número de tarjeta o presione 0 para salir: ")

            if num_tarjeta == "0":
                break
            elif len(num_tarjeta) == 16:
                tarjetas.append(num_tarjeta)
            else:
                print("Número inválido.")

    elif opt == "2":
        for tarjeta in tarjetas:
            saldo_tarjeta = float(input(f"Ingrese el número de la tarjeta {tarjeta}: "))
            saldos.append(saldo_tarjeta)

    elif opt == "3":
        for i, tarjeta in enumerate(tarjetas):
            print(f"Tarjeta {tarjeta}: {saldos[i]} pesos")

    elif opt == "4":
        tarjeta_buscar = input("Ingrese el número de tarjeta a consultar: ")

        tarjeta_encontrada = False
        for i, tarjeta in enumerate(tarjetas):
            if tarjeta_buscar == tarjeta:
                print(f"Tarjeta {tarjeta}: {saldos[i]} pesos")
                tarjeta_encontrada = True

        if tarjeta_encontrada == False:
            print("Tarjeta no encontrada.")

    elif opt == "5":
        for i, tarjeta in enumerate(tarjetas):
            if saldos[i] <= 0:
                print(f"Tarjeta {tarjeta}: {saldos[i]} pesos")

    elif opt == "6":
        nueva_tarjeta = input("Ingrese el número de la nueva tarjeta: ")
        nuevo_saldo = float(input("Ingrese el saldo de la nueva tarjeta: "))

        tarjetas.append(nueva_tarjeta)
        saldos.append(nuevo_saldo)

    elif opt == "7":
        for i in range(len(tarjetas)):
            print(f"{i} - {tarjetas[i]}")
        print()

        tarjeta_actualizar = int(input("Qué número de tarjeta desea actualizar? Ingrese el indice: "))
        saldo_actualizar = float(input("Ingrese la cantidad de saldo a actualizar: "))

        saldos[tarjeta_actualizar] = saldos[tarjeta_actualizar] + (saldo_actualizar)

    elif opt == "8":
        print()
        print("Saliendo.")
        break
    
    else:
        print("Opción inválida.")




