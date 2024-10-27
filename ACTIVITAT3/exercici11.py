divises = {
    "euro": "€",
    "dòlar": "$",
    "ien": "¥",
    "lliura": "£",
}

divisa_usuari = input("Introdueix una divisa: ").lower()

if divisa_usuari in divises:
    print(f"El símbol de {divisa_usuari} és {divises[divisa_usuari]}")
else:
    print("La divisa no està al diccionari")
