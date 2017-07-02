# _*_ coding: utf-8 _*_

# Una empresa requiere saber en que categoria estan sus clientes
#    respesto a las siguientes  categorias
#     A de 0 a 11 años 
#     B de 12 a 16 años mantenidos por papas
#     C de 17 a 24 años ninis
#     D de 24 a 31 años inicio Trabajo
#     E de otros casos Trabajo estable 

#     Crear un programa que solicite 
#     la edad y responda con la categoria 
#     en la que se encuentra la persona

edad = int(raw_input("Edad "))

if edad >= 0 and edad <= 11:
    print("A")
elif edad >= 12 and edad <= 16:
    print("B")
elif edad >= 17 and edad <= 24:
    print("C")
elif edad >= 25 and edad <= 31:
    print("D")
else:
    print("E")
                