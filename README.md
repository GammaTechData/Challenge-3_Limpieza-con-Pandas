# CHALLENGE 3 - Limpieza de datos con Pandas en Python
---
![](https://media.proprofs.com/images/QM/user_images/2503852/New%20Project%20(90)(183).jpg)

## Intro

En este challenge vamos a trabajar con un dataset con información de series de televisión en formato `.csv y .json`  💾[descarga](https://www.kaggle.com/datasets/bourdier/all-tv-series-details-dataset/download?datasetVersionNumber=4)

El dataset usado se encuentra disponible en **kaggle** y contiene información de +150.000 series de televisión.

En este [enlace](https://www.kaggle.com/datasets/bourdier/all-tv-series-details-dataset) verás la descripción de las columnas del dataset, así como su contenido.

## Instrucciones:

1. Forkea este repositorio en tu cuenta de GitHub.
2. Clona **tu** repositorio a tu local.
3. Abre el repositorio clonado y manos a la obra con el challenge! 🤓
4. Una vez finalizado recuerda hacer tu Pull Request antes del límite de la entrega para poder valorar tu trabajo.⏳

#### *Recomendaciones:*
- 💾Recuerda hacer commits con frecuencia para no perder tu progreso.
- 👀Lee bien las consignas e instrucciones.

## Requisitos:

1. Mete todas tus funciones de limpieza que realices sobre las columnas en un archivo `cleaning.py` y luego importa las funciones en el notebook.
2. Realiza un análisis exploratorio de los datos dentro del ``main.ipynb``.
3. Realiza un análisis de los datos faltantes y / 0 incorrectos y decide qué hacer con ellos, NaN, 0, etc...
4. Todas las funciones de limpieza deberán estar en el archivo `cleaning.py` y ser importadas en el notebook❗❗❗
5. Una vez tengas el dataset limpio, deberás exportarlo a un archivo `.csv` con el nombre `clean_data.csv` y subirlo a tu repositorio.
6. En el notebook deberás responder a las preguntas de la sección **Preguntas**.
7. También deberás realizar las transformaciones que se piden en la sección **Transformaciones**.
7. Además de ello, realiza un análisis exploratorio de los datos y saca tus propias conclusiones de los datos. Puedes usar gráficos, tablas, etc... para mostrar tus conclusiones.

## Preguntas:
1. ¿Cual es la serie con la duración más corta?
2. ¿Cual es la serie con la duración más larga?
3. ¿Cual es la serie con más temporadas? ¿Y la que tiene más capítulos?
4. ¿Cual es el género más estrenado para cada mes y año?
5. ¿Cual es la media de temporadas por género?
6. Listado de los 10 creadores más prolíficos.
7. ¿Que género es el que más producen estos escritores?
8. ¿Cuanto duran de media *en el aire* las series? ¿Y por género?

## Transformaciones:
1. Crea una nueva columna llamada 'media_episodios' que el número de episodios por temporada de cada serie.
2. Crea una nueva columna llamada 'habla_inglesa' que indique si la serie está en inglés o no.
3. Crear una nueva columna llamada 'produccion_europea' que indique si la serie es de producción europea o no.
4. Crea una nueva columna llamada 'mes_cancelacion' que indique el mes en el que se canceló la serie.


