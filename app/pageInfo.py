import streamlit as st
from datetime import datetime

def pageInfo():
    st.subheader("Alertas")

    with st.sidebar:
        st.header("Filtros")

        st.text("Tasa Churn")
        st.checkbox("Silent")
        st.checkbox("Parcial")
        st.checkbox("Complete")

        st.text("Usuarios")
        st.checkbox("Mujer")
        st.checkbox("Hombre")

        st.slider(
            "Tiempo",
            min_value = datetime(2022, 1, 1),
            max_value = datetime(2023, 12, 31),
            format="MM/YYYY"
        )
    
    col1, col2 = st.columns(2)

    with col1:
        container = st.container(border=True)
        container.metric(label= "Meta 1", value="82%", delta="+5%")

    with col2:
        container1 = st.container(border=True)
        container1.metric(label= "Meta 2", value="50%", delta="+10%")

    st.subheader("Dashboard")

    col3, col4, col5 = st.columns(3)
    with col3:
        container2 = st.container(border=True)
        container2.metric(label= "Tasa Actual de Churn", value="33.3%")

        container3 = st.container(border=True)
        container3.text("Churn en el tiempo")
        container3.line_chart(
            {
                "Tasa de Churn": [36, 35, 23, 26, 18, 17, 20,10,7,0]
            }
        )

    with col4:
        container4 = st.container(border=True)
        container4.metric(label= "Usuarios Totales", value="872,546")

        container5 = st.container(border=True)
        container5.text("Costo por cliente")
        container5.bar_chart(
            {
                "Costo": [2, 4, 10, 8, 14, 12, 6]
            }
        )

    with col5:
        container6 = st.container(border=True)
        container6.metric(label= "Rendimiento", value="$2,345,678")

        container7 = st.container(border=True)
        container7.text("Calificación Call Center")
        container7.bar_chart(
            {
                "Ingresos": [3, 2, 1, 4, 5]
            }
        )
