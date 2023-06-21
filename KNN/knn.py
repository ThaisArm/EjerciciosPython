from collections import Counter

X_train = [[1, 2], [3, 4], [5, 6], [7, 8]]
y_train = [1, 0, 1, 1]

def distancia_minkowski(x1, x2, p):
    suma = 0
    for i in range(len(x1)):
        suma += abs(x1[i] - x2[i])**p
    return suma**(1/p)

def knn(k, p, x_test):
    distancias = []
    for x_train in X_train:
        distancia = distancia_minkowski(x_test, x_train, p)
        distancias.append(distancia)

    indices_ordenados = sorted(range(len(distancias)), key=distancias.__getitem__)

    etiquetas_cercanas = []
    for i in indices_ordenados[:k]:
        etiquetas_cercanas.append(y_train[i])

    etiqueta_comun = Counter(etiquetas_cercanas).most_common(1)
    return etiqueta_comun[0][0]


X_test = [4, 5]

prediction = knn(3, 2, X_test)

print(prediction)
