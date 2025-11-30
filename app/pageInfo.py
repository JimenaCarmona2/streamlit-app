import streamlit as st
from datetime import datetime
from funciones_BD import *

def pageInfo():
    cont_principal = st.container()

    with cont_principal:
        col_left, col_right = st.columns([0.65, 0.35])

        with col_left:
            cont_left = st.container()

            with cont_left:
                st.write("")
                col_m1, col_m2, col_m3 = st.columns(3)

                with col_m1:
                    st.container(border=True).metric(label="Meta 1", value="82%")
                with col_m2:
                    st.container(border=True).metric(label="Meta 2", value="50%")
                with col_m3:
                    usuarios = usuarios_totales()
                    st.container(border=True).metric(label="Usuarios Totales", value=f"{usuarios}")

            col_b1, col_b2 = st.columns(2)

            with col_b1:
                dato = tasa_de_churn()
                st.container(border=True).metric(label="Usuarios en Churn", value=f"{dato}")
            with col_b2:
                st.container(border=True).metric(label="Rendimiento", value="$1,234,567")

        with col_right:
            contFiltros = st.container(border=True)

            with contFiltros:
                st.multiselect(
                    "Tasa de Churn",
                    options=["Silent", "Parcial", "Complete"],
                    default=["Complete"],
                )

                st.radio(
                    "Usuarios",
                    options=["Ambos", "Mujer", "Hombre"],
                    horizontal=True
                )

                st.slider(
                    "Tiempo",
                    min_value=datetime(2022, 1, 1),
                    max_value=datetime(2023, 12, 31),
                    format="MM/YYYY"
                )
    st.write("")

    col4_1, col5, col6 = st.columns(3)
    with col4_1:

        container3 = st.container(border=True)
        fig1 = churn_en_el_tiempo()
        container3.plotly_chart(fig1, use_container_width=True)

    with col5:
        container5 = st.container(border=True)
        container5.text("Costo por cliente")
        container5.bar_chart(
            {
                "Costo": [2, 4, 10, 8, 14, 12, 6]
            }
        )

    with col6:
        container7 = st.container(border=True)
        fig3 = calificacion_call_center()
        container7.plotly_chart(fig3, use_container_width=True)