
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")

datos_personales = {
    "Nombre": nombre,
    "Edad": edad,
    "Dirección": direccion
}

print(datos_personales["Nombre"], " tiene ", datos_personales["Edad"], " años y vive en ", datos_personales["Dirección"])

listadeDatos = []
listadeDatos.append(datos_personales)

print(listadeDatos[0].get("Nombre"))