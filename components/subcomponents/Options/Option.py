import streamlit as st
from AIComponents.Crew import *
from dotenv import load_dotenv

def Base() :
    UserQueries = st.text_input("hi")
    submit = st.button("Tanyakan !")
    if  submit and UserQueries != "":
        st.write('**Your Query:**')
        st.write(f"> {UserQueries}")
        st.write("Model is processing the answer, please wait...")

        CacaoSupportServiceCrew = Crew(UserQueries).BaseCrew

        results = CacaoSupportServiceCrew.kickoff()
        st.success("Here are the results:")
        st.markdown(results)
    elif submit and UserQueries == "":
        st.warning("Please enter a query to get started.")