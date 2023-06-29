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
from datetime import datetime
import bs4
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
st.title('Presentación de bcrpscrapper: Descarga fácil de datos del BCRP')
st.write('¡Bienvenido a mi aplicación de Streamlit!')
st.write('En esta aplicación, te presentaré mi librería bcrpscrapper, que te permite descargar datos del Banco Central de Reserva del Perú (BCRP) de forma sencilla y conveniente.')
st.write('A continuación, puedes ver un ejemplo de cómo utilizar la librería para descargar datos y mostrarlos en un DataFrame:')

st.write("¡Hola", pd.__version__, ' ', bs4.__version__)
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2010-03-01','2023-08-05').T
st.dataframe(df)

def gra_bcrp(df):
  ejex= df.index.name
  ejey= df.columns[0]
  chart = alt.Chart(df.reset_index()).mark_line().encode(
    x=ejex,
    y=ejey).interactive()

  return chart

st.altair_chart(gra_bcrp(df), use_container_width=True)

