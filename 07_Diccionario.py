### Diccionario ###

# Declaracion de diccionarios y type
mi_diccionario = dict()
print(type(mi_diccionario))
mi_otro_diccionario = {} 
print(type(mi_otro_diccionario))

# Colocar datos en un diccionario y ver de forma general
mi_otro_diccionario = {"Nombre": "Marco", "Apellido": "Lopez", "Edad": 22}
print(mi_otro_diccionario)
# Diccionario guarda datos en formato clave-valor
mi_diccionario = {
    "Nombre": "Marco", 
    "Apellido": "Lopez", 
    "Edad": 22,
    "Lenguajes": {"Python", "Java", "C++"},
    1: 1.85
    }
print(mi_diccionario)

# Sacar datos de un diccionario y modificarlos
print(mi_diccionario[1])
mi_diccionario[1] = 1.80
print(mi_diccionario[1])

# Añadir una nueva clave-valor a un diccionario
mi_diccionario["Gato"] = "Nina"
print(mi_diccionario)

# Eliminar una clave-valor de un diccionario
del mi_diccionario["Gato"]
print(mi_diccionario)

# Revisar si un diccionario tiene una clave
print("Nombre" in mi_diccionario)

# Funciones para diccionarios
print(mi_diccionario.keys()) # Lista de claves
print(mi_diccionario.values()) # Lista de valores
print(mi_diccionario.items()) # Lista de tuplas clave-valor

# Una lista de Claves pasar a un diccionario
lista_de_claves = ["Nombre", "Apellido", "Edad", "Lenguajes"]
mi_diccionario = dict.fromkeys(lista_de_claves)
print(mi_diccionario)