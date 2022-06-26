#Library imports
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
st.sidebar.write('Hi! I am Uma kadam from IIIT Guwahati and Stay healthy won under the category Most Technically difficult Hack in Hackbytes. from'
                 ' 160+ participants hosted on Devpost')

if st.sidebar.button(' Go to Devpost ') :
    webbrowser.open_new_tab('https://devpost.com/software/stay-healthy-suc1ki')

if st.sidebar.button(' Go to Github ') :
    webbrowser.open_new_tab('https://github.com/umak1106')

if st.sidebar.button(' Go to Linkedin ') :
    webbrowser.open_new_tab('https://www.linkedin.com/in/uma-kadam-7885341b0/')


