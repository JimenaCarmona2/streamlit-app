import streamlit as st
from datetime import datetime

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
                    st.container(border=True).metric(label="Tasa Actual de Churn", value="33.3%")

            col_b1, col_b2 = st.columns(2)

            with col_b1:
                st.container(border=True).metric(label="Usuarios Totales", value="582,345")
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
                st.markdown(
                    """
                    <style>
                    /* Código para personalizar las opciones seleccionadas en st.multiselect */
                    .st-ae .st-at button {
                        background-color: blue;
                        color: white;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
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
        container3.text("Churn en el tiempo")
        container3.line_chart(
            {
                "Tasa de Churn": [36, 35, 23, 26, 18, 17, 20,10,7,0]
            }
        )

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
        container7.text("Calificación Call Center")
        container7.bar_chart(
            {
                "Ingresos": [3, 2, 1, 4, 5]
            }
        )