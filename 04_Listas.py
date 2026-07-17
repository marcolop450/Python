### Listas ###

# Declaración de listas y Creación de listas
mi_lista = list() # Declaración de una lista vacía
mi_otra_lista = [] # Declaración de una lista vacía
mi_lista_cargada = [1, 2, 3, 4, 5] # Declaración de una lista con valores
print(mi_lista)
print(mi_otra_lista)
print(mi_lista_cargada)

# Tamaño de una lista
print(len(mi_lista)) # Tamaño de una lista vacía
print(len(mi_otra_lista)) # Tamaño de una lista vacía   
print(len(mi_lista_cargada)) # Tamaño de una lista con valores

# Lista con diferentes tipos de datos
mi_lista_mixta = [0, "Hola", 3.64, True, [3, 2, 3],0]
print(mi_lista_mixta)

# La lista en Type es de tipo list sin importar el tipo de dato que contenga
print(type(mi_lista_mixta)) # <class 'list'>

# Acceso a los elementos de una lista
print(mi_lista_mixta[0]) # Acceso al primer elemento de la lista
print(mi_lista_mixta[2]) # Acceso al tercer elemento de la lista
print(mi_lista_mixta[-1]) # Acceso al último elemento de la lista
print(mi_lista_mixta[-3]) # Acceso al tercer elemento desde el final de la lista

# Funciones de listas
print(mi_lista_mixta.count(1)) # Cuenta cuantas veces aparece un elemento en la lista

# Sacar en variables elmentos de una lista
lista_de_dato = ["Marco", "Lopez", 22]
name, surname, age = lista_de_dato
print(name)

# Concatenación de listas
mi_lista_1 = [1, 2, 3]
mi_lista_2 = [4, 5, 6]
mi_lista_concatenada = mi_lista_1 + mi_lista_2  
print(mi_lista_concatenada) # Concatenación de listas

# Insertar y Modificar elementos de una Lista
mi_lista_mixta.append("Nuevo elemento") # Inserta un elemento al final de la lista
print(mi_lista_mixta)
mi_lista_mixta.insert(1, "Elemento insertado") # Inserta un elemento en una posición específica de la lista
print(mi_lista_mixta)
mi_lista_mixta[1] = "Negro" # Modificando un dato
print(mi_lista_mixta)

# Eliminar y copiar elementos de una Lista
mi_lista_mixta.remove("Negro") # Elimina un elemento específico de la lista
print(mi_lista_mixta)
print(mi_lista_mixta.pop()) # Elimina el último elemento de la lista
print(mi_lista_mixta)
print(mi_lista_mixta.pop(2)) # Elimina un elemento en una posición específica de la lista
print(mi_lista_mixta)
del mi_lista_mixta[0] # Elimina un elemento en una posición específica de la lista
print(mi_lista_mixta)
mi_nueva_lista = mi_lista_mixta.copy() # Se puede copiar lista a otra lista
mi_lista_mixta.clear() # Eliminar todos los elementos de una lista
print(mi_lista_mixta)
print(mi_nueva_lista)

# Invertir la lista
mi_nueva_lista.reverse()
print(mi_nueva_lista)

# Ordenar la lista
mi_nueva_lista = [12,4,15,1,5]
print(mi_nueva_lista)
mi_nueva_lista.sort()
print(mi_nueva_lista)