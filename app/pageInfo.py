import streamlit as st
from datetime import datetime
from funciones_BD import *

def pageInfo():
    cont_principal = st.container()

    with cont_principal:
        col_left, col_right = st.columns([0.7, 0.347])

        with col_left:
            cont_left = st.container()

            with cont_left:
                st.write("")
                col_m1, col_m2, col_m3 = st.columns(3)

                with col_m1:
                    st.container(border=True).text("Meta 1")
                    # st.metric(label="Meta 1", value="82%")
                with col_m2:
                    st.container(border=True).text("Meta 2")
                    # st.metric(label="Meta 2", value="50%")
                with col_m3:
                    usuarios = usuarios_totales()
                    st.container(border=True).metric(label="Usuarios Totales", value=f"{usuarios}")

            col_b1, col_b2 = st.columns(2)

            with col_b1:
                dato = tasa_de_churn()
                st.container(border=True).metric(label="Usuarios en Churn", value=f"{dato}")
            with col_b2:
                st.container(border=True).text("Rendimiento")
                # st.metric(label="Rendimiento", value="$1,234,567")

        with col_right:
            contFiltros = st.container(border=True)

            with contFiltros:
                contFil = st.container()

                with contFil:
                    f1, f2 = st.columns(2)
                    with f1:
                        st.radio(
                            "Usuarios",
                            options=["Ambos", "Mujeres", "Hombres"],
                            horizontal=True
                        )
                    with f2:
                        st.radio(
                            "Calificación Call Center",
                            options=["No churn", "Churn"],
                            horizontal=True
                        )

                fil1, fil2 = st.columns(2)
                with fil1:
                    st.write("De:")
                    st.selectbox(
                        "Mes",
                        options=["01","02","03","04","05","06",
                                 "07","08","09","10","11","12"],
                        key="mes_inicio_churn"
                    )
                    st.selectbox(
                        "Año",
                        options=["2022", "2023"],
                        key="año_inicio_churn"
                    )
                with fil2:
                    st.write("A:")
                    st.selectbox(
                        "Mes",
                        options=["01","02","03","04","05","06",
                                 "07","08","09","10","11","12"],
                        key="mes_fin_churn"
                    )
                    st.selectbox(
                        "Año",
                        options=["2022", "2023"],
                        key="año_fin_churn"
                    )

    col4_1, col5, col6 = st.columns(3)
    with col4_1:

        container3 = st.container(border=True)
        fig1 = churn_en_el_tiempo()
        container3.plotly_chart(fig1, use_container_width=True)

    with col5:
        container5 = st.container(border=True)
        container5.text("Costo por cliente")
        # container5.bar_chart(
        #     {
        #         "Costo": [2, 4, 10, 8, 14, 12, 6]
        #     }
        # )

    with col6:
        container7 = st.container(border=True)
        fig3 = calificacion_call_center()
        container7.plotly_chart(fig3, use_container_width=True)