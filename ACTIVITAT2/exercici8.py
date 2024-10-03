val = input("Introduce entre 1 y 3 palabras separadas por espacios: ")
words = val.split()

if 1 <= len(words) <= 3:
    for word in words:
        print(f"Palabra: {word}")
        print(f"Numero de carácteres: {len(word)}")
        print(f"Primer carácter: {word[0]}")
        print(f"Ultimo carácter: {word[-1]}")
        print("")
else:
    print("Introduce entre 1 y 3 palabras!")