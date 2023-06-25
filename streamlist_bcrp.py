
# Mostrar el DataFrame en Streamlit
df = bcrpscrapper('https://estadisticas.bcrp.gob.pe/estadisticas/series/diarias/resultados/PD04637PD/html','2020-05-01','2020-05-05')
st.dataframe(df)

# Convertir las columnas a tipo numérico
df = df.apply(pd.to_numeric)

# Transponer el DataFrame para que los períodos sean las filas y los precios sean las columnas
df = df.T
df = df[::-1]

# Convertir el índice en una columna
df['Periodo'] = df.index

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
