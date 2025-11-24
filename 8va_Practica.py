
frase = input("Ingrese una frase: ")

vocal = input("Ingrese una vocal: ").lower()

if len(vocal) != 1 or vocal not in "aeiou":
    print("Error: Debe ingresar una única vocal.")
else:
    frase_modificada = frase.replace(vocal, vocal.upper())
    print(frase_modificada)