from sklearn.neural_network import MLPClassifier
from numpy.random import uniform, seed
from matplotlib.mlab import griddata
import matplotlib.pyplot as plt
import numpy as np

X = [

    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

Y = [
    0,
    1,
    1,
    0
]

# Crea un clasificador de tipo MLP
clf = MLPClassifier()

# Ajusta los datos de entramiento para aprender
clf.fit(X, Y)

# make up data.
#npts = int(raw_input('enter # of random points to plot:'))
seed(0)
npts = 100
x = uniform(0, 1, npts)
y = uniform(0, 1, npts)
z = [clf.predict([[x[i], y[i]]])[0] for i in range(npts)]

# define grid.
xi = np.linspace(0, 1, 100)
yi = np.linspace(0, 1, 100)
# grid the data.
zi = griddata(x, y, z, xi, yi, interp='linear')
# contour the gridded data, plotting dots at the nonuniform data points.
CS = plt.contour(xi, yi, zi, 15, linewidths=0.5, colors='k')
CS = plt.contourf(xi, yi, zi, 15,
                  vmax=abs(zi).max(), vmin=-abs(zi).max())
plt.colorbar()  # draw colorbar
# plot data points.
plt.scatter(x, y, marker='o', s=5, zorder=10)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.title('griddata test (%d points)' % npts)
plt.show()