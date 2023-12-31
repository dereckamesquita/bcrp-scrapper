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


codepbi = '''
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01728AM/html',  
'2022-08-01', '2024-07-05').T
df.loc[pd.to_datetime('2023-05-30')] = -1.43 #Fuente INEI
df.tail(8).T
chart = gra_bcrp_bar(df)

'''
codelistas = '''
mis_variables = [
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01207PM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01129XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01130XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01138XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PD31895MM/html']
df = bcrpscrapper(mis_variables,  '2022-08-01', '2024-08-05')
'''
codeinversion = '''
!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
from bcrp_scrapper import *
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN02533AQ/html',
                  '2021-08-01',
                  '2024-08-05').T
df['Var % (12 meses)'] = df.iloc[:, 0].pct_change(periods=4) * 100 #Calcular variaciones
df.loc[pd.to_datetime('2023-06-30')] = -7.41 #Estimado segun MEF
df = df.iloc[:, 1:].dropna()
chart = gra_bcrp_labels(df)
chart 
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
########### NOTICIA

st.title('📉 La peor caída del PBI en 27 meses')
st.write('📉 En mayo, el Producto Bruto Interno (PBI) de Perú sufrió una caída del 1.43%, impactado por la disminución en pesca 🎣, industria 🏭 y sector agropecuario 🌾. \
El sector pesca tuvo la mayor contracción, con un preocupante -70.60%. \
A pesar de estos resultados, se espera una recuperación económica 📈 para finales del 2023.')
st.write('Sin embargo, alcanzar un crecimiento del 2.5% anual será un desafío, afectando los índices de pobreza 📉 y generación de empleo 👥. \
Algunos sectores como minería ⛏️, comercio 🛒 y servicios 💼 lograron crecer en mayo, ofreciendo un rayo de esperanza en medio de las dificultades.')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01728AM/html',  '2022-08-01', '2024-07-05').T
df.loc[pd.to_datetime('2023-05-30')] = -1.43 #Fuente INEI

st.dataframe(df.tail(8).T)

st.code(codepbi, language='python')
chart = gra_bcrp_bar(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Variación del PBI (Year over Year)',
        fontSize=20))
st.altair_chart(chart, use_container_width=True)
st.dataframe(df.tail(8).T)


########
st.title('🦖 Descarga masiva de datos: El verdadero fin de BCRP-SCRAPPER')
mis_variables = [
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01207PM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01129XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01130XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01138XM/html',
'https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PD31895MM/html']
df = bcrpscrapper(mis_variables,  '2022-08-01', '2024-08-05')
st.write('Antes de lanzar la beta de un pronosticador con ML. Quiero presentar la razón por la cual creé este scrapper. \
Cuando solo tenemos que acceder a una serie, podriamos pensar, ni tan necesario fue tener que usar python. \
Pero cuando necesitamos entrar a 20, 30 , 40 o 50 series, y encima cuando se repite cada cierto tiempo, ahi si se ve mejor.')
st.write('Por ello, la función "bcrpscrapper", tambien puede recibir una lista con varias series, y lo mejor de todo, te devuelve un dataframe\
con las fechas en orden.')
st.dataframe(df)
st.code(codelistas, language='python')
#############
st.title('📉 Inversión privada continua en rojo, pero modera caída')
st.write('La inversión privada continúa en terreno negativo, con una contracción del 12% en el primer trimestre, la mayor desde 2009, excluyendo la pandemia. \
Se prevé una moderación en el segundo trimestre, con una caída estimada del 7.1% (estimada por el MEF). \
Se espera una recuperación en el futuro debido a mejores expectativas y proyectos de infraestructura.')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/trimestrales/resultados/PN02533AQ/html',
                  '2021-08-01',
                  '2024-08-05').T
df['Var % (12 meses)'] = df.iloc[:, 0].pct_change(periods=4) * 100
df.loc[pd.to_datetime('2023-06-30')] = -7.41
df = df.iloc[:, 1:].dropna()

st.code(codeinversion, language='python')
chart = gra_bcrp_labels(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Inversión Bruta - Var (12%)',
        fontSize=20))
df.index = df.index.strftime('%b %Y')
st.altair_chart(chart, use_container_width=True)
st.dataframe(df.tail(8).T)
##################
st.title('✅ Caida de la inflación en el mes de junio')
st.write('El 01 de Julio salio el informe de precios del INEI. La sorpresa es que comunicaron que la inflación es de 6.46%.')
st.write('Una caída en la tasa de inflación no implica una disminución de los precios, pero indica que el ritmo de crecimiento de los precios se está desacelerando.')
st.write('Te dejo el link del informe y tambien los codigos para recrear el gráfico y el dataframe mediante BCRP SCRAPPER.')

st.markdown('[Informe INEI (julio)](https://m.inei.gob.pe/media/MenuRecursivo/boletines/07-informe-tecnico-variacion-de-precios-jun-2023.pdf)')

df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN01273PM/html',
                  '2021-08-01',
                  '2024-08-05').T
df.loc[pd.to_datetime('2023-06-01')] = 6.46
df.index = df.index.strftime('%b %Y')

st.code(codeinversion, language='python')
chart = gra_bcrp_labels(df)
chart = chart.properties(
    title=alt.TitleParams(
        text= 'Inflación (Var % 12 meses)',
        fontSize=20))
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

