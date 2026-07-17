# Variables
mi_variable_string = "My Variable"
print(mi_variable_string)

mi_variable_int = 5
print(mi_variable_int)
print(type(mi_variable_int))

mi_int_to_string = str(mi_variable_int)
print(mi_int_to_string)
print(type(mi_int_to_string))

mi_variable_float = 5.5
print(mi_variable_float)

mi_variable_bool = True
print(mi_variable_bool)

# Print puede imprimir varias variables a la vez}
# A la vez la coma sirve para concatenar variables de diferentes tipos
print(mi_variable_string, mi_variable_int)
print("Este es el valor de mi boolean:", mi_variable_bool)
# Algunas Funciones del Sistema
print(len(mi_variable_string))

# Variables en una sola linea
# ! Cuidado con abusar de esta sintaxis ¡
name, surname, alias, age = "Marco", "Lopez",'Kakis', 22
print("Me llamo", name, surname, "y mi alias es", alias, "y tengo", age, "años")

# Inputs
'''
name = input("Cual es tu nombre?: ")
age = input("Cual es tu edad?: ")
print("Hola",name)
print("Tu edad es", age)
'''
# Cambiamos su tipo
name = 43
age = "Kakis"
print(name)
print(age)

# ¿Forzamos el tipo de dato?
address: str = "Calle 123"
address = 32
print(type(address))