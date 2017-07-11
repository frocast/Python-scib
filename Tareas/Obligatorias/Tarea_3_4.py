from sklearn.neural_network import MLPClassifier

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

# En base a su aprendizaje predecimos
# que pasa con el X = [1, 0, 1, 1]
# (La respuesta fue [2] - Godinez)

# print clf.predict([1, 0, 1, 1])

print clf.predict([0, 1])
