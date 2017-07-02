# _*_ coding: utf-8 _*_

##############################################################################################
# f0 = 0
# f1 = 1
# fn = fn-1 + fn-2 
#
#
#
#
##############################################################################################

def fib(n):
    if n >= 0 and n <= 1 :
        return n         
    else:
        return fib(n-1) + fib(n-2)        

#print fib(8)
salida = ""

entrada = int(raw_input("Valor de n: "))        

for f in range(entrada + 1):
   salida = salida + str(fib(f)) + " "

print salida   