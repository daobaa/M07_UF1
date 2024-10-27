areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Segon element:", areas_pis[1])
print("Últim element:", areas_pis[-1])
print("Àrea de la Terrassa:", areas_pis[areas_pis.index("Terrassa") + 1])
print("Primer al tercer element:", areas_pis[0:3])
print("Tercer element a l'últim:", areas_pis[2:])

total_habitacions = areas_pis[areas_pis.index("Habitació1") + 1] + areas_pis[areas_pis.index("Habitació2") + 1]
print("Total de l'àrea de les dues habitacions:", total_habitacions)

areas_pis[areas_pis.index("Lavabo") + 1] = 8.50
print("Nova llista amb l'àrea del lavabo modificada:", areas_pis)

areas_pis.extend(["Pati Interior", 2.78])
print("Nova llista amb 'Pati Interior' afegit:", areas_pis)

total_area = sum(area for area in areas_pis if isinstance(area, (int, float)))
print("Total de l'àrea del pis:", total_area)