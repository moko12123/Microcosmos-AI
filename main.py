# main.py
from api_utils import obtener_datos_nasa, obtener_datos_skymap
from model import IADetector
import json

# Función principal que integra todo
def main():
    # Obtener datos de la NASA
    datos_nasa = obtener_datos_nasa()
    if datos_nasa:
        print("Datos de NASA obtenidos exitosamente:")
        print(f"Imagen: {datos_nasa['url']}")
        print(f"Descripción: {datos_nasa['explanation']}")
    else:
        print("No se pudo obtener información de la NASA.")
    
    # Cargar datos de materiales desde JSON
    with open('data/materials.json', 'r') as f:
        materiales = json.load(f)
    
    # Integrar los datos de NASA o Skymap en los materiales
    for material in materiales:
        if datos_nasa:
            material['nasa_imagen'] = datos_nasa['url']
            material['nasa_descripcion'] = datos_nasa['explanation']
    
    # Crear el modelo IA y preparar los datos
    ia = IADetector()
    X, y = ia.preparar_datos(materiales)
    ia.entrenar(X, y)

    # Realizar predicciones o análisis con el modelo
    # Aquí iría la lógica para predecir o aprender de los materiales

if __name__ == "__main__":
    main()
