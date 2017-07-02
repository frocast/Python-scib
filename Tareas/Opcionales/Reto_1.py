
a = [1, 2, 3, 4, 5, 6, 5, 4, 7, 6, 5, 4, 2, 1, 1, 2, 5, 6, 5, 5, 5, 8, 9, 10]

numero = int(raw_input("Elemento a Eliminar: "))

print "Existen " + str(a.count(numero)) + " con el valor: " + str(numero) 
print "Antes: " + str(a)

for indice in range(a.count(numero)):
    a.remove(numero)

print "Despues: " + str(a)    
