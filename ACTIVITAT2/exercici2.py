val = int(input("Introduce un valor en euros(€): "))

while True:
    iva = int(input("Introduce el IVA a aplicar(4, 10, 21): "))
    if iva in [4,10,21]:
        break
    else:
        print("IVA no válido. Por favor, inténtalo de nuevo.")

total = val + (val * iva / 100)

print(val, " es el valor original.")
print(iva, " es el IVA a añadir.")
print(total, " es el valor + IVA.")

