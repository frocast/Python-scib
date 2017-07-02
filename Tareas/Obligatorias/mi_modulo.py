#_*_ coding: utf-8 _*_

# Función: contenido(nombre)
# Lee el contenido del archivo de texto plano `nombre` y devuelvelo. 
# No olvides abrir el archivo dentro de la función en modo lectura y cerrarlo antes de devolver el contenido.
# Lineas aprox. 5

# Función: colocar(nombre, contenido)
# Abre el archivo de texto plano `nombre` y escribe en el el contenido envíado como segundo parámetro.
# Lineas aprox. 5

# Función: contenido_falso(nombre, n)
# Investiga como utilizar el módulo random y randint para generar números aleatorios entre 0 y 9 inclusive. 
# Genera n números aleatorios y colocalos dentro de un archivo de texto plano usando la variable `nombre` como nombre del archivo.

# Crea un segundo archivo llamado `mi_prueba.py` con el siguiente contenido:

import random as rd

def contenido(nombre):
    archivo = open(nombre)
    texto = archivo.read()   
    archivo.close() 
    return texto

def colocar(nombre, texto):
    archivo = open(nombre, 'w+')
    archivo.write(texto)    
    archivo.close() 

def contenido_falso(nombre, n):
    archivo = open(nombre,'a')
    for i in range(0,n):
        archivo.write(str(rd.randint(0,9)))
    archivo.close()    