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
st.dataframe(df)

# Crear el gráfico de línea
fig, ax = plt.subplots()
ax.plot(df.columns[1:], df.iloc[0, 1:])
ax.set_xlabel('Período')
ax.set_ylabel('Precio')
ax.set_title('Precio en diferentes períodos')

# Mostrar el gráfico en Streamlit
st.pyplot(fig)
