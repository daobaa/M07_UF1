pal1 = input("Introduce una palabra: ")
pal2 = input("Introduce otra palabra: ")

newpal1 = pal2[:2] + pal1[2:]
newpal2 = pal1[:2] + pal2[2:]

print("Las palabras intercambiadas son: " + newpal1, newpal2)