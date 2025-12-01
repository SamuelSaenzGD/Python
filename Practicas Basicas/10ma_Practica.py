
bucle = True

while bucle:
    num = int(input("Ingrese un numero entero positivo: "))
    
    if num >= 0:
        for i in range(num):
            if i % 2 != 0:
                print(i, end=", ")
        
        bucle = False

