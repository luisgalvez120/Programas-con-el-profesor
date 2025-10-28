# Diccionarios

# Crear un diccionario
diccionario = {"azul":"blue", "rojo":"red", "verde":"green", "amarillo":"yellow"}

# Agregar un nuevo elemento al diccionario
diccionario["negro"] = "black"

# Imprimir diccionario actualizado
print(diccionario)

# Agregar un nuevo elemento al diccionario
diccionario["rojo"] = ""
print(diccionario)

diccionario["rosado"] = "pink"
print(diccionario)

# Modificar elementos
diccionario["rosado"] = "PINK-COLOR"
print(diccionario)

# Eliminar elementos
del(diccionario["rosado"])
print(diccionario)