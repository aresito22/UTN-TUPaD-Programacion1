#1
print("Hola Mundo!")

#2
nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

#3
nombre = input("Ingrese su primer nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_de_residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}.")

#4
import math

radio = float(input("Ingrese el area: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio

print(f"El area es {area} y el perimetro es {perimetro}")

#5
segundos = int(input("Ingrese la cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {segundos/3600} horas")

#6
multiplicando = int(input("Ingrese el número a multiplicar: "))

# Hecho de manera secuencial tal como fue instruido, en vez de con un bucle for que sería más ordenado:
print(multiplicando * 1)
print(multiplicando * 2)
print(multiplicando * 3)
print(multiplicando * 4)
print(multiplicando * 5)
print(multiplicando * 6)
print(multiplicando * 7)
print(multiplicando * 8)
print(multiplicando * 9)
print(multiplicando * 10)

#7
print("Ingrese dos números (que no sean 0): ")
num_1 = int(input())
num_2 = int(input())

print(f"Suma: {num_1 + num_2}")
print(f"Resta: {num_1 - num_2}")
print(f"Multiplicación: {num_1 * num_2}")
print(f"División: {num_1 / num_2}")

#8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Su IMC es {imc}")

#9
celsius = float(input("Ingrese una temperatura en grados Celsius: "))

fahrenheit = 9/5 * celsius + 32

print(f"La temperatura en Fahrenheit es {fahrenheit}")

#10
print("Ingrese 3 números:")
a = float(input())
b = float(input())
c = float(input())

promedio = (a + b + c) / 3

print(f"El promedio es {promedio}.")