import random

victorias_jugador = 0
victorias_maquina = 0

while True:
    print("")
    print("-NUEVA PARTIDA-")
    print("Ingrese la opción a jugar:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")
    print("4 - Salir")
    opcion_jugador = int(input("Opción: "))
    print("")

    opcion_maquina = random.randint(1, 3)

    if opcion_jugador == 1:
        print("Tu jugada: Piedra")
        if opcion_maquina == 1:
                print("Maquina: Piedra")
                print("Empate.")
        elif opcion_maquina == 2:
                print("Maquina: Papel")
                print("Perdiste!")
                victorias_maquina += 1
        elif opcion_maquina == 3:
                print("Maquina: Tijera")
                print("Ganaste!")
                victorias_jugador += 1
    elif opcion_jugador == 2:
        print("Tu jugada: Papel")
        if opcion_maquina == 2:
                print("Maquina: Papel")
                print("Empate.")
        elif opcion_maquina == 3:
                print("Maquina: Tijera")
                print("Perdiste!")
                victorias_maquina += 1
        elif opcion_maquina == 1:
                print("Maquina: Piedra")
                print("Ganaste!")
                victorias_jugador += 1
    elif opcion_jugador == 3:
        print("Tu jugada: Tijera")
        if opcion_maquina == 3:
                print("Maquina: Tijera")
                print("Empate.")
        elif opcion_maquina == 1:
                print("Maquina: Piedra")
                print("Perdiste!")
                victorias_maquina += 1
        elif opcion_maquina == 2:
                print("Maquina: Papel")
                print("Ganaste!")
                victorias_jugador += 1    

    print(f"JUGADOR: {victorias_jugador}")
    print(f"MAQUINA: {victorias_maquina}")

    if opcion_jugador == 4:
        break

print("")
print("-VICTORIAS TOTALES-")
print(f"JUGADOR: {victorias_jugador}")
print(f"MAQUINA: {victorias_maquina}")
print("")
if victorias_jugador > victorias_maquina:
    print("Ganaste!")
elif victorias_jugador < victorias_maquina:
    print("Perdiste!")
else:
    print("Empate.")