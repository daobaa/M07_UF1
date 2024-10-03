val1 = int(input("Introduce un valor:"))
val2 = int(input("Introduce otro valor:"))

suma = val1 + val2
resta = val1 - val2
division = val1 / val2 if val2 != 0 else "No se puede dividir entre cero"
multiplicacion = val1 * val2

print(f"la suma es: {suma}")
print(f"La resta es: {resta}")
print(f"La división es: {division}")
print(f"La multiplicación es: {multiplicacion}")