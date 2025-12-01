import streamlit as st
from datetime import datetime
from funciones_BD import *

def pageInfo():
    df = st.session_state["data"]
    df_churn = st.session_state["data_churn"]

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
                        genero = st.radio(
                            "Usuarios",
                            options=["Ambos", "Mujeres", "Hombres"],
                            horizontal=True,
                            key="filtro_usuario"
                        )
                    with f2:
                        st.radio(
                            "Calificación Call Center",
                            options=["No churn", "Churn"],
                            horizontal=True,
                            key="filtro_calificacion"
                        )
                    st.text("Tiempo de Análisis")

                fil1, fil2 = st.columns(2)
                with fil1:
                    with st.expander("De:", expanded=False):
                        df["Fecha"] = pd.to_datetime(df["Fecha"], errors='coerce')
                        df = df.dropna(subset=['Fecha'])

                        df["mes"] = df["Fecha"].dt.strftime("%m")
                        df["año"] = df["Fecha"].dt.strftime("%Y")

                        meses_base = sorted(df["mes"].unique().tolist())
                        año_base = sorted(df["año"].unique().tolist())

                        mes_inicio_default = meses_base[0]
                        año_inicio_default = año_base[0]

                        mes_fin_default = meses_base[-1]
                        año_fin_default = año_base[-1]

                        st.selectbox(
                            "Mes",
                            options=meses_base,
                            index=meses_base.index(mes_inicio_default),
                            key="mes_inicio_churn"
                        )
                        st.selectbox(
                            "Año",
                            index=año_base.index(año_inicio_default),
                            options=año_base,
                            key="año_inicio_churn"
                        )
                    
                with fil2:
                    with st.expander("A:", expanded=False):
                        st.selectbox(
                            "Mes",
                            options=meses_base,
                            index=meses_base.index(mes_fin_default),
                            key="mes_fin_churn"
                        )
                        st.selectbox(
                            "Año",
                            options=año_base,
                            index=año_base.index(año_fin_default),
                            key="año_fin_churn"
                        )

        with col_left:
            cont_left = st.container()

            with cont_left:
                #st.write("")
                col_m1, col_m2, col_m3 = st.columns(3)

                with col_m1:
                    meta1 = meta_1()
                    st.container(border=True).metric(label="Satisfacción baja del cliente", value=meta1)
                    
                with col_m2:
                    meta2 = meta_2()
                    st.container(border=True).metric(label="Frecuencia de Uso", value=meta2)
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

                    st.container(border=True).metric(label=label, value=usuarios)
            
            col_b1, col_b2, col_b3 = st.columns([3,2,3])

            with col_b1:
                st.container(border=True).metric(label="Rendimiento", value="$8,955,000.00")
                
            with col_b2:
                st.container(border=True).metric(label="Costo por Cliente", value="$1.33")
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
                st.container(border=True).metric(label=label, value=usuariosC)


    col4_1, col6 = st.columns(2)
    with col4_1:

        container3 = st.container(border=True)
        fig1 = churn_en_el_tiempo()
        container3.plotly_chart(fig1, use_container_width=True)

    with col6:
        container7 = st.container(border=True)
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