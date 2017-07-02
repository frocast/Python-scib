#_*_ coding: utf-8 _*_
# Algoritmo 
# Solcitar n
# crear una lista vacia dos_tres
# para i en el rango de 1 a n inclusive
# si i % 2 es ceroo i % 3 es cero
# agregar i a la lista dos_tres
# imprimir la lista dos_tres 


n = int(raw_input("Valor de n, debe ser mayor que cero: "))

dos_tres = []

for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0:
        dos_tres.append(i)    

print dos_tres