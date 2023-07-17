# -*- coding: utf-8 -*-
"""BCRP - Scrapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CFS6qirWxo-Puqn0vkJh23uv9BW5fV8O

# BCRP Scrapper
"""


import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import urllib.request
import re
from datetime import datetime
import ssl
import altair as alt
ssl._create_default_https_context = ssl._create_unverified_context
import requests
import xml.etree.ElementTree as ET
import pandas as pd

def reemplazar_mes(x):
    diccionario_meses = {
        'Ene': 1,
        'Feb': 2,
        'Mar': 3,
        'Abr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Ago': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dic': 12
    }

    return diccionario_meses.get(x)

def bcrpscrapper(datos, fecha_inicio='1900-01-01', fecha_final='2100-01-01'):
    """
    Scrapea datos del BCRP de forma libre. Esta función usa otra función principal, la cual se encarga de procesar cada+
    serie.

    Parameters:
        datos (str o list): Puede ser una lista "[]" o un string. Usa la o las URLS que te proporciona el BCRP

    Return:
        DataFrame con los

    Ejemplos:
    """
    if isinstance(datos, str): #Comprobando si es una lista o no
      datos = [datos]
    for x in range(len(datos)):
      if 'diarias' in datos[x]:
        datos[x]=str(datos[x]+'/1900-01-02/2024-06-22/')
      elif 'mensuales' in datos[x]:
        datos[x]=str(datos[x]+'/1900-1/2024-5/')
      elif 'trimestrales' in datos[x]:
        datos[x]=str(datos[x]+'/1900-1/2024-5/')
      elif 'anuales' in datos[x]:
        datos[x]=str(datos[x]+'/1900/2024/')
    df_vacio = pd.DataFrame()
    for x in datos:
      data = scraperbcrp(x,fecha_inicio,fecha_final)
      df_vacio = pd.concat([df_vacio, data])
    df_vacio=df_vacio.apply(pd.to_numeric, errors='coerce')

    return df_vacio

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def scraperbcrp(direct, fecha_inicio1, fecha_final2):
    """
    Esta función se encarga de entrar a una serie del BCRP.
    Toma el dataframe y lo procesa en un pandas.

    Parameters:
        direct (str): URL de la serie del BCRP
        fecha_inicio1 (str): Fecha de inicio en formato "YYYY-MM-DD"
        fecha_final2 (str): Fecha final en formato "YYYY-MM-DD"

    Returns:
        pd.DataFrame: DataFrame con los datos de la serie

    Ejemplos:
    """
    ####### MOTOR DE CREACIÓN (inicio) ######
    # URL de la página web a scrapear
    df1 = motorscraper(direct)
        ####### MOTOR DE CREACIÓN (Final) ######

    df2 = convertir_fechas(df1, 'Periodo')

    df2 = cortador(df2, fecha_inicio1, fecha_final2)

    # Transponer dataframe
    transposed_df = df2.transpose()
    transposed_df.columns = transposed_df.iloc[0]
    final = transposed_df[1:]

    return final

def cortador(df, fechainicio, fechafinal):
    fechainicio1 = pd.to_datetime(fechainicio)
    fechafinal1 = pd.to_datetime(fechafinal)
    df['Periodo'] = pd.to_datetime(df['Periodo']).dt.strftime('%Y-%m-%d')
    df['Periodo'] = pd.to_datetime(df['Periodo'])
    df_filtrado = df[df['Periodo'].between(fechainicio1, fechafinal1, inclusive='both')]
    return df_filtrado

#Limpieza de fechas
def convertir_fechas(df, columna):
    def ajustar_anio(anio):
        if anio <= 30:
            anio += 2000
        elif anio <= 100:
            anio += 1900
        return anio

    def convertir_fecha(fecha):
        diccionario_meses = {
            'Ene': 1,
            'Feb': 2,
            'Mar': 3,
            'Abr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Ago': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dic': 12
        }
        if len(fecha) == 7:
            dia = int(fecha[:2])
            mes = diccionario_meses.get(fecha[2:5], 1)
            anio = int(fecha[5:])
            anio = ajustar_anio(anio)
        elif fecha[0] == 'T':
            trimestre = int(fecha[1])
            anio = int(fecha[2:])
            anio = ajustar_anio(anio)
            mes = trimestre * 3
            dia = 30
        elif len(fecha) == 5:  # Meses
            mes = diccionario_meses.get(fecha[:3], 1)
            anio = int(fecha[3:])
            anio = ajustar_anio(anio)
            dia = 1
        else:  # Años
            anio = int(fecha)
            mes = 12
            dia = 31
        fecha_convertida = datetime(anio, mes, dia)
        fecha_formateada = fecha_convertida.strftime("%Y-%m-%d")  # Formato: AAAA-MM-DD
        return fecha_formateada

    df[columna] = df[columna].apply(convertir_fecha)
    return df

def motorscraper(url):
  codigo = url.split('/')[7]
  uno = url.split('/')[9]
  dos = url.split('/')[10]
  url_archivo = 'https://estadisticas.bcrp.gob.pe/estadisticas/series/api/'+codigo+'/xml/'+uno+'/'+dos+'/'
  # Realizar la solicitud GET a la URL y obtener el contenido XML
  response = requests.get(url_archivo)
  contenido_xml = response.content
  # Analizar el contenido XML
  root = ET.fromstring(contenido_xml)

# Crear listas para almacenar los datos de fecha y valor
  fechas = []
  valores = []

# Recorrer los elementos 'period' en el XML y extraer la fecha y el valor
  for period in root.iter('period'):
    fecha = period.attrib['name']
    valor = period.find('v').text
    fecha = ''.join(fecha.split('.'))
    fechas.append(fecha)
    valores.append(valor)
  config = root.find('config')
  title = config.attrib['title']
  # Crear un DataFrame de pandas con los datos
  df = pd.DataFrame({'Periodo': fechas, title: valores})
  df['Periodo'] = df['Periodo'].astype(str)
  return df

def motorscrapeobasico(direct):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = direct
    headers = {'User-Agent': user_agent}
    request = urllib.request.Request(url, None, headers)  # The assembled request
    try:
        response = urllib.request.urlopen(request)
    except:
        print('error', direct)

    data = response.read()  # The data you need
    soup = BeautifulSoup(data)

    # Obtenemos la tabla que contiene los datos
    tabla = soup.find("table", class_="series")

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

    # Obtener nombre de la serie
    nombre = soup.title.text

    # Convertir la lista de datos en un DataFrame de Pandas
    df = pd.DataFrame(datos, columns=["Periodo", nombre])
    return df
def gra_bcrp(df):
  ejex= df.index.name
  ejey= df.columns[0]
  chart = alt.Chart(df.reset_index()).mark_line().encode(
    x=ejex,
    y=ejey).properties(
    width=600,
    height=400).interactive()
  return chart



def gra_bcrp_labels(df):
    ejex = df.index.name
    ejey = df.columns[0]
    
    chart = alt.Chart(df.reset_index()).mark_line().encode(
        x=ejex,
        y=ejey
    )
    
    # Agregar etiquetas personalizadas en color blanco
    labels = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3,
        color='black'  # Cambiar el color de las etiquetas a blanco
    ).encode(
        x=ejex,
        y=ejey,
        text=alt.Text(ejey, format='.2f'),  # Etiquetas con formato de dos decimales
        color=alt.value('white')  # Especificar el color blanco de las etiquetas
    )
    
    # Combinar gráfico y etiquetas
    chart_with_labels = chart + labels
    
    return chart_with_labels.interactive()

def gra_bcrp_bar(df):
    ejex = df.index.name
    ejey = df.columns[0]
    
    # Convertir el índice al formato de fecha adecuado
    df.index = pd.to_datetime(df.index)
    
    # Agrupar los datos por mes y obtener la suma de los valores para cada mes
    df_monthly = df.resample('MS').sum()
    
    chart = alt.Chart(df_monthly.reset_index()).mark_bar().encode(
        x=alt.X(ejex, timeUnit='yearmonth', axis=alt.Axis(format='%Y-%m', title='Fecha')),
        y=ejey
    )
    
    # Agregar etiquetas personalizadas en color blanco
    labels = chart.mark_text(
        align='left',
        baseline='middle',
        dx=3,
        color='black'  # Cambiar el color de las etiquetas a blanco
    ).encode(
        x=alt.X(ejex, timeUnit='yearmonth', axis=alt.Axis(format='%Y-%m', title='Fecha')),
        y=ejey,
        text=alt.Text(ejey, format='.2f'),  # Etiquetas con formato de dos decimales
        color=alt.value('white')  # Especificar el color blanco de las etiquetas
    )
    
    # Combinar gráfico y etiquetas
    chart_with_labels = chart + labels
    
    return chart_with_labels.interactive()


