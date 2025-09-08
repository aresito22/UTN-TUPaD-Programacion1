import random

numeros = random.sample(range(1, 51), 25)

carton = [numeros[i:i+5] for i in range(0, 25, 5)]

print("Este es tu carton: ")
for fila in carton:
    print(fila)

print("")
print("--------")

contador = 0

while contador != 25:
    numero_a_buscar = random.randint(1, 51)
    print("")
    print(f"El número sorteado es {numero_a_buscar}")
    print("")

    encontrado = False

    for fila in carton:
        for i in range(5):
            if numero_a_buscar == fila[i]:
                print("Encontrado!")
                fila[i] = 0
                contador += 1
                encontrado = True

                print("")
                print("Este es tu cartón ahora:")      
                for fila in carton:
                    print(fila) 
    
    if not encontrado:
        print("No lo tenés.")

print("")
print("Bingo! Ganaste.")