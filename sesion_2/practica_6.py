# r/w/a 
# lectura
# escritura
# escritura desdel el final

# 1 abrir archivo
f = open("ruta archivo.txt","r")

# 2 Extraer el contenido

contenido =  f.read()

# escritura
f.write("Hola mundo \n Otra linea ")

# 2.- REcuperar el archivo linea por linea

for linea in f:
    print linea

# cerrar el archivo

f.close()    