### Bucles ###

# While en Python se puede usar el Else
mi_condicion = 0
while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else: # Es opcional
    print("Mi condicion es mayor o igual a 10")

# Puede haber dentro de un While un if
while mi_condicion < 20:
    mi_condicion += 2
    if mi_condicion == 16:
        print("Mi condicion es 16")
    print(mi_condicion)

# Para romper un While se usa el break
mi_condicion = 0
while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 1
    if mi_condicion == 5:
        print("Mi condicion es 5 y se detiene el While")
        break

# For en Python se usa para iterar sobre una lista, tupla, set o diccionario
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for elemento in mi_lista:
    print(elemento)

mi_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for elemento in mi_tuple:
    print(elemento)

mi_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
for elemento in mi_set:
    print(elemento)

mi_diccionario = {"Nombre": "Marco", "Apellido": "Lopez", "Edad": 22}
for clave, valor in mi_diccionario.items():
    print(clave, valor)
    if clave == "Nombre": # En un for se puede usar un if para filtrar
        print("El nombre es:", valor)
        continue # Y tambien se puede usar el continue para saltar el siguiente elemento
        print("Se lo salta")
    if clave == "Apellido": # Y tambien se puede usar el break
        print("El apellido es:", valor)
        break
else: # Y a la vez se puede usar un else como el while
    print("No hay datos en el diccionario")

print("La ejecucion continua")