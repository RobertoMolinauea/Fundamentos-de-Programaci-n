# U4_T4.3 - Trabajando con Diccionarios en Python
# Tema: Diccionarios
# Este programa crea un diccionario con datos personales ficticios
# y realiza varias operaciones básicas.

# 1) Crear el diccionario con datos iniciales
informacion_personal = {
    "nombre": "Carlos Gómez",
    "edad": 30,
    "ciudad": "Cuenca",
    "profesion": "Profesor"
}

# 2) Acceder al valor de "ciudad" y modificarlo
# (Antes estaba "Cuenca", ahora lo cambiamos a otra ciudad)
informacion_personal["ciudad"] = "Guayaquil"

# 3) Agregar una nueva clave relacionada a la profesión
# Ya existe "profesion", por eso añadimos un campo extra
informacion_personal["profesion_secundaria"] = "Escritor"

# 4) Verificar si existe la clave "telefono"
# Si no está, la creamos con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0998765432"

# 5) Eliminar la clave "edad" porque no la necesitamos
del informacion_personal["edad"]

# 6) Imprimir el diccionario final para ver el resultado
print("Diccionario final:")
print(informacion_personal)
