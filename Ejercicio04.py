ganadores = []
n = 6
while n != 0:
    ganadores.append(int(input("Cuales son los números ganadores de la primitiva\n")))
    n = n-1
ganadores.sort()
print(ganadores)