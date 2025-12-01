

bucle = True

while bucle:
    try:
        dividendo = int(input("Ingrese el valor a dividir: "))
        divisor = int(input("Ingrese el divisor: "))
        
        if divisor == 0:
            print("Error: No se puede dividir por cero. Intente nuevamente.")
        else:
            resultado = dividendo / divisor
            print(f"El resultado de {dividendo} dividido por {divisor} es: {resultado}")
            bucle = False
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números enteros.")
