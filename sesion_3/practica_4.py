import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 10)

y = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y,"r+")
plt.plot(x,y2,"g")
plt.show()