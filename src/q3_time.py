from typing import List, Tuple
import json
from collections import defaultdict

## OBJETIVO 3 ##
## El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno  de ellos.

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
menciones = defaultdict(int)

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    with open(file_path) as contenido:  #type contenido = class '_io.TextIOWrapper'
        lineas = contenido.readlines()  #type lineas = class 'list' y contiene \n de cada linea
    lista_tweets = [json.loads(linea.rstrip()) for linea in lineas] #recorremos la lista contenido y quitamos los espacios de la derecha que pueda tener la linea y la incluimos dentro de una lista, con esto evitamos los \n de cada linea

    for tweet in lista_tweets:#Recorrido de la lista de tweets
        content = tweet.get("content")#Extraemos de cada tweet el diccionario con clave content
        # Buscar menciones de usuarios (@username)
        for mencion in content.split():# dividimos la cadena de content por espacios ya que entre mencion y mencion hay un espacio
            if mencion.startswith('@'): #validamos que la cadena empieze con @
                usuario = mencion[1:]#quitamos el @ del usuario
                menciones[usuario] += 1#Agregamos una coincidencia mas al diccionario con clave de usuario

    # Ordenar usuarios por el top 10 recuento de menciones y con items() convierte el diccionario en una lista de tuplas
    top_usuarios = sorted(menciones.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_usuarios

resultado = q3_memory(file_path)
print(resultado)