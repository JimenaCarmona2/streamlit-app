import streamlit as st
from datetime import datetime
from kpis import *

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
            fig = kpi_abandono_por_edad()
            container.plotly_chart(fig)

        with col2:
            container2 = st.container(border=True)
            container2.text("Motivos de llamada previo al churn")
            fig2 = kpi_motivos_de_llamada_previo_al_churn()
            container2.plotly_chart(fig2)

            container3 = st.container(border=True)
            container3.text("Distribución de usuarios por categoría de turno")
            fig4 = kpi_distribucion_horario()
            container3.plotly_chart(fig4)

        with col3:
            container4 = st.container(border=True)
            container4.text("Churn por nivel de cuenta vs transacciones")
            fig3 = kpi_churn_por_nivel_de_cuenta()
            container4.plotly_chart(fig3)

            container5 = st.container(border=True)
            container5.text("Churn por canal de atención telefónica")
            fig5 = kpi_atencion_telefonica()
            container5.plotly_chart(fig5)
