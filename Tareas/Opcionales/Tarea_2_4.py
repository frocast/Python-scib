# _*_ coding:utf-8 _*_

entrada = [1, 3, 2, 4, 5, 2, 1, 2, 3, 2, 4, 5, 7, 6, 5, 4]
salida_1 = []
salida_2 = []

if len(entrada) % 2 == 0:
    for indice in range(0, len(entrada), 2):
        if entrada[indice] < entrada[indice + 1]:
            salida_1.append(entrada[indice])
            salida_2.append(entrada[indice + 1]) 
        else:
            salida_1.append(entrada[indice + 1])
            salida_2.append(entrada[indice]) 
            
else:
    for indice in range(0, len(entrada) - 1, 2):
        if entrada[indice] < entrada[indice + 1]:
            salida_1.append(entrada[indice])
            salida_2.append(entrada[indice + 1]) 
        else:
            salida_1.append(entrada[indice + 1])
            salida_2.append(entrada[indice]) 

print entrada            
print str(salida_1) + str(salida_2)   
