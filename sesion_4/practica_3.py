# _*_ coding:utf-8 _*_

# Tecnicas de Clasificación 
# Clasificación
# Regresión
# Clúster

# clúster evita un experto

# matriz de entrenamiento x (conjunto de datos de entranamiento) training set

# matriz de prueba test set

# sklearn

# preguntas            godin dark    
# 1.- Escuchar musica   si    si 
# 2.- Ver Tele          si    no
# is a starbuks         si    no
# Conocer gente         no    no

from sklearn.neural_network import MLPClassifier

# Otaku: 1
# Godinez: 2
# Darks: 3

def rol(categoria):
    if categoria == 1:
        return "Otaku"
    elif categoria == 2:
        return "Godinez"
    elif categoria == 3:
        return "Dark"
    else:
        return "Sin categoria"
            
        

X = [
    [1, 1, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 1]
]

Y = [
    1,
    2,
    3,
    2,
    3,
    2,
    1,
    3,
    2,
    3,
    3,
    2,
    3,
    2,
    3,
    3,
    1,
    1,
    2,
    1,
    2,
    3
]

# print len(X), len(Y)

# Crea un clasificador de tipo MLP
clf = MLPClassifier()

# Ajusta los datos de entramiento para aprender
clf.fit(X, Y)

# En base a su aprendizaje predecimos
# que pasa con el X = [1, 0, 1, 1]
# (La respuesta fue [2] - Godinez)

# print clf.predict([1, 0, 1, 1])

T = [
    ([1, 0, 0, 0], 3),
    ([1, 0, 1, 0], 2),
    ([1, 1, 0, 0], 1),
    ([1, 1, 0, 0], 1),
    ([1, 0, 1, 0], 3),
    ([1, 0, 1, 1], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 0, 1], 3),
    ([1, 0, 0, 0], 1),
    ([1, 1, 0, 0], 2),
    ([1, 0, 0, 0], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 0, 0], 3),
    ([1, 1, 1, 1], 2),
    ([1, 0, 1, 1], 2),
    ([1, 0, 1, 1], 2),
    ([1, 1, 1, 1], 2),
    ([1, 1, 1, 1], 1),
    ([1, 0, 1, 1], 2),
    ([1, 0, 0, 0], 3),
    ([1, 0, 0, 0], 1),
]

for (x, y) in T:
    print "Real: %s" %(rol(y)) 
    #print "Computado: %s" %(rol(clf.predict(x)))
    print "Computado: %s" %(rol(clf.predict([x])))[0]
