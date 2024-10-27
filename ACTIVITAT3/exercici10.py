abecedari = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

abecedari_filtrat = [lletra for i, lletra in enumerate(abecedari, start=1) if i % 3 != 0]

tupla_abecedari = tuple(abecedari_filtrat)

print("Llista:", abecedari_filtrat)
print("Tupla:", tupla_abecedari)