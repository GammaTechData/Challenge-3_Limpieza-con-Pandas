def crear_columnas_por_el_primeiro_elemento_coma(df):
    opciones = df.columns
    columna = input(f'escribe la columna que vaya aplicar la funcion: /n {opciones}')
    nueva_columna = input('escribre nombre de la nueva columna')
    df[nueva_columna] = df[columna].str.split(',').apply(lambda x: x[0] if len(x) > 1 else 'desconocido')
    df[nueva_columna]   
def crear_columnas_por_el_segundo_elemento_coma(df):
    opciones = df.columns
    columna = input(f'escribe la columna que vaya aplicar la funcion: /n {opciones}')
    nueva_columna = input('escribre nombre de la nueva columna')
    df[nueva_columna] = df[columna].str.split(',').apply(lambda x: x[1] if len(x) > 1 else 'desconocido')
    df[nueva_columna]
def crear_columnas_por_el_primeiro_elemento_dos_puntos(df):
    opciones = df.columns
    columna = input(f'escribe la columna que vaya aplicar la funcion: /n {opciones}')
    nueva_columna = input('escribre nombre de la nueva columna')
    df[nueva_columna] = df[columna].str.split(':').apply(lambda x: x[0] if len(x) > 1 else 'desconocido')
    df[nueva_columna]
def crear_columnas_por_el_segundo_elemento_dos_puntos(df):
    opciones = df.columns
    columna = input(f'escribe la columna que vaya aplicar la funcion: /n {opciones}')
    nueva_columna = input('escribre nombre de la nueva columna')
    df[nueva_columna] = df[columna].str.split(':').apply(lambda x: x[1] if len(x) > 1 else 'desconocido')
    df[nueva_columna]
def extraer_nombres(nombres_str):
    import re
    """Función que extrae los nombres de las compañías de una cadena en formato JSON"""
    nombres = re.findall(r'"name":"([^"]*)"', nombres_str)
    if not nombres:  # si no se encuentra ningún nombre, poner 'Desconocido'
        return 'Desconocido'
    else:
        return ', '.join(nombres)
def genero_mas_repetido(lista):
    generos = {}
    for genero in lista:
        if genero in generos:
            generos[genero] += 1
        else:
            generos[genero] = 1
    return max(generos, key=generos.get)