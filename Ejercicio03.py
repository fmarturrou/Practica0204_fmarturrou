asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for asignatura in asignaturas:
    notas.append(input(f"¿Qué nota has sacado en {asignatura}?")) 
for posiciónlista in range(len(asignaturas)): 
#Con la línea de arriba estamos diciendo que el for cree un número según la posición en la lista
#entonces crea una lista [0, 1, 2, 3, 4, 5] en la que al hacer el print
#imprime la asigantura y la nota en ese orden, por lo que se imprime correctamente
    print(f"En {asignaturas[posiciónlista]} has sacado {notas[posiciónlista]}")