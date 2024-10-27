num = int(input("Introdueix un número de l'1 al 10: "))

if 1 <= num <= 10:
    taula_multiplicar = [num * i for i in range(1, 11)]
    print(", ".join(map(str, taula_multiplicar)))
else:
    print("El número ha de ser de l'1 al 10.")