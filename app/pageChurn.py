import streamlit as st
from funciones_BD import *

def pageChurn():
    df = st.session_state["data"]
    df_churn = st.session_state["data_churn"]

    cont_principal = st.container()
    with cont_principal:
        filtros, kpi = st.columns([0.3, 0.7])
        with filtros:
            container_filtros = st.container(border=True)
            with container_filtros:
                fil1, fil2 = st.columns(2)
                with fil1:
                    st.write("De:")

                    df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
                    df = df.dropna(subset=['Fecha'])

                    df["mes"] = df["Fecha"].dt.strftime("%m")
                    df["año"] = df["Fecha"].dt.strftime("%Y")

                    meses_base = sorted(df["mes"].unique().tolist())
                    año_base = sorted(df["año"].unique().tolist())

                    mes_inicio_default = meses_base[0]
                    anio_inicio_default = año_base[0]

                    mes_fin_default = meses_base[-1]
                    anio_fin_default = año_base[-1]
                    
                    st.selectbox(
                        "Mes",
                        options=meses_base,
                        index=meses_base.index(mes_inicio_default),
                        key="mes_inicio_churn"
                    )
                    st.selectbox(
                        "Año",
                        options=año_base,
                        index=año_base.index(anio_inicio_default),
                        key="año_inicio_churn"
                    )
                with fil2:
                    st.write("A:")
                    st.selectbox(
                        "Mes",
                        options=meses_base,
                        index=meses_base.index(mes_fin_default),
                        key="mes_fin_churn"
                    )
                    st.selectbox(
                        "Año",
                        options=año_base,
                        index=año_base.index(anio_fin_default),
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
        cont5 = st.container(border=True)
        fig5 = kpi_atencion_telefonica()
        cont5.plotly_chart(fig5, use_container_width=True)

    with col3:
        cont4 = st.container(border=True)
        fig4 = kpi_distribucion_horario()
        cont4.plotly_chart(fig4, use_container_width=True) 
        
    with col4:
          
        cont2 = st.container(border=True)
        fig2 = kpi_motivos_de_llamada_top3()
        cont2.plotly_chart(fig2, use_container_width=True) 