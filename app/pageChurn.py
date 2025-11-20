import streamlit as st
from datetime import datetime

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