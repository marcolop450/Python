### Strings ###

# Declaraciones de strings
mi_string = "Hola Python"
mi_otro_string = 'Hola Python'

# Longitud de un string
print(len(mi_string))
print(len(mi_otro_string))

# Concatenación de strings
print(mi_string + " " + mi_otro_string)

# Mas tipo de strings
mi_string_multilinea = "Este es un string\nmultilinea"
print(mi_string_multilinea)

mi_string_con_tab = "\tEste es un string con tabulacion"
print(mi_string_con_tab)

mi_string_con_escape = "\\t Este es un String \\ con escape"
print(mi_string_con_escape)

# Formateo de strings
name, surname, age = "Marco", "Lopez", 22
print("Mi nombre es {} {} y tengo {} años".format(name, surname, age)) # Uso de format
print("Mi nombre es %s %s y tengo %d años" %(name, surname, age)) # Uso de %s y %d
print(f"Mi nombre es {name} {surname} y tengo {age} años") # Uso de f-strings
print("Mi nombre es "+ name + " " + surname + " y tengo " + str(age) + " años") # Concatenación de strings

# Desempaquetado de strings
mi_string = "Python"
a, b, c, d, e, f = mi_string
print(a)
print(e)

# Division de strings
mi_string_dividido = mi_string[0:3]
print(mi_string_dividido)
mi_string_dividido = mi_string[1:]
print(mi_string_dividido)
mi_string_dividido = mi_string[0:6:2]
print(mi_string_dividido)
mi_string_dividido = mi_string[-2]
print(mi_string_dividido)

# Reverse de strings
mi_string_reversed = mi_string[::-1]
print(mi_string_reversed)

# Funciones de strings
print(mi_string.upper()) # Convierte a mayusculas
print(mi_string.lower()) # Convierte a minusculas
print(mi_string.upper().isupper()) # Verifica si todos los caracteres son mayusculas combinando funciones
print(mi_string.capitalize()) # Convierte la primera letra a mayuscula
print("123".isnumeric()) # Verifica si todos los caracteres son numericos
print(mi_string.swapcase()) # Intercambia mayusculas por minusculas y viceversa
print(mi_string.count("o")) # Cuenta cuantas veces aparece un caracter
print(mi_string.find("o")) # Encuentra la posición de la primera ocurrencia de un caracter
print(mi_string.replace("o", "a")) # Reemplaza un caracter por otro
print(mi_string.startswith("Py")) # Verifica si el string empieza con un caracter