import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Generar datos aleatorios
np.random.seed(0)
x = np.linspace(0, 10, 100)
y1 = np.random.randn(100)
y2 = np.random.randn(100)
y3 = np.random.randn(100)

# Crear la aplicación web
st.title('Gráfico con Streamlit')
st.subheader('Gráfico de ejemplo')

# Seleccionar las series a graficar
columnas = st.multiselect('Selecciona las series', ['Serie 1', 'Serie 2', 'Serie 3'])

# Graficar las series seleccionadas
if columnas:
    fig, ax = plt.subplots()
    for columna in columnas:
        if columna == 'Serie 1':
            ax.plot(x, y1, label='Serie 1')
        elif columna == 'Serie 2':
            ax.plot(x, y2, label='Serie 2')
        elif columna == 'Serie 3':
            ax.plot(x, y3, label='Serie 3')
    ax.legend()
    st.pyplot(fig)
