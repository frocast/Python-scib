# -*- coding:utf-8 -*-
import matplotlib.pylab as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 500)

plt.plot(x, np.sin(x), label='sin(x)', color='b')
plt.plot(x, np.cos(x), label='cos(x)', color='g')
plt.xlabel('(x)')
plt.ylabel('Funciones (x)')
plt.axis('tight')
plt.grid(color='r', linestyle='-', linewidth=0.3)
plt.legend()
plt.show()