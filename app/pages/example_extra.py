import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Página de ejemplo", layout="centered")

st.title("Página de ejemplo extra")
st.write("Esta es una página de ejemplo que puedes usar como plantilla para nuevas páginas.")

st.markdown("---")

n = st.slider("Número de filas de ejemplo", min_value=5, max_value=500, value=50)

if st.button("Generar datos de ejemplo"):
    df = pd.DataFrame({
        "x": np.arange(n),
        "y": np.random.randn(n).cumsum(),
        "label": np.random.choice(["A","B","C"], size=n)
    })
    st.subheader("Gráfico de series de ejemplo")
    st.line_chart(df.set_index("x")["y"]) 

    st.subheader("Tabla de ejemplo (primeras filas)")
    st.dataframe(df.head(50))

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Descargar CSV de ejemplo", data=csv, file_name="ejemplo.csv")
else:
    st.info("Pulsa 'Generar datos de ejemplo' para ver la demo.")

st.markdown("---")
st.write("Consejo: copia este archivo a `app/pages/nueva_pagina.py` y edítalo para crear más páginas.")
