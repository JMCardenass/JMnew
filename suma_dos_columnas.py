print("Ingrese los elementos de la columna 1 separados por espacios:")
columna1 = input().split()

print("Ingrese los elementos de la columna 2 separados por espacios:")
columna2 = input().split()

for x in range(len(columna1)):
    elemento1 = int(columna1[x])
    elemento2 = int(columna2[x])
    columna3 = elemento1 + elemento2
    print(elemento1, "+", elemento2, "=", columna3)