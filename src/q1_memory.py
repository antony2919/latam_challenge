from typing import List, Tuple
from datetime import datetime
import json

## OBJETIVO 1 ##
## Las top 10 fechas donde hay más tweets. Mencionar el usuario (username) que más publicaciones tiene por cada uno de esos días.

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Leer el contenido del fichero JSON
    with open(file_path) as contenido:  #type contenido = class '_io.TextIOWrapper'
        lineas = contenido.readlines()  #type lineas = class 'list' y contiene \n de cada linea
    lista_tweets = [json.loads(linea.rstrip()) for linea in lineas] #recorremos la lista contenido y quitamos los espacios de la derecha que pueda tener la linea y la incluimos dentro de una lista, con esto evitamos los \n de cada linea

