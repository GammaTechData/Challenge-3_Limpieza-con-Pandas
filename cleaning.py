import pandas as pd
import re
import json

def limpiar_creador(row):
    try:
        cadena = row["created_by"]
        lista_creadores = json.loads(cadena)
        nombres_creadores = [creador["name"] for creador in lista_creadores]
        if nombres_creadores:
            return ", ".join(nombres_creadores)
        else:
            return "Sin creador especificado"
    except:
        return "Sin creador especificado"

def limpiar_genero(row):
    try:
        cadena = row["genres"]
        lista_generos = json.loads(cadena)
        nombres_genero = [genero["name"] for genero in lista_generos]
        if nombres_genero:
            return ", ".join(nombres_genero)
        else:
            return "Sin género"
    except:
        return "Sin género"
    
def limpiar_productora(row):
    try:
        cadena = row["production_companies"]
        lista_productoras = json.loads(cadena)
        nombres_productora = [productora["name"] for productora in lista_productoras]
        if nombres_productora:
            return ", ".join(nombres_productora)
        else:
            return "Productora independiente"
    except:
        return "Productora independiente"


def borrar_columna(df, columna):
    if columna in df.columns:
        df.drop(columna, axis=1, inplace=True)
        print(f"La columna '{columna}' se ha eliminado del DataFrame.")
    else:
        print(f"La columna '{columna}' no existe en el DataFrame.")

def limpiar_filas_nan(dataframe, columna):
    dataframe.dropna(subset=[columna], inplace=True)

def reemplazar_nan(dataframe, columna, valor_reemplazo):
    dataframe[columna].fillna(valor_reemplazo, inplace=True)
    
