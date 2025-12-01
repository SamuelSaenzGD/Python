import os
# Importamos 'os' para trabajar con rutas de archivos

bucle = True

# --- Definición de la Ruta del Archivo ---
# Obtenemos la ruta del directorio donde está el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Construimos la ruta completa del archivo que queremos crear
ruta_completa_archivo = os.path.join(directorio_script, "numeros.txt")
# ----------------------------------------

while bucle:
    try:
        num = int(input("Introduce un número entero: "))
        
        # Usamos la nueva variable con la ruta completa
        with open(ruta_completa_archivo, "a") as archivo:
            archivo.write(f"\n--- Tabla del {num} ---\n") 
            
            for i in range(1, 13):
                resultado = num * i
                linea = f"{num} x {i} = {resultado}\n" 
                
                print(linea.strip()) 
                archivo.write(linea)
            
        print("\nDesea continuar? (s/n): ")
        respuesta = input().lower()
        if respuesta != 's':
            bucle = False
        
    except ValueError:
        print("Error: Debes introducir un número entero válido.")