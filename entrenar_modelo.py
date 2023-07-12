import joblib
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from preprocesar_imagenes import imagenes_procesadas, etiquetas

def codificar_etiquetas(etiquetas):
    encoder = LabelEncoder()
    etiquetas_codificadas = encoder.fit_transform(etiquetas)
    return etiquetas_codificadas, encoder.classes_

def dividir_dataset(imagenes, etiquetas, test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(imagenes, etiquetas, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test

# Cargar las imágenes preprocesadas
imagenes_procesadas = joblib.load('imagenes_procesadas.pkl')

# Entrenar el modelo SVM
etiquetas_codificadas, clases_etiquetas = codificar_etiquetas(etiquetas)
X_train, X_test, y_train, y_test = dividir_dataset(imagenes_procesadas, etiquetas_codificadas)
modelo = SVC(kernel='linear')
modelo.fit(X_train, y_train)
precision_entrenamiento = modelo.score(X_train, y_train)
precision_testeo = modelo.score(X_test, y_test)

# Guardar el modelo entrenado y las clases de etiquetas en archivos
joblib.dump(modelo, 'modelo.pkl')
np.save('clases_etiquetas.npy', clases_etiquetas)
