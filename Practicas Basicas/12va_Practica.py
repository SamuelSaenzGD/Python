
import os

bucle = True

while bucle:
    try:
        num = int(input("Ingrese un numero para generar la tabla de multiplicar: "))
        
        for i in range(1, 13):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")
            
        print("Desea generar otra tabla? (s/n): ")
        respuesta = input().lower()
        
        os.system("cls")  # Limpiar la pantalla (Windows)
        
        if respuesta != 's':
            bucle = False
            print("\n\n\nPrograma terminado.\n\n")
            
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número entero.\n")
        continue