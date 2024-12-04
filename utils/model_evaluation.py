from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def evaluar_modelo(modelo, datos):
    # Dividir los datos en conjunto de entrenamiento y prueba
    X = [material[1:] for material in datos]
    y = [material[0] for material in datos]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Entrenar el modelo
    modelo.fit(X_train, y_train)
    
    # Evaluar el modelo
    y_pred = modelo.predict(X_test)
    return accuracy_score(y_test, y_pred)
