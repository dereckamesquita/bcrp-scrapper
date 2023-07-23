# BCRP Scrapper
Este es un proyecto que realiza web scraping de datos económicos proporcionados por el Banco Central de Reserva del Perú (BCRP). El código utiliza Python y algunas librerías populares como BeautifulSoup, pandas y altair para extraer, procesar y visualizar los datos.

# Descripción
El objetivo de este proyecto es permitir a los usuarios obtener y analizar datos económicos de diferentes series proporcionadas por el BCRP. El código incluye varias funciones que permiten acceder a las series específicas y filtrar los datos según un rango de fechas definido por el usuario.

# Funcionalidades principales
bcrpscrapper(datos, fecha_inicio, fecha_final): Esta función realiza web scraping de las series económicas proporcionadas por el BCRP. Los parámetros datos, fecha_inicio y fecha_final permiten seleccionar las series específicas y filtrar los datos dentro de un rango de fechas.

scraperbcrp(direct, fecha_inicio1, fecha_final2): Esta función se encarga de extraer los datos de una serie económica específica del BCRP a partir de su URL. Convierte las fechas al formato adecuado y filtra los datos según el rango de fechas especificado.

gra_bcrp(df): Función que utiliza la librería altair para generar un gráfico de líneas a partir de un DataFrame df. El gráfico muestra la evolución de la serie a lo largo del tiempo.

gra_bcrp_labels(df): Similar a gra_bcrp, pero esta función agrega etiquetas a las líneas del gráfico para mostrar los valores correspondientes.

gra_bcrp_bar(df): Esta función genera un gráfico de barras a partir de un DataFrame df. Agrupa los datos por mes y muestra la suma de los valores para cada mes.

# Requisitos
Para ejecutar el código, se requiere tener instaladas las siguientes librerías:

requests
pandas
BeautifulSoup
altair
Uso
Para obtener datos de una serie específica, se debe proporcionar la URL correspondiente al parámetro datos de la función bcrpscrapper. También es posible filtrar los datos dentro de un rango de fechas utilizando fecha_inicio y fecha_final.

El código se ha diseñado para ser flexible y fácil de usar. Es posible agregar más funcionalidades según las necesidades específicas del usuario.

# Contribuciones
Siéntete libre de realizar contribuciones y mejoras a este proyecto. Las contribuciones son bienvenidas y pueden ser enviadas a través de pull requests.

# Notas importantes
Este proyecto está destinado únicamente con fines educativos y de aprendizaje. Se recomienda siempre revisar las políticas de uso de los datos proporcionados por el BCRP antes de utilizarlos en aplicaciones o análisis comerciales.

# Autor
Dereck Amesquita






