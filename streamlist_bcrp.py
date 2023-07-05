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

codeinversion = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
'''

codeipc = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01273PM/html',
                  '2021-08-01',
                  '2024-08-05').T
df.loc[pd.to_datetime('2023-06-01')] = 6.46 #Fuente INEI
chart = gra_bcrp_labels(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Inflación (Var % 12 meses)',
        fontSize=20))
chart
'''
code = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
'''
codediario = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2010-03-01','2023-08-05').T
gra_bcrp(df)
'''
codemensual = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html').T
gra_bcrp(df1)
'''
codeanual= '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2000-03-01','2023-05-05').T
gra_bcrp(df2)
'''

st.title('✅ Presentación de bcrpscrapper: Descarga fácil de datos del BCRP')
st.write('Hola, soy Dereck Amesquita')
st.markdown('[LinkedIn](https://www.linkedin.com/in/dereck-amesquita/)')
st.write('En esta aplicación, te presentaré mi librería bcrpscrapper, que te permite descargar datos del Banco Central de Reserva del Perú (BCRP) de forma sencilla y conveniente.')
st.subheader('Absolutamente todas las series 📊')
st.write('⭐️ No tienes que descargar nada, ni cuadernos colab, ni raros archivos. Simplemente necesitaras ejecutar un comando simple.')
st.code(code, language='python')
st.write('📌 Eso es todo, podrás acceder a cualquier serie del Banco Central para que puedas trabajarla.')
st.write('📌 Adicionalmente te presento una forma de realizar gráficos rapidamente.')
st.write('Te muestro un ejemplo para cada tipo de dato, donde te dejo los códigos necesarios para su réplica')

st.title('✅ Inversión privada continua en rojo, pero modera caida')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN02533AQ/html',
                  '2018-08-01',
                  '2024-08-05').T


df['var%'] = df.iloc[:, 0].pct_change(periods=4) * 100
df.loc[pd.to_datetime('2023-06-30')] = float (-7.41)

df = df.iloc[:, 1:]
df = df.dropna()

st.code(codeipc, language='python')
chart = gra_bcrp_labels(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Inversión Bruta - Var (12%)',
        fontSize=20))
df.index = df.index.strftime('%b %Y')
st.altair_chart(chart, use_container_width=True)
st.dataframe(df.tail(8).T)

st.title('✅ Caida de la inflación en el mes de junio')
st.write('El 01 de Julio salio el informe de precios del INEI. La sorpresa es que comunicaron que la inflación es de 6.46%.')
st.write('Una caída en la tasa de inflación no implica una disminución de los precios, pero indica que el ritmo de crecimiento de los precios se está desacelerando.')
st.write('Te dejo el link del informe y tambien los codigos para recrear el gráfico y el dataframe mediante BCRP SCRAPPER.')

st.markdown('[Informe INEI (julio)](https://m.inei.gob.pe/media/MenuRecursivo/boletines/07-informe-tecnico-variacion-de-precios-jun-2023.pdf)')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01273PM/html',
                  '2021-08-01',
                  '2024-08-05').T
df.loc[pd.to_datetime('2023-06-01')] = 6.46

st.code(codeipc, language='python')
chart = gra_bcrp_labels(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Inflación (Var % 12 meses)',
        fontSize=20))
df.index = df.index.strftime('%b %Y')
st.altair_chart(chart, use_container_width=True)
st.dataframe(df.tail(8).T)




st.title('✅ Otras pruebas de BCRP SCRAPPER')

st.subheader('Serie diaria: Tipo de cambio')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html',
                  '2010-03-01',
                  '2024-08-05').T
st.code(codediario, language='python')
st.altair_chart(gra_bcrp(df), use_container_width=True)
st.dataframe(df.tail(5))
st.subheader('Serie Mensual: Evolución del IPC')

### Serie mensual
df1 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html').T
st.code(codemensual, language='python')
st.altair_chart(gra_bcrp(df1), use_container_width=True)
st.dataframe(df1.tail(6))
st.subheader('Serie Anual: Reservas internacionales')

### Serie anual
df2 = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/anuales/resultados/PM06103MA/html','2000-03-01','2023-05-05').T
st.code(codeanual, language='python')
st.altair_chart(gra_bcrp(df2), use_container_width=True)
st.dataframe(df2.tail(6))
#https://docs.streamlit.io/library/api-reference/data/st.dataframe

