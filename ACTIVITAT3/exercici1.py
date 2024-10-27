num = int(input("Introdueix un número entre 10 i 100: "))

if num < 10 or num > 100:
    print("El número ha de ser entre 10 i 100.")
else:
    numeros = tuple(range(1, num + 1))
    print(numeros)