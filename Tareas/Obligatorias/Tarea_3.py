# _*_ conding: utf-8 _*_

entrada = [4, 2, 3, 5, 0, 1, -1]

for indice in entrada:
    salida = ""
    if indice >= 0:
        for i in range(indice + 1):
            salida = salida + str(i) + " " 
    else:
        salida = "x"
    print salida       