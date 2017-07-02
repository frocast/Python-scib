# _*_ coding:utf-8 _*_

def menores(lista, indice):
    contador = 0
    for elemento in lista:
        if lista[indice] < elemento:
            contador += 1
    return contador        

def mayores(lista, indice):    
    contador = 0
    for elemento in lista:
        if lista[indice] > elemento:
            contador += 1
    return contador

fuerzas = [2, 3, 1, 4, 5, 8, 6, 7]

for indice in range(len(fuerzas)):    
    cadena = str(fuerzas[indice]) + " - " + str(fuerzas[0:indice]) + str(fuerzas[indice+1:len(fuerzas)]) + " : " + str(mayores(fuerzas,indice)) + "/" + str(menores(fuerzas,indice))            
    print cadena