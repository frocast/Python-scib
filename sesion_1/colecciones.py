# _*_ coding: utf-8 _*_ 
"""
 
 listas - (Arreglos lineales)
        Numeros algo en comun [] <--- Lista 
            Ejemplos
                Numeros pares 
                    pares = [2,4,6,8,"Hola",...]
                    el indice inicia desde cero
                    print pares[2]
                    pares[3] = 8
                    pares[100] = 102 <-- Error si esta fuera de lo indices <IndexError>

                    lista vacia 
                impares = [] <-- se crea una lista vacia
                Metodos 
                agregar elementos
                    append(x)   <-- Agrega un elemento al final de la lista imparares.append(1)
                    insert(i,x) <-- para agregar en un indice especifico impares.insert(2,5)
                remover elementos    
                    pop(i)      <-- quita el indice i pop(3) regresa el valor 
                    remove(x)   <-- quita el elemento con valor remove(4) quita 
                    count(x)
        Iterador - Estructura
        Interable - Ser parte de un iterador
                    rangos, colecciones y otros
        ______
no <--  |     |  --> Siguiente elemento (iterando)
        |  ?  |  
        |     |  <-- ¿Tienes otro elemento?
        -------
        iterable
iterador
___|___        
|     |
for e in iterable: e --> iterando
    bloque(e)

    funcion en python
    forma 1
        range(10) --> 0,1,2..9
    forma 2    
        range(3,7) --> 3,4,5,6,7
    forma 3
        range(1,100,2) --> 1,3,5,7,9,11 <-- Saltos de 2 

 Tuplas - (Empaquetados)
 Diccionarios - (Clave - Valor)
        ejemplos: 
            Datos de una persona
"""

a = [1,5,8,11,21,34,55,99]

#len(lista) Regresa el numero de elementos en una lista

# Recorrer lista por indice
for i in range(len(a)):
    print a[i]

for x in a:
    print x    