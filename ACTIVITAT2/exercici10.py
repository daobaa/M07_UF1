import random

def guess_num():
    num_secret = random.randint(1, 100)
    tries = 0
    guessed = False

    print("Adivina el numero entre 1 y 100!")

    while not guessed:
        ask = int(input("Introduce un numero: "))
        tries += 1

        if ask < num_secret:
            print("El numero es mas grande")
        elif ask > num_secret:
            print("El numero es mas pequeño")
        else:
            guessed = True
            print(f"Has acertado el numero en {tries} intentos.")

if __name__ == "__main__":
    guess_num()