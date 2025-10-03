# 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

# 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

nombre = input("Nombre: ")
saludar_usuario(nombre)

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

# 4
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Radio: "))
print(f"Area: {calcular_area_circulo(radio)}")
print(f"Perimetro: {calcular_perimetro_circulo(radio)}")

# 5
def segundos_a_horas(segundos):
    return segundos / 60

segundos = int(input("Segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} * {i}: {numero * i}")

num = int(input("Número: "))
tabla_multiplicar(num)

# 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    resultados = (suma, resta, multiplicacion, division)
    return resultados

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))

print(operaciones_basicas(num_1, num_2))

# 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
print(f"Su IMC es {calcular_imc(peso, altura)}.")

# 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

temp_c = float(input("Ingrese la temperatura en celsius: "))
print(f"{temp_c} celsius en fahrenheit es {celsius_a_fahrenheit(temp_c)}.")

# 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num_1 = float(input("Ingrese el valor del primer número: "))
num_2 = float(input("Ingrese el valor del segundo número: "))
num_3 = float(input("Ingrese el valor del tercer número: "))

print(f"El promedio es {calcular_promedio(num_1, num_2, num_3)}")