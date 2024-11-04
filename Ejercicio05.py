numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
numeros_inversos = numeros[::-1]
resultado = ', '.join(map(str, numeros_inversos))
print(resultado)