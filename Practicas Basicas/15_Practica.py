
numeros = []

for i in range(1,11):
    numeros.append(i)

print("Forma de imprimir #1:")
print(numeros[::-1])

print("\nForma de imprimir #2:")
for i in range(1, 11):
    print(numeros[-i], end=", ")