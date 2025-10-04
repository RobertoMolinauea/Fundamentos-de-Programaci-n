# Tarea: Trabajo con Archivos de Texto en Python
# Curso: Fundamentos de Programación

# 1) ESCRITURA: creo (o sobrescribo) my_notes.txt con tres notas.
with open("my_notes.txt", "w", encoding="utf-8") as f:
    f.write("Hoy repasé lectura y escritura de archivos en Python.\n")
    f.write("Usar 'with open' me evita olvidar cerrar el archivo.\n")
    f.write("Practicar con GitHub me ayuda a llevar registro.\n")

# 2) LECTURA LÍNEA POR LÍNEA con readline()
archivo = open("my_notes.txt", "r", encoding="utf-8")

print("Contenido de my_notes.txt (línea por línea):")
linea = archivo.readline()
while linea != "":
    print(linea.strip())   # limpio el salto de línea
    linea = archivo.readline()

# 3) CIERRE explícito
archivo.close()
print("\nArchivo cerrado:", archivo.closed)