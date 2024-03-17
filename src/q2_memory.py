from typing import List, Tuple
import json
from collections import defaultdict
import re

## OBJETIVO 2 ##
## Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
emojis = defaultdict(int)
patron_sep = r"\ud8"
patron_regex = r"\\ud8\w{2}\\ud\w{3}"
diccionario = {}

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as contenido:  #type contenido = class '_io.TextIOWrapper'
        lineas = contenido.readlines()  #type lineas = class 'list' y contiene \n de cada linea
    lista_tweets = [json.loads(linea.rstrip()) for linea in lineas] #recorremos la lista contenido y quitamos los espacios de la derecha que pueda tener la linea y la incluimos dentro de una lista, con esto evitamos los \n de cada linea

    for tweet in lista_tweets:#Recorriendo los tweet de la lista de tweets
        content = tweet.get("content")#
        # Buscar emojis del mensaje
        for parttwo in json.dumps(content).split(patron_sep):#Recorreriendo en las divisiones de patron de separador
            if parttwo is not None:
                emoji = patron_sep + parttwo[:8]#Agregamos el patron que se perdio al dividir en la sentencia de arriba y solo consideramos los 8 primero caracteres de segunda parte del codigo del emoji
                if re.search(patron_regex, emoji):#Validamos que cumpla el patron de un codigo de Emoji
                    emojis[emoji] += 1#Agregamos una coincidencia mas al diccionario con clave de codigo del emoji

    # Ordenar usuarios por el top 10 recuento de emojis y con items() convierte el diccionario en una lista de tuplas
    top_emojis = sorted(emojis.items(), key=lambda x: x[1], reverse=True)[:10]