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

code = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
'''
codefind = '''
bcrp_find('Reservas internacionales', fre = 'D')
'''
codere = '''
df = bcrpscrapper('PD04650MD').T
'''
st.title('✅ Presentación de bcrpscrapper 2.0: Descarga fácil de datos del BCRP')
st.write('Hola, soy Dereck Amesquita')
st.markdown('[LinkedIn](https://www.linkedin.com/in/dereck-amesquita/)')
st.write('En esta aplicación, te presentaré mi librería bcrpscrapper, que te permite descargar datos del Banco Central de Reserva del Perú (BCRP) de forma sencilla y conveniente.')
st.subheader('Absolutamente todas las series 📊')
st.write('⭐️ No tienes que descargar nada, ni cuadernos colab, ni raros archivos. Simplemente necesitaras ejecutar un comando simple.')
st.code(code, language='python')
st.write('📌 Eso es todo, podrás acceder a cualquier serie del Banco Central para que puedas trabajarla.')

#####
st.title('📌 Nueva función: bcrp_find')

st.write("¡Tenemos una función poderosa para ti! Con `bcrp_find`, podrás obtener el código único de una serie económica y las fechas sobre la última actualización de dicha serie.")

st.write("¿Cómo usarlo? Es muy sencillo:")
st.write("1. Ingresa una palabra clave relacionada con el tema económico de tu interés.")
st.write("2. La función buscará en nuestra base de datos y te mostrará los resultados que coincidan con tu búsqueda.")
st.write("3. Descubre el código único de la serie y las fechas más recientes sobre su última actualización.")

st.write("Además, si necesitas datos con una frecuencia específica, como mensuales, trimestrales o anuales, simplemente especifica la frecuencia y `bcrp_find` te proporcionará los datos deseados.")

st.write("¡Haz tus análisis económicos de manera más eficiente con BCRP Scrapper y esta nueva función! Descubre información relevante y toma decisiones informadas con confianza.")
st.write('Te muestro como usarla. No solo obtendras el código unico, tambien las fechas sobre la ultima actualización de la serie.')
st.code(codefind, language='python')
st.dataframe(bcrp_find('Reservas internacionales', fre = 'D'))
######
st.title('📌 Ahora basta con el código de la serie')
st.write('Suponiendo que quieres ver las Reservas Internacionales Netas, tomaras el codigo "PD04650MD".')
df = bcrpscrapper('PD04650MD').T
st.dataframe(df.head(10))




