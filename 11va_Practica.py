
bucle = True

while bucle:
    try:
        num = int(input("Ingrese un numero entero positivo: "))
        
        if num >= 0:
            for i in range(num):
                for j in range(i + 1):
                    print("*", end="")
                print("")
            
            bucle = False 
        else:
            print("Error: El número debe ser positivo. Intente nuevamente.\n")
            
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número.\n")
        continue

