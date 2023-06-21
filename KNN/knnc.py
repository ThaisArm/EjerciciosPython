from collections import Counter
import math

"""DATASET: IRIS
  4 atributos, todos en cm: longitud del sépalo, anchura del sépalo, longitud del pétalo, ancho de pétalo
  3 clases: "Iris-setosa" es 1, "Iris-versicolor" es 2, "Iris-virginica" es 3
"""

X_train = []
y_train = []

with open("KNN/irisdataset.data", "r") as file:
    for line in file:
        line = line.strip().split(",")
        x = list(map(float, line[:-1])) 
        y = int(line[-1])  
        X_train.append(x)
        y_train.append(y)

def distancia_minkowski(x1, x2, p):
    suma = 0
    for i in range(len(x1)):
        suma += abs(x1[i] - x2[i])**p
    return suma**(1/p)

def knn(p, x_test):
    N = len(X_train)
    k = int(math.log(N))
    distancias = []
    for x_train in X_train:
        distancia = distancia_minkowski(x_test, x_train, p)
        distancias.append(distancia)

    indices_ordenados = sorted(range(len(distancias)), key=distancias.__getitem__)

    etiquetas_cercanas = []
    for i in indices_ordenados[:k]:
        etiquetas_cercanas.append(y_train[i])

    etiquetas = Counter(etiquetas_cercanas)
    probabilidades = {etiqueta: count / k for etiqueta, count in etiquetas.items()}

    return probabilidades

X_test = X_test = [5.4,3.9,1.7,0.5]

prediction = knn(2, X_test)

print(prediction)
