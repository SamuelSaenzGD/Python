
#variables

bucle = True
payaso = 112
muñecas = 75

#Programa principal

while bucle:
    try:
        cajas_payasos = int(input("Ingrese la cantidad de cajas de payasos a enviar: "))
        cajas_muñecas = int(input("Ingrese la cantidad de cajas de muñecas a enviar: "))
        
        if cajas_payasos < 0 or cajas_muñecas < 0:
            print("Error: La cantidad de cajas no puede ser negativa. Intente nuevamente.")
        else:
            peso_total = (cajas_payasos * payaso) + (cajas_muñecas * muñecas)
            print(f"El peso total del envío es: {peso_total} gramos")
            bucle = False
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese números enteros.")