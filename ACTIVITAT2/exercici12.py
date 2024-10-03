num = int(input("Introduce un numero: "))

suma = 0

for i in range(1, num + 1):
    suma += i
    print(f"+ {i}: Total = {suma}")

print(f"La suma de todos los numeros del 1 hasta el {num} és {suma}.")