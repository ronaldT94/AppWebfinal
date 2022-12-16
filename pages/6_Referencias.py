import streamlit as st
from PIL import Image
import base64
import plotly.express as px


ds = px.data.iris()

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        dat = f.read()
    return base64.b64encode(dat).decode()


img = get_img_as_base64("imagenes/image.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQs8ujv8r0jGFqrG2cYpKYhVyGtgrjhSuzW0MMePxfYqEdNb0k-U2gAXv7F-F9epEi6bZE&usqp=CAU");
background-size: 150%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img}");
background-size: 130%;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

logo = Image.open('imagenes/LOGO_UNSA.png')
with st.sidebar:
    st.image(logo)
st.title("REFERENCIAS")
st.markdown("- __Profesor de Matematicas__: `John Gabriel Muñoz Cruz` https://www.linkedin.com/in/jgmc")

st.markdown("- __Análisis de correlación__: `José Alquicira. (2017)` https://conogasi.org/articulos/analisis-de-correlacion-2/")

st.markdown("- __¿Qué es un análisis de correlación en encuestas?__: https://www.questionpro.com/blog/es/analisis-de-correlacion/")

st.markdown("- https://numpy.org/doc/stable/reference/generated/numpy.unique.html")

st.markdown("- __Convertir Array de NumPy a DataFrame de Pandas__: https://www.delftstack.com/es/howto/python-pandas/numpy-arrays-to-pandas-dataframe/")

st.markdown("- __Limpieza de datos y mapas de calor__: https://www.youtube.com/watch?v=QwgNjctlYnQ")

st.markdown("- __Coeficiente de correlacion de Pearson__: https://www.youtube.com/watch?v=1BMX762A9Dg")

st.markdown("- __Pandas DataFrame__: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html")

st.markdown("- __Funcion reshape con Numpy__: https://www.analyticslane.com/2021/04/05/numpy-la-funcion-reshape-de-numpy-con-ejemplos/")

st.markdown("- __Creación de un dataframe a partir de un array NumPy__: https://interactivechaos.com/es/manual/tutorial-de-pandas/creacion-de-un-dataframe-partir-de-un-array-numpy")

st.markdown("- __Identificación e imputación de valores perdidos en Python__: https://elmundodelosdatos.com/identificacion-valores-perdidos-python/")

st.markdown("- __Funciones de estadística matemática__: https://docs.python.org/es/3/library/statistics.html")

st.markdown("- __Regresión lineal con Python__: https://www.cienciadedatos.net/documentos/py10-regresion-lineal-python.html")
