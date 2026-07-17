### Tuplas ####

# Declaracion  y creacion
mi_tupla = tuple()
mi_otra_tupla = ()

# Tupla cargada y Tipo de dato
mi_tupla = (22, 1.85, "Marco", 'Lopez')
print(mi_tupla)
print(type(mi_tupla))

# Acceder elementos de una Tupla
print(mi_tupla[0])
print(mi_tupla[-1])

# Funciones para Tupla
print(mi_tupla.count(22))
print(mi_tupla.index(22))

# No se puede modificar
# mi_tupla[1] = 1.80 

# Concatenar tuplas
mi_otra_tupla = (4,2.5,"Marcol")
mi_tupla_concatenado = mi_tupla + mi_otra_tupla
print(mi_tupla_concatenado)
print(mi_tupla_concatenado[3:6])

# Tupla a Lista y viceversa
mi_tupla = list(mi_tupla)
print(type(mi_tupla))
mi_tupla[3] = "Marco"
mi_tupla.insert(1, "Juan")
mi_tupla = tuple(mi_tupla)
print(mi_tupla)
print(type(mi_tupla))

# Usar Del en una Tupla lo eliminaa de forma general
del mi_tupla
# print(mi_tupla) NameError: name 'mi_tupla' is not defined