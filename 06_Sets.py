### Sets ###

# Declaracion de Sets y type
mi_set = set()
print(type(mi_set))
mi_otro_set = {} # Inicialmente es un diccionario
print(type(mi_otro_set))
mi_otro_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # Pero ahora es un set
print(type(mi_otro_set))

# Sacar longitud de un set y añadir a los elementos
print(len(mi_set)) # Tamaño de un set vacío
print(len(mi_otro_set)) # Tamaño de un set con valores
print(mi_otro_set)
mi_otro_set.add(11) # Añadir un elemento al set
print(mi_otro_set)
mi_otro_set.add(11) # Aunque ya existe el elemento no se añade
print(mi_otro_set)

# !En un set no se puede acceder a los elementos con el indice debido a que set no esta ordenado!
# print(mi_otro_set[0]) # Error

# Existenia de un elemento en un set
print(11 in mi_otro_set) # Existe el elemento en el set
print(12 in mi_otro_set) # No existe el elemento en el set

# Remover un elemento de un set
mi_otro_set.remove(11) # Remover el elemento
print(mi_otro_set)

# Si hago un clear del set se elimina todos los elementos
mi_otro_set.clear()
print(mi_otro_set)

# Convertir un set a lista y viceversa
mi_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mi_set = list(mi_set)
print(mi_set[2])
print(type(mi_set))
mi_set = set(mi_set)
print(mi_set)
print(type(mi_set))

# Union de sets
mi_set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
mi_set_2 = {1, 2, 13, 14, 15, 16, 17, 18, 19, 20}
mi_union = mi_set_1.union(mi_set_2).union({"1", "2", "3"})
print(mi_union)

# Diferencia de sets
print(mi_set_1.difference(mi_set_2))