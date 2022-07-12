import numpy as np
import streamlit as st
from keras.models import load_model
import app1
import app2
import app4
import app5
import app3
PAGES = {
    "Malaria Detection":app1 ,
    "Mental Health": app2 ,
    "Cancer Disease":app3 ,
    "Covid19": app4 ,
    "Mask Detection": app5

}
st.sidebar.title('StayHealthy ')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
st.sidebar.header('About Me & this project')
st.sidebar.write('Hi! I am Uma kadam from IIIT Guwahati')

st.sidebar.write("[Linkedin](https://www.linkedin.com/in/uma-kadam-7885341b0/)")
st.sidebar.write("[Github](https://github.com/umak1106)")

