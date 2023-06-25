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
def scraperbcrp(direct):

  # URL de la página web a scrapear
  user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
  url = direct
  headers={'User-Agent':user_agent,}
  request=urllib.request.Request(url,None,headers) #The assembled request
  try:
    response = urllib.request.urlopen(request)
  except:
    print('error',direct)
  data = response.read() # The data u need
  soup =  BeautifulSoup(data)
  # Obtenemos la tabla que contiene los datos
  tabla = soup.find("table", class_ = "series")

  # Obtenemos todas las filas de la tabla, excepto la primera que corresponde a los encabezados
  filas = tabla.find_all("tr")[1:]

  # Creamos una lista vacía para almacenar los datos
  datos = []

  # Recorremos las filas y obtenemos los datos de cada columna
  for fila in filas:
      celdas = fila.find_all("td")
      periodo = celdas[0].text.strip()
      valor = celdas[1].text.strip()
      datos.append((periodo, valor))


  #ultima_fila = df1.iloc[-1]
  # Obtener nombre de la serie
  nombre = soup.title.text
   # Convertimos la lista de datos en un DataFrame de Pandas
  df1 = pd.DataFrame(datos, columns=["Periodo", nombre])
  #df1 = convertir_fechas(df1, 'Periodo')

  #df1 = cortador(df1, fecha_inicio1, fecha_final2)
  #Trasponer dataframe
  transposed_df = df1.transpose()
  transposed_df.columns = transposed_df.iloc[0]
  transposed_df = transposed_df[1:]
  #Cortar elementos
  #index_to_drop = transposed_df.columns.get_loc('Ago22')

# Eliminar columnas desde la primera hasta 'Feb95'
  #df = transposed_df.drop(transposed_df.columns[:index_to_drop], axis=1)

  return df1

# Mostrar el DataFrame en Streamlit
df = scraperbcrp('https://estadisticas.bcrp.gob.pe/estadisticas/series/mensuales/resultados/PN38705PM/html/2021-06/2023-06/')
st.dataframe(df.T)

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


