# api_utils.py
import requests

def obtener_datos_nasa():
    api_key = 'DEMO_KEY'  # Reemplaza con tu propia clave si tienes una
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + api_key
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la respuesta fue exitosa
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de NASA: {e}")
        return None

def obtener_datos_skymap():
    # Aquí iría la lógica para consultar la API de SkyMap o cualquier otra API relacionada
    pass
