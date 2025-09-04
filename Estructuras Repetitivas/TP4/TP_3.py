#1
for i in range (0,101):
    print(i)

#2
numero = input("Ingrese un número entero: ")
for i in range(len(numero)):
    contador += 1

print(f"Su número tiene {contador} dígitos.")

#3
numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
suma = 0

#               Puse numero_1 + 1 para excluir el propio número de la cuenta
for i in range(numero_1 + 1, numero_2):
    suma += i

print(suma)

#4
suma = 0
while True:
    valor_ingresado = int(input("Ingrese el número a sumar o ingrese 0 para frenar la suma: "))
    if valor_ingresado == 0:
        break
    else:
        suma = suma + valor_ingresado

print(f"La suma de los números ingresados es {suma}")

#5
import random

numero_secreto = random.randint(0, 9)
intento = int(input("Adivine el número secreto: "))
contador_intentos = 1

while intento != numero_secreto:
    contador += 1
    print("Incorrecto!")
    intento = int(input("Adivine el número secreto: "))

print("Correcto!")
print(f"Adivinar el número le tomó {contador_intentos} intentos.")

#6
for i in range(100, 0, -2):
    print(i)

#7
numero_usuario = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(numero_usuario):
    suma = suma + i

print(f"La suma de los números entre 0 y {numero_usuario} es {suma}")

#8
contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

for i in range(100):
    var = int(input("Ingrese el número {i}: "))
    if var % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

    if var > 0:
        contador_positivos += 1
    else:
        contador_negtivos += 1

print(f"Hay {contador_pares} números pares.")
print(f"Hay {contador_impares} números impares.")
print(f"Hay {contador_positivos} números positivos.")
print(f"Hay {contador_negativos} números negativos.")

#9
suma = 0
for i in range(100):
    var = int(input(f"Ingrese el número {i}"))
    suma = suma + var

media = suma / 100
print(f"La media de esos números es {media}")

#10
var = int(input("Ingrese el número a invertir: "))
var = str(var)
temp = []

for i in range(len(var)):
    temp.append(var[len(var) - 1 - i])

numero_invertido = ("".join(temp))
numero_invertido = int(numero_invertido)
print(numero_invertido)