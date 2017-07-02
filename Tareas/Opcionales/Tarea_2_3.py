# _*_ coding:utf-8 _*_

# Entrada  [1, 10, 40, 20, 2, 3, 23, 2, 90]
# Salida [1, 10, 40, 20, 2, 3, 23]
# sumar los n elementos mientras sea menor a 100

entrada = [1, 10, 40, 20, 2, 3, 23, 2, 90]
lisalida = []
suma = 0

for elemento in entrada:
    suma += elemento
    if suma <= 100:        
        lisalida.append(elemento)   

print entrada
print lisalida