from typing import List, Tuple
from datetime import timedelta,datetime
from collections import defaultdict
import json

## OBJETIVO 1 ##
## Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
resultado=[]#Lista para concatenar las tuplas (fecha,usuario mas publicaciones)
pub_por_fecha = defaultdict(int) # Diccionario para almacenar el recuento de publicaciones por fecha
pub_usuario_fecha = defaultdict(lambda: defaultdict(int))# Diccionario para almacenar el recuento de publicaciones por usuario para cada fecha

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Leer el contenido del fichero JSON
    with open(file_path) as contenido:  #type contenido = class '_io.TextIOWrapper'
        lineas = contenido.readlines()  #type lineas = class 'list' y contiene \n de cada linea
    lista_tweets = [json.loads(linea.rstrip()) for linea in lineas] #recorremos la lista contenido y quitamos los espacios de la derecha que pueda tener la linea y la incluimos dentro de una lista, con esto evitamos los \n de cada linea

    #Recorremos la lista de tweets
    for tweet in lista_tweets:
        #Obtener el contenido del diccionario con clave date
        fecha_str = tweet.get("date")
        #Convertir el GMT al pais que desee analizar o mantener en GMT = 0 como viene por defecto
        fecha_hora = datetime.fromisoformat(fecha_str)
        nueva_fecha_hora = fecha_hora + timedelta(hours=-5) #en nuestro modificamos al gmt de peru -5,o de acuerdo a lo requerido analizar.
        fecha_formateada = nueva_fecha_hora.strftime("%Y-%m-%d") #Formateamos la fecha al formato indicado
        pub_por_fecha[fecha_formateada] += 1
        pub_usuario_fecha[fecha_formateada][tweet['user']['username']] +=1

    # Obtener las top 10 fechas con más publicaciones
    top_fechas = sorted(pub_por_fecha.items(), key=lambda x: x[1], reverse=True)[:10]
    # Obtener el usuario con más publicaciones para cada una de las top 10 fechas
    for fecha, _ in top_fechas:#solo iteramos por el primer valor de la tupla
        #pub_usuario_fecha es un dictionario[ fecha ][ dictionario[usuario][conteo_publicaciones] ]
        # con la funcion max a los valores de pub_usuario_fecha(es un diccionario) tome la primera fecha del top de la iteracion hasta llegar a la decima fecha
        # en el parametro key se pone en base a que valores realizara la funcion max en este caso, asignamos pub_usuario_fecha[fecha].get a key
        # para que lo haga en base a los valores de conteo de publicaciones de los usuario
        usuario_mas_publicaciones = max(pub_usuario_fecha[fecha], key=pub_usuario_fecha[fecha].get)
        resultado.append(((datetime.strptime(fecha, "%Y-%m-%d")).date(), usuario_mas_publicaciones))# cada resultado de la fecha, usuario de mas publiciones se agregan en forma de tupla a la lista resultado

    return resultado

resultado = q1_time(file_path)
print(resultado)