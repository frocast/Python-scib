import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi)
a = 0.3
r = 2 * a * np.sin(theta) * np.cos(theta)
fig = plt.figure()
ax = fig.add_subplot(111, projection = 'polar')
ax.plot(theta, r)
plt.show()