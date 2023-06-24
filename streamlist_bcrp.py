from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
response = requests.get("https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py")
with open("bcrp_scrapper.py", "w") as file:
    file.write(response.text)
from bcrp_scrapper import *
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
data = {'Nombre': ['Juan', 'María', 'Carlos'],
        'Edad': [25, 30, 35],
        'Ciudad': ['Lima', 'Bogotá', 'Santiago']}

df = pd.DataFrame(data)

# Mostrar el DataFrame en Streamlit
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01205PM/html')

# Convertir las columnas a tipo numérico
df = df.apply(pd.to_numeric)

# Transponer el DataFrame para que los períodos sean las filas y los precios sean las columnas
df = df.T
df1 = df[::-1]

# Configurar el gráfico de línea en Streamlit
df.set_index('Periodo', inplace=True)  # Establecer la columna 'Periodo' como el índice
st.line_chart(df, use_container_width=True)  # Graficar el DataFrame con el orden correcto en el eje X
