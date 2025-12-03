
import os
bucle = True

# Obtenemos la ruta del directorio donde está el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

while bucle:
    
    try:
        num = int(input("Introduce un número entero: "))
        
        nombreArchivo = f"tabla-{num}.txt"
        ruta_Archivo = os.path.join(directorio_script, nombreArchivo)
        
        with open(ruta_Archivo, "r") as archivo:
            contenido = archivo.read()
            print(contenido)
        
    except FileNotFoundError:
        print(f"Error: El archivo 'tabla-{num}.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        
    