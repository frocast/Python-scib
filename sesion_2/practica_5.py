#util.py >> def foo(), def bar()
#
# formas de importar 
# 
# CAnonica
# import util
# util.foo()
# util.bar()
# 
# por alias
# import util as u
# u.foo()
# u.bar()
# 
# por partes
# from util import foo, bar (para cargar todo *)
# bar
# foo



from math import tan
from math import pi

def are_poli(n,L):
    """ Area de poligono regualar """
    return (((L**2)*tan(pi/n))/4)*n

print are_poli(3,2)