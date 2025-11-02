# P = Pared
# D = Dragón
# S = Salida
laberinto = [
    ['P', 'P', 'P', 'P', 'P'],
    ['D', '', '', '', 'P'],
    ['P', '', 'P', '', 'S'],
    ['P', '', '', '', 'P'],
    ['P', 'P', 'P', 'P', 'P']
]

def buscar_salida(laberinto, fila, columna):
    if laberinto[fila][columna] == 'S':
        return True
    elif laberinto[fila][columna] == 'P' or laberinto[fila][columna] == '.':
        return False
    elif laberinto[fila][columna] == '':
        pass
    
for fila in laberinto:
    print(*fila)

# Tener en cuenta la posición actual del dragón para poder moverlo
for i, fila in enumerate(laberinto):
    for j, posicion in enumerate(fila):
        if posicion == 'D':
            fila_dragon = i
            columna_dragon = j

print("\n1 - Mover arriba")
print("2 - Mover abajo")
print("3 - Mover derecha")
print("4 - Mover izquierda")

while True:
    try:
        movimiento = int(input("Movimiento: "))
        if movimiento < 1 or movimiento > 4:
            print("Inválido - opción no encontrada.")
    except ValueError:
        print("Inválido - debe ser un número entero.")

    if movimiento == 1: # Arriba
        buscar_salida(laberinto, fila_dragon+1, columna_dragon)
    elif movimiento == 2: # Abajo
        buscar_salida(laberinto, fila_dragon-1, columna_dragon)
    elif movimiento == 3: # Derecha
        buscar_salida(laberinto, fila_dragon, columna_dragon+1)
    elif movimiento == 4: # Izquierda
        buscar_salida(laberinto, fila_dragon, columna_dragon-1)