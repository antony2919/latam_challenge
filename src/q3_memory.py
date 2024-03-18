from typing import List, Tuple
import pandas as pd
from collections import defaultdict

file_path = 'C:\\Users\\anton\\Downloads\\tweets\\farmers-protest-tweets-2021-2-4.json'
# Crear una lista para almacenar las menciones de usuarios
menciones = defaultdict(int)

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Leer el archivo JSON y cargar los datos en un DataFrame de Pandas
    df = pd.read_json(file_path, lines=True)
    # Iterar sobre cada tweet en el DataFrame
    for content in df['content']:
        # Buscar menciones de usuarios (@username)
        for mencion in content.split():# dividimos la cadena de content por espacios ya que entre mencion y mencion hay un espacio
            if mencion.startswith('@'): #validamos que la cadena empieze con @
                usuario = mencion[1:] #quitamos el @ del usuario
                menciones[usuario] += 1 #Agregamos una coincidencia mas al diccionario con clave de usuario

    top_usuarios = sorted(menciones.items(), key=lambda x: x[1], reverse=True)[:10]
    return top_usuarios

resultado= q3_memory(file_path)
print(resultado)