#_*_ coding: utf-8 _*_
from __future__ import division

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f = f * i
    return f    

s_n = 0
signo = 0

x = int(raw_input("Valor de x: "))

for n in range(101):
    dosn = 2 * n
    signo = ((-1) ** n)
    expon = (x ** (dosn))
    cos_x = ((signo * expon) / fact(dosn) )
    s_n = s_n + cos_x

print "valor de coseno: " + str(s_n)    
