mesos = ("Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre")

while True:
    num = int(input("Introdueix un número entre 0 i 12 (0 per sortir): "))
    if num == 0:
        print("Programa finalitzat.")
        break
    elif 1 <= num <= 12:
        print(mesos[num - 1])
    else:
        print("El número ha de ser entre 0 i 12.")