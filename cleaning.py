def limpieza_cadenas(cadena):
    #cadena = cadena.lower()
    cadena = cadena.replace(',','')
    cadena = cadena.replace('!','')
    cadena = cadena.replace('¡','')
    cadena = cadena.replace('?','')
    cadena = cadena.replace('¿','')
    cadena = cadena.replace('#','')
    cadena = cadena.replace('&','')
    cadena = cadena.replace(':','')
    cadena = cadena.replace(';','')
    cadena = cadena.replace('\n','')
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    return cadena

def extraer_data(columna):
    import re
    # extrae los nombres de una cadena en formato json
    name = re.findall(r'"name":"([^"]*)"', columna)
    if not name:  # si no se encuentra ningún nombre, poner 'Desconocido'
        return 'Desconocido'
    else:
        return ', '.join(name)
    
def idioma_ingles(columna):
    columna.lower()
    if columna == 'en':
        return 'Es habla Inglesa'
    else:
        return 'No es habla Inglesa'
    
def calcular_nuevo_año(row):
    import pandas as pd
    if row['first_air_date_new'].date() > row['last_air_date_new'].date():
        restar_years = int(row['number_of_seasons'])
        restar_semanas = int(row['number_of_episodes'])
        return row['last_air_date_new'] - pd.DateOffset(years=restar_years, semanas=restar_semanas)
    else:
        return row['first_air_date_new']