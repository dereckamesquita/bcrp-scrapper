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
codediario = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2010-03-01','2023-08-05').T
st.dataframe(df)
st.altair_chart(gra_bcrp(df), use_container_width=True)
'''
codemensual = '''
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html').T
st.dataframe(df1)
st.altair_chart(gra_bcrp(df1), use_container_width=True)
'''
codeanual= '''
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2000-03-01','2023-05-05').T
st.dataframe(df2)
st.altair_chart(gra_bcrp(df2), use_container_width=True)
'''

st.title('Presentación de bcrpscrapper: Descarga fácil de datos del BCRP')
st.write('Hola, soy Dereck Amesquita')
st.markdown('[LinkedIn](https://www.linkedin.com/in/dereck-amesquita/)')
st.write('En esta aplicación, te presentaré mi librería bcrpscrapper, que te permite descargar datos del Banco Central de Reserva del Perú (BCRP) de forma sencilla y conveniente.')
st.write('A continuación, puedes ver un ejemplo de cómo utilizar la librería para descargar datos y mostrarlos en un DataFrame:')
st.subheader('Serie diaria: Tipo de cambio')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html',
                  '2010-03-01',
                  '2024-08-05').T
st.dataframe(df.tail(5))

st.altair_chart(gra_bcrp(df), use_container_width=True)
st.code(codediario, language='python')
st.subheader('Serie Mensual: Evolución del IPC')

### Serie mensual
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html').T
st.dataframe(df1.tail(6))
st.altair_chart(gra_bcrp(df1), use_container_width=True)
st.code(codemensual, language='python')

st.subheader('Serie Anual: Reservas internacionales')

### Serie anual
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2000-03-01','2023-05-05').T
st.dataframe(df2.tail(6))
st.altair_chart(gra_bcrp(df2), use_container_width=True)
st.code(codeanual, language='python')
