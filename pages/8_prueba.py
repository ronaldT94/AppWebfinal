import streamlit as st
url = 'https://stackoverflow.com'

st.markdown(f'''
<a href={url}><button style="background-color:GreenYellow;">Stackoverflow</button></a>
''',
unsafe_allow_html=True)
