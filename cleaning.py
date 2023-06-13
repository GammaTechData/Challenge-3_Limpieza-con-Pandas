def librerias():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    import bokeh as bk
    return print('importado')

def extraer_diccionarios(columna):
    import re
    """Función que extrae los nombres de las compañías de una cadena en formato JSON"""
    dicc = re.findall(r'"name":"([^"]*)"', columna)
    if not dicc:  # si no se encuentra ningún nombre, poner 'Desconocido'
        return 'Desconocido'
    else:
        return ', '.join(dicc)
    
def rellenar_nombre(columna):
    return tvsc['columna'].fillna('Desconocido', inplace=True)

def reemplazar_fechas_nat(fila):
    import pandas as pd
    if pd.isna(fila['first_air_date']):
        fila['first_air_date'] = pd.to_datetime('1900-01-01')
    if pd.isna(row['last_air_date']):
        fila['last_air_date'] = pd.to_datetime('1850-01-01')
    return fila

def reemplazar_fechas_nat_coincidentes(row):
    import pandas as pd
    import numpy as np
    if (row['first_air_date'].isna()) and (row['last_air_date'].isna()):
        row['first_air_date'] = pd.to_datetime('1700-01-01')
        row['last_air_date'] = pd.to_datetime('1700-01-01')
    return row
    
def limpiar_original():
    tvs.drop(['_id', 'overview', 'tagline', 'poster_path'], axis = 1, inplace = True)
    orden_columnas = ['id', 'name', 'original_name', 'first_air_date', 'last_air_date', 'in_production', 'status', 'original_language', 'origin_country', 'number_of_episodes', 'number_of_seasons', 'created_by', 'genres', 'production_companies', 'popularity', 'vote_average', 'vote_count']
    tvs = tvs.drop(101265)
    tvs = tvs.drop(61126)
    tvs = tvs.drop(62008)
    tvs = tvs.drop(60194)
    tvs['created_by_desc'] = tvs.created_by.replace('[]', 'Desconocido')
    tvs['genres_desc'] = tvs.genres.replace('[]', 'Desconocido')
    tvs['production_companies_desc']= tvs.production_companies.replace('[]', 'Desconocido')
    tvs = tvs.drop(['created_by', 'genres', 'production_companies'], axis=1)
    tvs['created_by'] = tvs['created_by_desc'].apply(extraer_diccionarios)
    tvs['genres'] = tvs['genres_desc'].apply(extraer_diccionarios)
    tvs['production_companies'] = tvs['production_companies_desc'].apply(extraer_diccionarios)
    tvs = tvs.drop(['created_by_desc', 'genres_desc', 'production_companies_desc'], axis=1)
    tvs = tvs.reindex(columns = orden_columnas)
    mediana_episodios = tvs.number_of_episodes.median()
    tvs['number_of_episodes'].fillna(mediana_episodios, inplace=True)
    first_last_date = tvs[tvs.duplicated(subset=['first_air_date', 'last_air_date'])]
    fechas_eliminar = first_last_date[(first_last_date.number_of_episodes == 0.0) & (first_last_date.in_production == False)]
    tvs.drop(fechas_eliminar.index, inplace=True)
    first_last_date2 = tvs[tvs.duplicated(subset=['first_air_date', 'last_air_date'])]
    fechas_nan = first_last_date2[(first_last_date2.first_air_date.isna()) & (first_last_date2.last_air_date.isna()) & (first_last_date2.number_of_episodes == 0.0) & (first_last_date2.number_of_seasons == 0) & (first_last_date2.status == 'Returning Series')]
    tvs.drop(fechas_nan.index, inplace=True)
    last_false = tvs[(tvs.last_air_date.isna()) & (tvs.first_air_date.isna()) & (tvs.in_production == False) & (tvs.number_of_episodes < 5.0)]
    tvs.drop(last_false.index, inplace=True)
    tvs.name.fillna('Desconocido', inplace=True)
    tvs.original_name.fillna('Desconocido', inplace=True)
    tvs['first_air_date'] = pd.to_datetime(tvs['first_air_date'], errors='coerce')
    tvs['last_air_date'] = pd.to_datetime(tvs['last_air_date'], errors='coerce')
    tvs.drop(125986, inplace=True)
    fecha_relleno = pd.to_datetime('1900-01-01')
    tvs.first_air_date.fillna(fecha_relleno, inplace=True)
    tvs.last_air_date.fillna(fecha_relleno, inplace=True)
    cambiar_fechas_condicion = tvs[(tvs.first_air_date.isna()) & (tvs.last_air_date.isna())]
    tvs.loc[cambiar_fechas_condicion.index, ['first_air_date', 'last_air_date']] = [pd.to_datetime('1700-01-01'), pd.to_datetime('1700-01-01')]
    tvs['first_air_date'].fillna(pd.to_datetime('1900-01-01'), inplace=True)
    tvs['last_air_date'].fillna(pd.to_datetime('1850-01-01'), inplace=True)
    tvs['id'] = tvs['id'].astype('int32')
    tvs['number_of_episodes'] = tvs['number_of_episodes'].astype('float16')
    tvs['number_of_seasons'] = tvs['number_of_episodes'].astype('int32')
    tvs['vote_count'] = tvs['vote_count'].astype('int32')

    