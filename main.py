from fastapi import FastAPI
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
from unidecode import unidecode
import uvicorn
from IPython.display import display
from pandas import DataFrame
import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.openapi.utils import get_openapi

app = FastAPI()

df_peliculas = pd.read_csv('data_movies_fin.csv')
df_peliculas['id'] = df_peliculas['id'].astype(int)
df_creditos = pd.read_csv('creditos_fin.csv')
df_unido = pd.merge(df_peliculas, df_creditos, on='id')

index = 0
    
@app.get("/cantidad_filmaciones_mes/{mes}")
async def cantidad_filmaciones_mes(mes: str):
    global index
    index += 1
    # Convertir la columna "release_date" a tipo datetime si no está en ese formato
    df_unido['release_date'] = pd.to_datetime(df_unido['release_date'])
    # Filtrar los datos por el mes especificado en español
    data_filtrado = df_unido[df_unido['release_date'].dt.month_name(
        locale='es') == mes]
    # Obtener la cantidad de registros que coinciden
    cantidad = len(data_filtrado)
    mensaje = f"La cantidad de películas estrenadas en el mes es {cantidad}"
    return mensaje