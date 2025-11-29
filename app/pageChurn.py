import streamlit as st
from datetime import datetime
from kpis import *

def pageChurn():
    cont_principal = st.container()
    with cont_principal:
        filtros, kpi = st.columns([0.3, 0.7])
        with filtros:
            container_filtros = st.container(border=True)
            with container_filtros:
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
        with kpi:
            container_kpi = st.container()
            with container_kpi:
                datos_trnx = kpi_churn_por_nivel_de_cuenta()
                st.subheader("Cantidad de Usuarios por rangos de Transacciones")
                k1, k2, k3 = st.columns(3)
                with k1:
                    st.container(border=True).metric(label="0 - 1000", value=f"{datos_trnx.get('0 - 1000', 0)} usuarios")
                with k2:
                    st.container(border=True).metric(label="1000 - 3000", value=f"{datos_trnx.get('1000 - 3000', 0)} usuarios")
                with k3:
                    st.container(border=True).metric(label="3000+", value=f"{datos_trnx.get('3000+', 0)} usuarios")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        cont1 = st.container(border=True)
        fig1 = kpi_abandono_por_edad()
        cont1.plotly_chart(fig1, use_container_width=True)

    with col2:
        cont2 = st.container(border=True)
        fig2 = kpi_motivos_de_llamada_top3()
        cont2.plotly_chart(fig2, use_container_width=True)

    with col3:
        cont5 = st.container(border=True)
        fig5 = kpi_atencion_telefonica()
        cont5.plotly_chart(fig5, use_container_width=True)
    
    with col4:
        cont4 = st.container(border=True)
        fig4 = kpi_distribucion_horario()
        cont4.plotly_chart(fig4, use_container_width=True)    