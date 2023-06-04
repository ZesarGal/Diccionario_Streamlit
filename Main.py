import streamlit as st
import base64

file1_ = open("./Im1.png", "rb")


#Portada
contents1 = file1_.read()
data_url1 = base64.b64encode(contents1).decode("utf-8")
file1_.close()

import streamlit as st

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")


st.title('''Diccionario\n

            ''',)

file = open(r"path", 'rb')
contents = file.read()
data_url = base64.b64encode(contents).decode('utf-8-sig')
file.close()
st.markdown(f'<img src="data:image/gif;base64,{data_url}>',unsafe_allow_html = True)



st.subheader('''
_César Gal_
''')






