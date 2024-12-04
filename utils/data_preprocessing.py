def preprocesar_datos(materiales):
    datos_preprocesados = []
    
    for material in materiales:
        caracteristicas = material['caracteristicas']
        frecuencia_min = caracteristicas['frecuencia'][0]
        frecuencia_max = caracteristicas['frecuencia'][1]
        longitud_onda_min = caracteristicas['longitud_onda'][0]
        longitud_onda_max = caracteristicas['longitud_onda'][1]
        
        datos_preprocesados.append({
            'nombre': material['nombre'],
            'frecuencia_min': frecuencia_min,
            'frecuencia_max': frecuencia_max,
            'longitud_onda_min': longitud_onda_min,
            'longitud_onda_max': longitud_onda_max
        })
    
    return datos_preprocesados
