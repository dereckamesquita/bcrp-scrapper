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
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Mostrar el DataFrame en Streamlit
#df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2020-03-01','2020-05-05').T
#st.dataframe(df)
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html','2020-03-01','2020-05-05').T
st.dataframe(df)
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2019-03-01','2023-05-05').T
st.dataframe(df2)


# Crear gráfico utilizando Matplotlib
import streamlit as st
import pandas as pd
import altair as alt

# Crear DataFrame de ejemplo

# Crear el gráfico de línea utilizando Altair
chart = alt.Chart(df.reset_index()).mark_line().encode(
    x='index',
    y='columna1'
)

# Configurar las etiquetas de los ejes
chart = chart.properties(
    title='Gráfico de Línea',
    xlabel='Periodo',
    ylabel='Valores'
)

# Mostrar el gráfico utilizando Streamlit
st.altair_chart(chart, use_container_width=True)








