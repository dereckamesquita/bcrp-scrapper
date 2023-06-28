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

st.write("¡Hola", pd.__version__)

# Mostrar el DataFrame en Streamlit
#df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2020-03-01','2020-05-05').T
#st.dataframe(df)
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html','2018-03-01','2022-05-05').T
st.dataframe(df1)
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2019-03-01','2023-05-05').T
st.dataframe(df2)

import streamlit as st
import altair as alt
import pandas as pd

# Crear una nueva columna con el formato de fecha deseado
df1['Periodo'] = pd.to_datetime(df1['Periodo'])
df1['Periodo_Format'] = df1['Periodo'].dt.strftime('%b %Y')

# Crear el gráfico utilizando Altair
chart = alt.Chart(df1).mark_line().encode(
    x='Periodo:T',
    y='Índice de Precios al Consumidor (IPC):Q',
    tooltip=['Periodo_Format', 'Índice de Precios al Consumidor (IPC)']
).properties(
    width=600,
    height=400,
    title='Variación del IPC'
).interactive()

# Mostrar el gráfico utilizando Streamlit
st.altair_chart(chart)








