
bucle = True

while bucle:
    try:
        letra = input("Ingrese una letra: ")
        
        frase = input("Ingrese una frase: ")
        
        if len(letra) == 1:
            contador = 0
            for char in frase:
                if char == letra:
                    contador += 1
            print(f"La letra '{letra}' aparece {contador} veces en la frase.")
            bucle = False
        else:
            print("Error: Debe ingresar solo una letra. Intente nuevamente.\n")
            
    except Exception as e:
        print(f"Error inesperado: {e}\n")
        continue
        
            
    