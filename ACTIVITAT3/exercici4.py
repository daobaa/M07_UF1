numeros = input("Introdueix 10 números separats per un espai: ")

numeros_llista = [int(num) for num in numeros.split()]

if len(numeros_llista) != 10:
    print("Si us plau, introdueix exactament 10 números.")
else:
    numeros_tupla = tuple(sorted(numeros_llista))
    print("Tupla ordenada:", numeros_tupla)