import streamlit as st
from datetime import datetime

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