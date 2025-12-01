
bucle = True

while bucle:
    a = input("Ingrese una palabra o frase: ")

    if a == a[::-1]:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
    
    print("¿Desea ingresar otra palabra o frase? (s/n): ")
    
    respuesta = input().lower()
    if respuesta != 's':
        bucle = False
        print("\n\n\nPrograma terminado.\n\n")