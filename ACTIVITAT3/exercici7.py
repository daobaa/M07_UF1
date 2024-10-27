contactes = {}

while True:
    nom = input("Introdueix el nom del contacte (o escriu 'no' per sortir): ")

    if nom.lower() == 'no':
        break
    if nom in contactes:
        print("El nom ja existeix. No s'ha afegit.")
        continue

    edat = int(input("Introdueix l'edat del contacte: "))
    contactes[nom] = edat
    
print("Contactes:", contactes)