import streamlit as st
from datetime import datetime

def dashboard():

    def pageInfo():
        st.title("Información Descriptiva")
        st.write("Contenido de la página 1")
        with st.sidebar:
            st.header("Filtros")

            st.text("Tasa Churn")
            st.checkbox("Silent")
            st.checkbox("Parcial")
            st.checkbox("Complete")

            st.text("Usuarios")
            st.checkbox("Mujer")
            st.checkbox("Hombre")

            st.slider(
                "Tiempo",
                min_value = datetime(2022, 1, 1),
                max_value = datetime(2023, 12, 31),
                format="MM/YYYY"
            )

    def pageChurn():
        st.title("Análisis de Churn")
        st.write("Contenido de la página 2")
        with st.sidebar:
            st.header("Filtros")
            st.slider(
                "Tiempo",
                min_value = datetime(2022, 1, 1),
                max_value = datetime(2023, 12, 31),
                format="MM/YYYY"
            )

    def pageUsuario():
        st.title("Perfil del Usuario")
        st.write("Contenido de la página 3")
        with st.sidebar:
            st.header("Filtros")
            st.text("Segmentación del cliente")
            st.checkbox("Perfil 1")
            st.checkbox("Perfil 2")
            st.checkbox("Perfil 3")

    pages = {
        "Páginas": [
            st.Page(pageInfo, title="Información Descriptiva"),
            st.Page(pageChurn, title="Análisis de Churn"),
            st.Page(pageUsuario, title="Perfil del Usuario")
        ]
    }

    pg = st.navigation(pages, position="sidebar")
    pg.run()


