import streamlit as st
from pageInfo import pageInfo
from pageChurn import pageChurn
from pageUsuario import pageUsuario

def dashboard():

    st.logo("app/img/logo.png")

    pages = {
        "Páginas": [
            st.Page(pageInfo, title="Información Descriptiva"),
            st.Page(pageChurn, title="Análisis de Churn"),
            st.Page(pageUsuario, title="Perfil del Usuario")
        ]
    }

    pg = st.navigation(pages, position="sidebar")
    pg.run()
