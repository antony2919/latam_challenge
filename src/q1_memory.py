import pandas as pd
from typing import List, Tuple
from datetime import datetime

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
resultado = []

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Leer el archivo JSON de un dataframe de pandas
    df = pd.read_json(file_path, lines=True)

    # Convertimos la columna de fechas al formato deseado
    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'] + pd.Timedelta(hours=-5)# Convertir a la zona horaria deseada gtm - 5 Peru

    # Agregar una columna de fecha formateada
    df['formatted_date'] = df['date'].dt.date

    # Calcular el recuento de publicaciones por fecha y por usuario
    pub_por_fecha = df['formatted_date'].value_counts()
    df['username'] = df['user'].apply(lambda x: x['username'])# Usamos lambda a cada elemento de la columna 'user' para tomar cada diccionario x y extrae el valor asociado a la clave 'username'.
    pub_usuario_fecha = df.groupby(['formatted_date', 'username']).size().unstack(fill_value=0) # pivotear los nombres a columnas y contar ocurrencias, llenar con 0 si no hay ocurrencias

    # Obtener las top 10 fechas con más publicaciones
    top_fechas = pub_por_fecha.head(10).index.tolist() # Obtenemos los top10 de los indices y lo convertimos en una lista

    # Obtener el usuario con más publicaciones para cada una de las top 10 fechas
    for fecha in top_fechas:
        usuario_mas_publicaciones = pub_usuario_fecha.loc[fecha].idxmax()
        resultado.append((fecha, usuario_mas_publicaciones))
    return resultado

resultado = q1_memory(file_path)
print(resultado)
