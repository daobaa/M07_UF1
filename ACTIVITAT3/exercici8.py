numeros = input("Introdueix 10 números separats per espais: ")

numeros_llista = [int(num) for num in numeros.split()]

if len(numeros_llista) != 10:
    print("Si us plau, introdueix exactament 10 números.")
else:
    suma_total = sum(numeros_llista)

    mitjana = suma_total / len(numeros_llista)

    numeros_llista.extend([suma_total, mitjana])
    
    print("Números de l'usuari:", numeros_llista[:-2])
    print("Suma total:", suma_total)
    print("Mitjana:", mitjana)