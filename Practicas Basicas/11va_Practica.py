
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

#Las excepciones en Python son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal del mismo.
# Algunos de los tipos más comunes de excepciones en Python incluyen:

#1. ValueError: Ocurre cuando una función recibe un argumento con el tipo correcto pero un valor inapropiado.
#2. TypeError: Se produce cuando una operación o función se aplica a un objeto de un tipo inapropiado.
#3. IndexError: Sucede cuando se intenta acceder a un índice que está fuera del rango de una lista o secuencia.
#4. KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
#5. ZeroDivisionError: Se produce cuando se intenta dividir un número por cero.
#6. FileNotFoundError: Ocurre cuando se intenta abrir un archivo que no existe.
#7. ImportError: Sucede cuando una importación de módulo falla.
#8. AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
#9. RuntimeError: Se produce cuando ocurre un error que no pertenece a ninguna de las categorías anteriores.
#10. SyntaxError: Ocurre cuando el código contiene un error de sintaxis y no puede ser interpretado por Python.

