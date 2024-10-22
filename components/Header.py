import components.subcomponents.Logo as Img
from components.subcomponents.Logo import *
import streamlit as st
import streamlit as st
def Header() :
    Img.image(["./Image/gema.png", "./Image/pkn.png"])
    
    st.title("KAKAO AI CENTER")
    st.write("Selamat datang di Pusat AI Kakao kami siap membantu anda dengan berbagai permasalahan terkait KAKAO!")
    st.write("")