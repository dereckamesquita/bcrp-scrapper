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
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2019-03-01','2023-05-05').T
st.dataframe(df1)

import streamlit as st
import altair as alt
import pandas as pd

# Crear una nueva columna con el formato de fecha deseado

import streamlit as st
import altair as alt
import pandas as pd

# Crear una nueva columna con el formato de fecha deseado
df1['Periodo'] = df1.index
df1['Periodo_Format'] = df1['Periodo'].dt.strftime('%b %Y')

# Crear el gráfico utilizando Altair
chart = alt.Chart(df1).mark_line().encode(
    x=alt.X('Periodo:T', title='Periodo'),
    y=alt.Y('Índice de Precios al Consumidor (IPC):Q', title='Índice de Precios al Consumidor (IPC)'),
    tooltip=['Periodo_Format', df1.columns[0]]
).properties(
    width=600,
    height=400,
    title='Variación del IPC'
).interactive()

# Añadir etiquetas a los puntos de datos
labels = alt.Chart(df1).mark_text(
    align='center',
    baseline='middle',
    dx=5,  # Desplazamiento horizontal de las etiquetas
    dy=-5,
    color='white'# Desplazamiento vertical de las etiquetas
).encode(
    x=alt.X('Periodo:T'),
    y=alt.Y('Índice de Precios al Consumidor (IPC):Q'),
    text='Índice de Precios al Consumidor (IPC):Q'
)

# Mostrar el gráfico y las etiquetas utilizando Streamlit
st.altair_chart(chart + labels)


# Crear el gráfico utilizando Altair
chart = alt.Chart(df1).mark_line().encode(
    x=alt.X('Periodo:T', title='Periodo'),
    y=alt.Y('Datos:Q', title='Datos'),
    tooltip=['Periodo', 'Datos']
).properties(
    width=600,
    height=400,
    title='Gráfico de Ejemplo'
).interactive()

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)





