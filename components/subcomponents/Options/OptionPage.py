import streamlit as st
from AIComponents.Crew import *
from dotenv import load_dotenv

class OptionPage:
    def __init__(self,question : str, info : str, Context, lang, crew_method):
        self.crew_method = crew_method
        self.question = question
        self.Context = Context
        self.info = info
        self.lang = lang

    def BaseIO(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("Model sedang memproses Pertanyaan!") : 
                kokoa_instance = KokoaCrew(UserQueries, Konteks, language)
                results = self.crew_method(kokoa_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    
    def DiseaseDetect(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("Model sedang memproses Pertanyaan!") : 
                kokoa_instance = KokoaCrew(UserQueries, Konteks, language)
                results = self.crew_method(kokoa_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    def StartPage(self) : 
        st.info("Silahkan memilih menu diatas untuk memulai berikut penjelasan setiap menu yang tersedia!")
        st.markdown("""##### Informasi Umum Kakao 
menyediakan Informasi yang umum mengenai berbagai hal tentang kakao        
##### Cluster Tanaman Kakao
Memberikan informasi terkait:
- Pembibitan
- Sambung Pucuk
- Sambung Samping
- Pemupukan
- Pemeliharaan
- Panen

##### Cluster Penyakit Kakao
Memberikan informasi terkait penyakit kakao dan langkah-langkah penanggulangan, pembasmian, maupun pencegahannya.

##### Cluster Pasca Panen
Memberikan informasi terkait:
- Proses Lapangan
- Distribusi
- Harga Jual
""")