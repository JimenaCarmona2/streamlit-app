import streamlit as st
from funciones_BD import *

def pageChurn():
    df = st.session_state["data"]
    df_churn = st.session_state["data_churn"]

    with open("app/styles/pageChurn.css") as f:
        inicio_css = f"<style>{f.read()}</style>"
        st.markdown(inicio_css, unsafe_allow_html=True)

    cont_principal = st.container()
    with cont_principal:
        filtros, kpi = st.columns([0.3, 0.7])
        with filtros:
            container_filtros = st.container(border=True)
            with container_filtros:
                st.write("Tiempo de Análisis")
                fil1, fil2 = st.columns(2)
                with fil1:
                    df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
                    df_time = df.dropna(subset=['Fecha']).copy()

                    df_time["periodo"] = df_time["Fecha"].dt.to_period("M")
                    periodos = sorted(df_time["periodo"].unique())
                    periodos_str = [str(p) for p in periodos]

                    inicio_default = periodos_str[0]
                    fin_default = periodos_str[-1]
                    
                    st.selectbox(
                        "Desde:",
                        options=periodos_str,
                        index=periodos_str.index(inicio_default),
                        key="per_inicio"
                    )
                with fil2:
                    st.selectbox(
                        "Hasta:",
                        options=periodos_str,
                        index=periodos_str.index(fin_default),
                        key="per_fin"
                    )

        with kpi:
            container_kpi = st.container()
            with container_kpi:
                datos_trnx = kpi_churn_por_nivel_de_cuenta()
                st.subheader("Cantidad de Usuarios por rangos de Transacciones")
                k1, k2, k3 = st.columns(3)
                with k1:
                    value = formato_miles(datos_trnx.get('0 - 1000', 0))
                    label = "0 - 1000"
                    #st.container(border=True).metric(label="0 - 1000", value=f"{value} usuarios")
                    st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #426eff;">
                                <div class="metric-title">{label}</div>
                                <div class="metric-value" style="color: #426eff;">{value} usuarios</div>
                                </div>
                                """, unsafe_allow_html=True)
                with k2:
                    value1 = formato_miles(datos_trnx.get('1000 - 3000', 0))
                    label = "1000 - 3000"
                    # st.container(border=True).metric(label="1000 - 3000", value=f"{value1} usuarios")
                    st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #426eff;">
                                <div class="metric-title">{label}</div>
                                <div class="metric-value" style="color: #426eff;">{value1} usuarios</div>
                                </div>
                                """, unsafe_allow_html=True)
                
    col1, col2, col3, col4 = st.columns(4)

    per_inicio = st.session_state["per_inicio"]
    per_fin = st.session_state["per_fin"]

    with col1:
        cont1 = st.container(border=True)
        fig1 = kpi_abandono_por_edad(per_inicio, per_fin)
        cont1.plotly_chart(fig1, use_container_width=True)

    with col2:
        cont5 = st.container(border=True)
        fig5 = kpi_atencion_telefonica(per_inicio, per_fin)
        cont5.plotly_chart(fig5, use_container_width=True)

    with col3:
        cont4 = st.container(border=True)
        fig4 = kpi_distribucion_horario(per_inicio, per_fin)
        cont4.plotly_chart(fig4, use_container_width=True) 
        
    with col4:
          
        cont2 = st.container(border=True)
        fig2 = kpi_motivos_de_llamada_top3(per_inicio, per_fin)
        cont2.plotly_chart(fig2, use_container_width=True)