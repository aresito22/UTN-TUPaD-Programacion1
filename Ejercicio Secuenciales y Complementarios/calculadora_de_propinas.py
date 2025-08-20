print("Ingrese el monto total de la cuenta:")
total_a_pagar = int(input())

propina_10 = total_a_pagar * 0.1
propina_15 = total_a_pagar * 0.15

print("")
print(f"Propina sugerida del 10%: {propina_10}")
print(f"Total a pagar con propina del 10%: {total_a_pagar + propina_10}")

print("")
print(f"Propina sugerida del 15%: {propina_15}")
print(f"Total a pagar con propina del 15%: {total_a_pagar + propina_15}")