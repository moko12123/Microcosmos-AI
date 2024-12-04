from utils.data_loader import cargar_datos_json
from utils.data_preprocessing import preprocesar_datos
from models.ia_model import IADetector
from utils.model_evaluation import evaluar_modelo

def main():
    # Cargar los datos de materiales
    ruta_archivo = 'data/materials.json'
    materiales = cargar_datos_json(ruta_archivo)
    
    # Preprocesar los datos
    datos_preprocesados = preprocesar_datos(materiales)
    
    # Crear y entrenar el modelo
    modelo_ia = IADetector()
    X, y = modelo_ia.preparar_datos(datos_preprocesados)
    modelo_ia.entrenar(X, y)
    
    # Evaluar el modelo
    precision = evaluar_modelo(modelo_ia.modelo, datos_preprocesados)
    print(f'Precisión del modelo: {precision * 100:.2f}%')
    
    # Hacer una predicción
    nuevas_caracteristicas = [100, 200, 1, 2]  # Ejemplo de características
    material_predicho = modelo_ia.predecir(nuevas_caracteristicas)
    print(f'El material predicho es: {material_predicho}')

if __name__ == '__main__':
    main()
