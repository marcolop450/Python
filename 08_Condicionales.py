### Condicionales ###

# Pruebas
mi_variable = False
if mi_variable:
    print("Mi variable es True")

# Uso de If
mi_condicion = 5 * 3
if mi_condicion == 10:  # Si no se pregunta si es True o False se ejecuta
    print("Se ejecuto el segundo if")

# Uso de Else
if mi_condicion > 10:  # Si no se pregunta si es True o False se ejecuta
    print("Es mayor de 10")
else:
    print("Es menor o igual de 10")


# Condiciones multiples
if mi_condicion > 10 and mi_condicion < 20:  # Si no se pregunta si es True o False se ejecuta
    print("Es mayor de 10 y menor de 20")
else:
    print("Es menor o igual de 10 o mayor de 20")

# Uso de elif
mi_condicion = 5 * 2
if mi_condicion > 10:
    print("Es mayor de 10")
elif mi_condicion < 10:
    print("Es menor de 10")
else:
    print("Es igual a 10")

# Condiciones con strings
mi_string = ""
if mi_string:
    print("La cadena es vacia") # Si la cadena esta vacia no se ejecuta el if

mi_string = "Hola"
if mi_string:
    print("La cadena contiene datos") # Pero si la cadena contiene datos se ejecuta el if

# Prueba de igualdad
if mi_string == "Hola":
    print("La cadena es igual a Hola") # Si la cadena es igual a Hola se ejecuta el if

# Uso del Not para negar una condicion T -> F y F -> T
mi_string = ""
if not mi_string:
    print("La cadena es vacia")

print("La ejecucion continua")