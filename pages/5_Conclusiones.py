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
background-size: 100%;
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
st.title("Conclusiones")

st.markdown("- Se logró validar los resultados ya que en la correlacion de pandas y en el codigo de correlacion grupal, al evaluar el maximo valor salio el mismo usuario.")
st.markdown("- Los resultados Validados son:")
st.markdown("                 - fairy2698@gmail.com    y   raraujoa@unsa.edu.pe    con una similitud de 0.643602")
st.markdown("     - chuaraccallo@unsa.edu.pe y meliodas7469@gmail.com  con una similitud de 0.633132")
st.markdown("- ¿Es efectivo el metodo de correlación de pearson?")
st.markdown("     En este caso donde nuestro objetivo era lograr validar los datos atravez de 2 procesos, si resulta efectivo usar la correlacion de pearson ya que para imputar los posibles valores nulos necesitabamos evaluar la relacion lineal entre las variables, ademas que este metodo es independiente de las unidades de las variables y tiene una alta exactitud cuando la muestra es grande.")
st.markdown("- Correlación de Pearson y Regresión Lineal, ¿cual es su relación?")
st.markdown("La regresion lineal nos premite obtener una recta con su ecuacion pendiente ordenada al origen de un par de datos, esta recta guarda relacion con el  coeficiente de corrrelación de pearson,ya que nos informa del grado de relación tambien entre dos variables. Si la relación es lineal perfecta, r será 1 ó -1, es decir que al graficar esa correlacion en un grafico de dispercion, si observamos que los datos forman una recta lineal con pendiente ya sea positiva o negativa obtendremos una valor de la correlacion, caso contrario si estan muy dispersos y no se aproximan a una recta lineal no hay correlacion.")
