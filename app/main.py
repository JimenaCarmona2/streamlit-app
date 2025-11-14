import streamlit as st
import pandas as pd
import os

import model_loader
import utils

st.set_page_config(page_title="Mi App Streamlit - ML", layout="wide")

st.title("App Streamlit con carga de modelo")

st.sidebar.header("Carga de archivos")
model_file = st.sidebar.file_uploader("Sube tu modelo (.pkl .joblib .sav)", type=["pkl","joblib","sav","jl"], accept_multiple_files=False)

csv_file = st.sidebar.file_uploader("(Opcional) Sube un CSV con datos para predecir", type=["csv"]) 

if model_file is not None:
    try:
        # guardamos en /models
        saved_path = model_loader.save_uploaded_model(model_file, dest_dir=os.path.join("..","models"))
        st.sidebar.success(f"Modelo guardado en: {saved_path}")
        model = model_loader.load_model(saved_path)
        st.sidebar.success("Modelo cargado correctamente")

        if csv_file is not None:
            df = pd.read_csv(csv_file)
            st.write("Datos cargados:")
            st.dataframe(df.head())

            if st.button("Realizar predicción"):
                try:
                    preds = utils.predict(model, df)
                    st.write("Predicciones:")
                    df_res = df.copy()
                    df_res["prediction"] = preds
                    st.dataframe(df_res.head(50))
                    csv = df_res.to_csv(index=False).encode("utf-8")
                    st.download_button("Descargar resultados (CSV)", data=csv, file_name="predicciones.csv")
                except Exception as e:
                    st.error(f"Error al predecir: {e}")
        else:
            st.info("Sube un CSV con las muestras para predecir o modifica `app/utils.py` para entrada manual.")

    except Exception as e:
        st.error(f"No se pudo cargar el modelo: {e}")
else:
    st.info("Sube un modelo en la barra lateral para empezar.")

st.markdown("---")
st.markdown("Nota: por seguridad, no cargues modelos no confiables. El proceso de unpickling puede ejecutar código arbitario.")

# --- Enlace / navegación rápida a la página de ejemplo extra ---
st.markdown("---")
st.subheader("Navegación")
st.write("Accede rápidamente a la página de ejemplo extra creada en `app/pages/example_extra.py`.")

try:
    if st.button("Ir a la página de ejemplo"):
        # El nombre de la página suele ser el título derivado del archivo.
        # Probamos con el nombre habitual "Example Extra". Si tu Streamlit muestra otro nombre
        # en el menú 'Pages', cámbialo aquí por el nombre exacto.
        st.experimental_set_query_params(page="Example Extra")
        st.experimental_rerun()
except Exception:
    st.info("Tu versión de Streamlit podría no soportar navegación programática. Usa el menú 'Pages' en la barra lateral para abrir la página 'Página de ejemplo extra'.")
