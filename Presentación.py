import base64
import streamlit as st
import plotly.express as px
from PIL import Image
import webbrowser

st.set_page_config(
    page_title="SISTEMA RECOMENDADOR / MACHINE LEARNING",
    )

base="dark"

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

st.title("INVESTIGACIÓN FORMATIVA")
st.header("SISTEMA RECOMENDADOR/APLICACION EN IA")


c1,c2 = st.columns([6,4])
c1.markdown("## GRUPO C - N°2")
c1.markdown("### INTEGRANTES")
c1.markdown("#### - Apaza Valdivia, Leonel Saul ")
c1.markdown("#### - Araujo Ari, Roberto Ricardo ")
c1.markdown("#### - Hancco Huillca, Sergio David")
c1.markdown("#### - Tello Alegria, Ronald Augusto")
