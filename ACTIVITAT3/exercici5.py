frase = input("Introdueix una frase: ")

frase_sense_espais = frase.replace(" ", "")

tupla_frase = tuple(frase_sense_espais)

frase_sense_repetits = "".join(dict.fromkeys(frase_sense_espais))

print("Tupla:", tupla_frase)
print("Frase sense caràcters repetits:", frase_sense_repetits)