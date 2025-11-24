import streamlit as st
from datetime import datetime

def pageChurn():
        containerFiltros = st.container(border=True)
        with containerFiltros:
            st.slider(
                 "Tiempo",
                    min_value=datetime(2022, 1, 1),
                    max_value=datetime(2023, 12, 31),
                    format="MM/YYYY"
            )

        col1, col2, col3 = st.columns(3)
        with col1:
            container = st.container(border=True)
            container.text("Abandono por grupo de edad")
            container.bar_chart(
                 {
                    "18-25": 20,
                    "26-35": 30,
                    "36-45": 25,
                    "46-55": 15,
                    "56+": 10    
                 }
            )

            container1 = st.container(border=True)
            container1.text("Churn por canal de creación de la cuenta (con género)")
            container1.bar_chart(
                 {
                    "Orgánico - Mujer": [5, 10, 15, 20, 25],
                    "Orgánico - Hombre": [10, 15, 20, 25, 30],
                    "Publicidad - Mujer": [3, 6, 9, 12, 15],
                    "Publicidad - Hombre": [4, 8, 12, 16, 20]
                 }
            )

        with col2:
            container2 = st.container(border=True)
            container2.text("Motivos de llamada asociados al churn")
            container2.bar_chart(
                    {
                        "Problemas técnicos": 40,
                        "Facturación": 25,
                        "Atención al cliente": 20,
                        "Competencia": 15    
                    }
            )

            container3 = st.container(border=True)
            container3.text("Distribución de usuarios por categoría de turno")
            container3.bar_chart(
                 {
                    "Mañana": 35,
                    "Tarde": 40,
                    "Noche": 25
                 }
            )

        with col3:
            container4 = st.container(border=True)
            container4.text("Churn por nivel de cuenta vs transacciones")
            container4.bar_chart(
                 {
                    "Básica": [10, 15, 20, 25, 30],
                    "Estándar": [5, 10, 15, 20, 25],
                    "Premium": [2, 4, 6, 8, 10]
                 }
            )

            container5 = st.container(border=True)
            container5.text("Churn por canal de atención telefónica")
            container5.bar_chart(
                 {
                    "Canal A": 30,
                    "Canal B": 25,
                    "Canal C": 20,
                    "Canal D": 15,
                    "Canal E": 10
                 }
            )
