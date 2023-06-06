import numpy as np
import pandas as pd
import ast
import json


def limpiar_columna(list_fromColumn):
    dicc_vacio={}
    lista_vacia=[]
    lista_final=[]
    lista_temp=[]
    for iterator1 in list_fromColumn:
        if iterator1 == '[]':
            list_empty=[]
            lista_final.append(list_empty)
        else:
            #lista_vacia=ast.literal_eval(iterator1)
            lista_vacia=json.loads(iterator1)
            for i in lista_vacia:
                dicc_vacio=i
                valor_dicc=dicc_vacio["name"]
                lista_temp.append(valor_dicc)
                dicc_vacio={}

            lista_final.append(lista_temp) 
            lista_temp=[]

    return(lista_final)
#leer la data
df_tvs = pd.read_csv('datasets/tvs.csv')
#hacer copias de los df que vamos a usar
df_tvs2=df_tvs.copy()
df_tvs1=df_tvs2.copy()

#created_by
list_fromColumn=df_tvs2.created_by.to_numpy()
lista_limpia=limpiar_columna(list_fromColumn)
column_name=df_tvs2.columns[1] #[1]
df_tvs1[column_name]=lista_limpia 

#genres
list_fromColumn=df_tvs2.genres.to_numpy()
lista_limpia=limpiar_columna(list_fromColumn) 
column_name=df_tvs2.columns[3] #[3]
df_tvs1[column_name]=lista_limpia 

#production_companies
list_fromColumn=df_tvs2.production_companies.to_numpy()
lista_limpia=limpiar_columna(list_fromColumn) 
column_name=df_tvs2.columns[16] #[16]
df_tvs1[column_name]=lista_limpia 

display(df_tvs1)