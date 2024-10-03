val1 = int(input("Introduce un valor: "))
val2 = int(input("Introduce otro valor: "))
if val1 > val2:
    print(val1, ">", val2,)
elif val2 > val1:
    print(val2, "<", val1)
else:
    print(val1, "=", val2)