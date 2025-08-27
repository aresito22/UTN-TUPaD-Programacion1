#1
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad")

#2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#3
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Ingrese un número par.")

#4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Niño")
elif edad >= 12 or edad < 18:
    print("Adolescente.")
elif edad >= 18 or edad < 30:
    print("Adulto joven.")
else:
    print("Adulto.")
    
#5
contrasena = input("Ingrese su contraseña: ")
cantidad_de_caracteres = len(contrasena)

if cantidad_de_caracteres >= 8 and cantidad_de_caracteres <= 14:
    print("Contraseña correcta.")
else:
    print("Ingrese una contraseña de entre 8 y 14 caracteres")

#6
import statistics
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = statistics.mode(numeros_aleatorios)
mediana = statistics.median(numeros_aleatorios)
media = statistics.mean(numeros_aleatorios)

if (media > mediana) and (mediana > moda):
    print("Sesgo positivo.")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo.")
# Abajo utilicé elif en vez de else porque, a pesar de ser la última condición, 
# quiero que solo se ejecute en ese caso puntual y no en otra posible combinación de patrones.
elif (media == mediana == moda):
    print("Sin sesgo.")

#7
frase_ingresada = input("Ingrese una frase: ")
ultimo_caracter = frase_ingresada[-1]

if ord(ultimo_caracter) >= 97 and ord(ultimo_caracter) <= 122:
    print(f"{frase_ingresada}!")
else:
    print(frase_ingresada)

#8
nombre = input("Ingrese su nombre:")
print("") # Para hacerlo un poco más prolijo
print("Ingrese 1 si quiere ver su nombre en mayúsculas.")
print("Ingrese 2 si quiere ver su nombre en minúculas.")
print("Ingrese 3 si quiere ver su nombre con la primera letra en mayuscula.")
opt = int(input())

if opt == 1:
    print(nombre.upper())
elif opt == 2:
    print(nombre.lower())
elif opt == 3:
    print(nombre.title())
else:
    print("Opción inválida.")

#9
magnitud = int(input("Ingrese la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve.")
elif magnitud >= 3 and magnitud < 4:
    print("Leve.")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado.")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte.")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte.")
else:
    print("Extremo.")

#10
fecha = input("Ingrese la fecha (MM/DD): ")
dia, mes = fecha.split("/")
dia = int(dia)
mes = int(mes)

hemisferio = input("Ingrese el hemisferio (N/S): ")
hemisferio = hemisferio.upper() # Por si el usuario lo ingresa en minúscula

if hemisferio == "N":
    if mes == 1 or mes == 2:
        print("Invierno.")
    elif mes == 3:
        if dia < 21:
            print("Invierno.")
        else:
            print("Primavera.")
    elif mes == 4 or mes == 5:
        print("Primavera.")
    elif mes == 6:
        if dia < 21:
            print("Primavera.")
        else:
            print("Verano.")
    elif mes == 7 or mes == 8:
        print("Verano.")
    elif mes == 9:
        if dia < 20:
            print("Verano.")
        else:
            print("Otoño")
    elif mes == 10 or mes == 11:
        print("Otoño.")
    elif mes == 12:
        if dia < 21:
            print("Otoño")
        else:
            print("Invierno.")
    else:
        print("Mes inválido.")
elif hemisferio == "S":
    if mes == 1 or mes == 2:
        print("Verano.")
    elif mes == 3:
        if dia < 21:
            print("Verano.")
        else:
            print("Otoño.")
    elif mes == 4 or mes == 5:
        print("Otoño.")
    elif mes == 6:
        if dia < 21:
            print("Otoño.")
        else:
            print("Invierno.")
    elif mes == 7 or mes == 8:
        print("Invierno.")
    elif mes == 9:
        if dia < 20:
            print("Invierno.")
        else:
            print("Primavera")
    elif mes == 10 or mes == 11:
        print("Primavera.")
    elif mes == 12:
        if dia < 21:
            print("Primavera")
        else:
            print("Verano.")
    else:
        print("Mes inválido.")
else:
    print("Mes inválido")