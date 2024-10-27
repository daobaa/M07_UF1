assignatures = ["Matemàtiques", "Història", "Biologia", "Física", "Llengua Catalana", "Educació Física"]
notes = {}

for assignatura in assignatures:
    nota = float(input(f"Introdueix la nota per a {assignatura}: "))
    notes[assignatura] = nota

for assignatura, nota in notes.items():
    print(f"A {assignatura} ha tret {nota}")