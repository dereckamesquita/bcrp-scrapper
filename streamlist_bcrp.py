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
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html')
st.dataframe(df.T)

df = df.T
fig, ax = plt.subplots()
df.plot(ax=ax)
plt.xlabel('Periodo')
plt.ylabel('IPC')
plt.title('Gráfico de IPC')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)

# Convertir las columnas a tipo numérico
df = df.apply(pd.to_numeric)

# Transponer el DataFrame para que los períodos sean las filas y los precios sean las columnas
df = df.T
df = df[::-1]
# Mostrar el DataFrame en Streamlit


# Configurar el gráfico utilizando Altair
chart = alt.Chart(df).mark_line().encode(
    x=alt.X('Periodo', sort='descending'),
    y=alt.Y('Interbancario - Compra', scale=alt.Scale(domain=[3, 4]))
)


# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)


###
line = alt.Chart(df).mark_line().encode(
    x=alt.X('Periodo', sort='descending'),
    y=alt.Y('Interbancario - Compra', scale=alt.Scale(domain=[3, 4]))
)

labels = alt.Chart(df).mark_text(align='left', baseline='middle', dx=3).encode(
    x=alt.X('Periodo', sort='descending'),
    y=alt.Y('Interbancario - Compra', scale=alt.Scale(domain=[3, 4])),
    text=alt.Text('Interbancario - Compra', format='.3f'),
    color=alt.value('white')
)



chart = line + labels

st.altair_chart(chart, use_container_width=True)

# Configurar el gráfico utilizando Altair
chart = alt.Chart(df).mark_line().encode(
    x=alt.X('Periodo', sort='descending'),
    y='Interbancario - Compra'
)

# Mostrar el gráfico en Streamlit
st.altair_chart(chart, use_container_width=True)
# Convertir el índice en una columna
df['Periodo'] = df.index


