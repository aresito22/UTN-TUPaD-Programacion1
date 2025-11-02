# 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
num = int(input("Ingrese un número: "))
print()
for i in range(1, num + 1):
    print(f"Factorial de {i}: {factorial(i)}")

# 2
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
num = int(input("Ingrese una posición de la secuencia de Fibonacci: "))
print()
for i in range(num+1):
    print(f"{fibonacci(num-i)}")

# 3
def potencia(base, exponente):
    if exponente == 0:          
        return 1
    else:               
        return base * potencia(base, exponente-1)

base = int(input("Número base: "))
exponente = int(input("Número exponente: "))

print(f"\nResultado: {potencia(base, exponente)}")

# 4
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
num = int(input("Número a convertir: "))
print(f"\n{num} = {decimal_a_binario(num)}")