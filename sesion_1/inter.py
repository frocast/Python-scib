# Crear un programa que solicite un intervalo [a,b] y tambien solicite
# un intervalo x y determine si x esta dentro o fuera del intervalo

# algoritmo 
# paso 1 
#   pedir a
# paso 2
#   pedir b
# paso 3
#   si x <= a y x >= b
#       imprimir dentro
#   caso contrario 
#       imprime fuera   

inferior = int(raw_input("Intervalo Inferior "))
superior = int(raw_input("Intervalo Superior "))
x = int(raw_input("Valor x "))

if inferior < superior or (type(inferior) == "str" and type(superior) == "str" and type(x) == "str"):  
    if x >= inferior and x <= superior:
        print("Dentro")
    else:
        print("Fuera")
else:
    print("El intervalo superior debe ser mayor al inferior")
