from typing import List, Tuple
import json
from collections import defaultdict
import re
import pandas as pd

## OBJETIVO 2 ##
## Los top 10 emojis más usados con su respectivo conteo. Debe incluir las siguientes funciones:

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
emojis = defaultdict(int)
patron_sep = r"\ud8" #patron para separar el contenido de cada tweet con los inicios del codigo de emoji que inician con ud8...
patron_regex = r"\\ud8\w{2}\\ud\w{3}" #patron para validar que se trata de un emoji
diccionario = {}

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON y cargar los datos en un dataFrame de Pandas
    df = pd.read_json(file_path, lines=True)
    # Iterar sobre cada tweet en el dataFrame
    for content in df['content']:
        # Buscar emojis del mensaje
        for parttwo in json.dumps(content).split(patron_sep):#Recorreriendo en las divisiones de patron de separador
            if parttwo is not None:
                emoji = patron_sep + parttwo[:8]#Agregamos el patron que se perdio al dividir en la sentencia de arriba y solo consideramos los 8 primero caracteres de segunda parte del codigo del emoji
                if re.search(patron_regex, emoji):#Validamos que cumpla el patron de un codigo de Emoji
                    emojis[emoji] += 1#Agregamos una coincidencia mas al diccionario con clave de codigo del emoji

    # Ordenar usuarios por el top 10 recuento de emojis y con items() convierte el diccionario en una lista de tuplas
    top_emojis = sorted(emojis.items(), key=lambda x: x[1], reverse=True)[:10]

    #Realizamos las lineas de abajo para contener la información en un diccionario y aplicarle json dumps para convertir en cadena para lograr representar los iconos
    for i, (emoji, cantidad) in enumerate(top_emojis, 1):#
        diccionario[f"top{i}"] = emoji
        diccionario[f"vtop{i}"] = cantidad

    diccionario_s = json.dumps(diccionario)#Convertir el dicionario en string
    diccionario_s= diccionario_s.replace("\\\\","\\") #Reemplazar el \\ a \ para que pueda representarse el emoji en el print
    diccionario_o = json.loads(diccionario_s) #convertir a diccionario python
    lista_values = list(diccionario_o.values())#convertir dict_value a una lista para poder iterar

    # Convertir una lista  a una lista de tuplas de dos valores
    lista_de_tuplas = [(lista_values[i], lista_values[i+1]) for i in range(0, len(lista_values), 2)]
    return lista_de_tuplas

resultado = q2_memory(file_path)
print(resultado)