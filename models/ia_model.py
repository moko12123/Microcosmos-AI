from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class IADetector:
    def __init__(self):
        self.modelo = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)
    
    def preparar_datos(self, datos):
        # Convertimos los datos en matrices de características y etiquetas
        X = []
        y = []
        
        for material in datos:
            caracteristicas = material['caracteristicas']
            frecuencia_min = caracteristicas['frecuencia'][0]
            frecuencia_max = caracteristicas['frecuencia'][1]
            longitud_onda_min = caracteristicas['longitud_onda'][0]
            longitud_onda_max = caracteristicas['longitud_onda'][1]
            
            X.append([frecuencia_min, frecuencia_max, longitud_onda_min, longitud_onda_max])
            y.append(material['nombre'])
        
        return np.array(X), np.array(y)
    
    def entrenar(self, X, y):
        # Entrenar el modelo
        self.modelo.fit(X, y)
    
    def evaluar(self, X_test, y_test):
        # Evaluar el modelo
        y_pred = self.modelo.predict(X_test)
        return accuracy_score(y_test, y_pred)
    
    def predecir(self, caracteristicas_material):
        # Predecir el material basado en sus características
        return self.modelo.predict([caracteristicas_material])[0]
