import streamlit as st
import pandas as pd
import joblib
import os

def pageUsuario():
    st.title("Predicción de Churn")

    models_dir = "models"
    model_files = [f for f in os.listdir(models_dir) if f.endswith((".joblib",".pkl"))]

    if not model_files:
        st.error("No hay modelos en la carpeta /models")
        return

    model_name = st.selectbox("Selecciona un modelo", model_files)
    model_path = os.path.join(models_dir, model_name)
    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error("No se pudo cargar el modelo por un error inesperado.")
        st.exception(e)
        return

    st.success(f"Modelo cargado: {model_name}")

    with st.form("form"):
        Cat_age = st.selectbox("Categoría edad", ['Joven Adulto', 'Adulto', 'Adulto de la Tercera Edad'])
        Usertype = st.selectbox("Tipo usuario", ["HYBRID","DIGITAL","ANALOG"])
        Gender = st.selectbox("Género", ["female", "male"])
        Age = st.number_input("Edad", 0, 120, 30)

        Evento2 = st.selectbox("Evento2", ['Deposito', 'Envio de Dinero', 'Compra con Tarjeta', 'Retiro', 'Compra in App'])
        Amount = st.number_input("Monto total", 0.0)
        Trnx = st.number_input("Transacciones", 0.0)

        Cat_motive = st.selectbox("Motivo", ['No especificado', 'Operaciones/Transacciones', 'Consulta/Informacion', 'Acceso/Soporte tecnico', 'Fraude/Cargos no reconocidos', 'Productos/Altas-Bajas'])
        ComoConocio = st.selectbox("Cómo conoció", ['No contestó', 'Facebook', 'Publicidad en la tienda DANU', 'Boca a boca (conversacion)', 'Promotor', 'Otro','Otras redes sociales', 'Television', 'Internet', 'Anuncios en redes sociales', 'Modulo de servicio', 'Radio', 'Periodico', 'Volante', 'Publicidad pagada en redes sociales (influencer)', 'Correo electronico', 'Sitio Web', 'Instagram', 'Twitter'])
        Avg_aht = st.selectbox("AHT", ['Fuera de rango', 'Dentro de rango'])
        Respfcr = st.selectbox("Resolución", ["0", "1", "2"])
        Canal = st.selectbox("Canal contacto", ['No especificó', 'LLamada', 'App Chat'])
        Respcsat = st.selectbox("Satisfacción", ["1","2","3","4","5"])

        Qualification = st.selectbox("Nivel de tarjeta", ["1", "2", "3"])
        Cat_turn = st.selectbox("Turno", ['Nocturno', 'Matutino', 'Vespertino'])
        State = st.selectbox("Estado", ['VE', 'NL', 'SO', 'BC', 'EM', 'DF', 'JA', 'CM', 'AG', 'PU', 'MI','CL', 'HG', 'CO', 'QR', 'CH', 'SI', 'YU', 'OA', 'TL', 'CS', 'TM','QT', 'GT', 'BS', 'TB', 'GR', 'MO', 'SL', 'No especificó', 'DG','ZA'])
        Cat_occupation = st.selectbox("Ocupación", ['Sin actividad laboral', 'Otros/No especificado', 'Independiente/Negocio', 'Estudiante', 'Empleado(a)'])
        
        enviar = st.form_submit_button("Predecir")

    if enviar:
        df = pd.DataFrame([{
            "Cat_age": Cat_age,
            "Usertype": Usertype,
            "Gender": Gender,
            "Age": Age,
            "Evento2": Evento2,
            "Amount": Amount,
            "Trnx": Trnx,
            "Cat_motive": Cat_motive,
            "Por_que_medio_se_enter_de_nosotros": ComoConocio,
            "Avg_aht": Avg_aht,
            "Respfcr": Respfcr,
            "Por_que_canal_nos_esta_contactando": Canal,
            "Respcsat": Respcsat,
            "Qualification": Qualification,
            "Cat_turn": Cat_turn,
            "State": State,
            "Cat_occupation": Cat_occupation
        }])

        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        st.subheader("Resultados")
        st.write(f"**Predicción:** {pred}")
        st.write(f"**Probabilidad de churn:** {prob:.3f}")
        if pred == 1:
            st.warning("El cliente tiene alta probabilidad de churn.")
        else:
            st.success("El cliente tiene baja probabilidad de churn.")
