import streamlit as st
from funciones_BD import *

def pageInfo():
    df = st.session_state["data"]
    df_churn = st.session_state["data_churn"]

    with open("app/styles/pageInfo.css") as f:
        inicio_css = f"<style>{f.read()}</style>"
        st.markdown(inicio_css, unsafe_allow_html=True)

    cont_principal = st.container()

    with cont_principal:
        col_left, col_right = st.columns([0.7, 0.347])

        with col_right:
            contFiltros = st.container(border=True)

            with contFiltros:

                contFil = st.container()

                with contFil:
                    f1, f2 = st.columns(2)
                    with f1:
                        st.markdown('<div class="form-section-title">Usuarios</div>', unsafe_allow_html=True)
                        genero = st.radio(
                            "",
                            options=["Ambos", "Mujeres", "Hombres"],
                            horizontal=True,
                            key="filtro_usuario",
                            label_visibility="collapsed"
                        )
                    with f2:
                        st.markdown('<div class="form-section-title">Calificación Call Center</div>', unsafe_allow_html=True)
                        st.radio(
                            "",
                            options=["No churn", "Churn"],
                            horizontal=True,
                            key="filtro_calificacion",
                            label_visibility="collapsed"
                        )
                st.markdown('<div class="form-section-title">Tiempo de Análisis</div>', unsafe_allow_html=True)

                df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
                df_time = df.dropna(subset=['Fecha']).copy()
                df_time["periodo"] = df_time["Fecha"].dt.to_period("M")

                periodos = sorted(df_time["periodo"].unique())
                periodos_str = [str(p) for p in periodos]

                inicio_default = periodos_str[0]
                fin_default = periodos_str[-1]

                fil1, fil2 = st.columns(2)

                with fil1:
                    st.markdown('<div class="form-section-title">Desde:</div>', unsafe_allow_html=True)
                    st.selectbox(
                        "",
                        options=periodos_str,
                        index=periodos_str.index(inicio_default),
                        key="periodo_inicio",
                        label_visibility="collapsed"
                    )
                    
                with fil2:
                    st.markdown('<div class="form-section-title">Hasta:</div>', unsafe_allow_html=True)
                    st.selectbox(
                        "",
                        options=periodos_str,
                        index=periodos_str.index(fin_default),
                        key="periodo_fin",
                        label_visibility="collapsed"
                    )

        with col_left:
            cont_left = st.container()

            with cont_left:
                col_m1, col_m2, col_m3 = st.columns(3)

                with col_m1:
                    meta1 = meta_1()
                    st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #8a66ff;">
                                <div class="metric-title">Satisfacción baja del cliente</div>
                                <div class="metric-value" style="color: #8a66ff;">{meta1}</div>
                                </div>
                                """, unsafe_allow_html=True)

                with col_m2:
                    meta2 = meta_2()
                    st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #8a66ff;">
                                <div class="metric-title">Frecuencia de uso</div>
                                <div class="metric-value" style="color: #8a66ff;">{meta2}</div>
                                </div>
                                """, unsafe_allow_html=True)

                with col_m3:
                    genero = st.session_state["filtro_usuario"]
                    if genero == "Mujeres":
                        df_gen = df[df["Gender"] == "female"]
                    elif genero == "Hombres":
                        df_gen = df[df["Gender"] == "male"]
                    else:
                        df_gen = df

                    usuarios = usuarios_totales(df_gen)

                    if genero == "Ambos":
                        label = "Usuarios Totales"
                    elif genero == "Mujeres":
                        label = "Usuarias Mujeres"
                    elif genero == "Hombres":
                        label = "Usuarios Hombres"

                    st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #426eff;">
                                <div class="metric-title">{label}</div>
                                <div class="metric-value" style="color: #426eff;">{usuarios}</div>
                                </div>
                                """, unsafe_allow_html=True)
            
            col_b1, col_b2, col_b3 = st.columns([3,2,3])

            with col_b1:
                value = formato_miles(2720000)
                st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #3ab64e;">
                                <div class="metric-title">Rendimiento</div>
                                <div class="metric-value" style="color: #3ab64e;">{value} USD</div>
                                </div>
                                """, unsafe_allow_html=True)
                
            with col_b2:
                st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #3ab64e;">
                                <div class="metric-title">Costo por cliente</div>
                                <div class="metric-value" style="color: #3ab64e;">{"1.33"} USD</div>
                                </div>
                                """, unsafe_allow_html=True)

            with col_b3:
                genero = st.session_state["filtro_usuario"]
                if genero == "Mujeres":
                    df_gen = df[df["Gender"] == "female"]
                    df_churn_gen = df_churn[df_churn["Gender"] == "female"]
                elif genero == "Hombres":
                    df_gen = df[df["Gender"] == "male"]
                    df_churn_gen = df_churn[df_churn["Gender"] == "male"]
                else:
                    df_gen = df
                    df_churn_gen = df_churn

                usuariosC = tasa_de_churn(df_gen, df_churn_gen)

                if genero == "Ambos":
                    label = "Usuarios en Churn"
                elif genero == "Mujeres":
                    label = "Usuarios en Churn (Mujeres)"
                elif genero == "Hombres":
                    label = "Usuarios en Churn (Hombres)"

                st.markdown(f"""
                                <div class="metric-card" style="border-left: 4px solid #426eff;">
                                <div class="metric-title">{label}</div>
                                <div class="metric-value" style="color: #426eff;">{usuariosC}</div>
                                </div>
                                """, unsafe_allow_html=True)


    col4_1, col6 = st.columns(2)
    with col4_1:
        periodo_inicio = st.session_state["periodo_inicio"]
        periodo_fin = st.session_state["periodo_fin"]

        container3 = st.container(border=True)
        container3.markdown('<div class="form-section-title-graph">Churn a través del Tiempo</div>', unsafe_allow_html=True)
        fig1 = churn_en_el_tiempo(periodo_inicio, periodo_fin)
        container3.plotly_chart(fig1, use_container_width=True)

    with col6:
        container7 = st.container(border=True)
        container7.markdown('<div class="form-section-title-graph">Calificación del Call Center</div>', unsafe_allow_html=True)
        filtroCC = st.session_state["filtro_calificacion"]
        genero = st.session_state["filtro_usuario"]

        if filtroCC == "No churn":
            df_call = df.copy()
        else:
            df_call = df_churn.copy()

        if genero == "Mujeres":
            df_call = df_call[df_call["Gender"] == "female"]
        elif genero == "Hombres":
            df_call = df_call[df_call["Gender"] == "male"]
            
        fig3 = calificacion_call_center(df_call)
        container7.plotly_chart(fig3, use_container_width=True)