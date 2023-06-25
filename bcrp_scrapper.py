# -*- coding: utf-8 -*-
"""BCRP - Scrapper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CFS6qirWxo-Puqn0vkJh23uv9BW5fV8O

# BCRP Scrapper
"""

#!wget https://raw.githubusercontent.com/dereckamesquita/bcrp-scrapper/main/bcrp_scrapper.py
#from bcrp_scrapper import *

import requests
import pandas as pd
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
import urllib.request
from datetime import datetime

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
    return df_vacio

def scraperbcrp(direct,fecha_inicio1,fecha_final2):
  """
  Esta función se encarga de entrar a una serie del BCRP.
  Toma el dataframe y lo procesa en un pandas.

  Parameters:
    datos (str o list): Puede ser una lista "[]" o un string. Usa la o las URLS que te proporciona el BCRP
  Return:
    DataFrame
  Ejemplos:
  """
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
  df1 = convertir_fechas(df1, 'Periodo')

  df1 = cortador(df1, fecha_inicio1, fecha_final2)
  #Trasponer dataframe
  transposed_df = df1.transpose()
  transposed_df.columns = transposed_df.iloc[0]
  transposed_df = transposed_df[1:]
  #Cortar elementos
  #index_to_drop = transposed_df.columns.get_loc('Ago22')

# Eliminar columnas desde la primera hasta 'Feb95'
  #df = transposed_df.drop(transposed_df.columns[:index_to_drop], axis=1)

  return transposed_df
  #return nombre, ultima_fila

def cortador(df, fechainicio, fechafinal):
    fechainicio1 = datetime.strptime(fechainicio, "%Y-%m-%d")
    fechafinal1 = datetime.strptime(fechafinal, "%Y-%m-%d")
    df['Periodo'] = pd.to_datetime(df['Periodo'], format='%Y-%m-%d')
    df_filtrado = df[df['Periodo'].between(fechainicio1, fechafinal1, inclusive=True)]
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
        elif fecha[1] == 'T':
            trimestre = int(fecha[0])
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
