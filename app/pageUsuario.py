import streamlit as st
import pandas as pd
import joblib
import os

def pageUsuario():

    st.set_page_config(layout="wide", page_title="Dashboard Churn")

    with open("app/styles/perfil.css") as f:
        inicio_css = f"<style>{f.read()}</style>"
        st.markdown(inicio_css, unsafe_allow_html=True)


    perfil_col1, perfil_col2, perfil_col3 = st.columns(3, gap="medium")

    with perfil_col1:
        st.markdown("""
            <div class="perfil-box">
                <div class="perfil-title">Perfil 1</div>
                <div class="perfil-icon">👤</div>
                <div class="perfil-subtitle">Alto valor</div>
            </div>
        """, unsafe_allow_html=True)

    with perfil_col2:
        st.markdown("""
            <div class="perfil-box">
                <div class="perfil-title">Perfil 2</div>
                <div class="perfil-icon">👤</div>
                <div class="perfil-subtitle">Valor medio</div>
            </div>
        """, unsafe_allow_html=True)

    with perfil_col3:
        st.markdown("""
            <div class="perfil-box">
                <div class="perfil-title">Perfil 3</div>
                <div class="perfil-icon">👤</div>
                <div class="perfil-subtitle">En evaluación</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown("### Predicción en Tiempo Real")
    
    models_dir = "models"
    model_files = [f for f in os.listdir(models_dir) if f.endswith((".joblib", ".pkl"))] if os.path.exists(models_dir) else []

    if not model_files:
        st.error("No hay modelos en la carpeta /models")
    else:
        model_name = st.selectbox("Selecciona un modelo", model_files, label_visibility="collapsed")
        model_path = os.path.join(models_dir, model_name)
        try:
            model = joblib.load(model_path)
        except Exception as e:
            st.error("No se pudo cargar el modelo.")
            st.exception(e)
        else:
            col_inputs_main = st.columns(4, gap="small")
            
            with st.form("formulario"):
                # Contenedor para inputs en 4 columnas
                with st.container():
                    col1, col2, col3, col4, col5 = st.columns(5, gap="small")

                    with col1:
                        st.markdown('<div class="form-section-title">Información</div>', unsafe_allow_html=True)
                        Cat_age = st.selectbox("Edad", ['Joven Adulto', 'Adulto', 'Adulto de la Tercera Edad'], key="cat_age")
                        Gender = st.selectbox("Género", ["female", "male"], key="gender")
                        Age = st.number_input("Edad", 0, 120, 30, key="age")
                        Cat_occupation = st.selectbox("Ocupación", ['Sin actividad laboral', 'Otros/No especificado', 'Independiente/Negocio', 'Estudiante', 'Empleado(a)'], key="occupation")

                    with col2:
                        st.markdown('<div class="form-section-title">Ubicación y tipo</div>', unsafe_allow_html=True)
                        State = st.selectbox("Estado", ['VE', 'NL', 'SO', 'BC', 'EM', 'DF', 'JA', 'CM', 'AG', 'PU', 'MI', 'CL', 'HG', 'CO', 'QR', 'CH', 'SI', 'YU', 'OA', 'TL', 'CS', 'TM', 'QT', 'GT', 'BS', 'TB', 'GR', 'MO', 'SL', 'No especificó', 'DG', 'ZA'], key="state")
                        Usertype = st.selectbox("Tipo Usuario", ["HYBRID", "DIGITAL", "ANALOG"], key="usertype")
                        Qualification = st.selectbox("Nivel Tarjeta", ["1", "2", "3"], key="qualification")
                        Cat_turn = st.selectbox("Horario de contacto", ['Nocturno', 'Matutino', 'Vespertino'], key="turn")

                    with col3:
                        st.markdown('<div class="form-section-title">Transacciones</div>', unsafe_allow_html=True)
                        Evento2 = st.selectbox("Tipo de Movimiento", ['Deposito', 'Envio de Dinero', 'Compra con Tarjeta', 'Retiro', 'Compra in App'], key="evento")
                        Amount = st.number_input("Monto Total", 0.0, key="amount")
                        Trnx = st.number_input("Transacciones", 0.0, key="trnx")
                        ComoConocio = st.selectbox("Cómo nos conoció", ['No contestó', 'Facebook', 'Publicidad en la tienda DANU', 'Boca a boca (conversacion)', 'Promotor', 'Otro', 'Otras redes sociales', 'Television', 'Internet', 'Anuncios en redes sociales', 'Modulo de servicio', 'Radio', 'Periodico', 'Volante', 'Publicidad pagada en redes sociales (influencer)', 'Correo electronico', 'Sitio Web', 'Instagram', 'Twitter'], key="conocio")

                    with col4:
                        st.markdown('<div class="form-section-title">Soporte</div>', unsafe_allow_html=True)
                        Cat_motive = st.selectbox("Motivo de Contacto", ['No especificado', 'Operaciones/Transacciones', 'Consulta/Informacion', 'Acceso/Soporte tecnico', 'Fraude/Cargos no reconocidos', 'Productos/Altas-Bajas'], key="motive")
                        Canal = st.selectbox("Canal de Contacto", ['No especificó', 'Llamada', 'App Chat'], key="canal")
                        Avg_aht = st.selectbox("Duración de Llamada", ['Fuera de rango', 'Dentro de rango'], key="aht")
                        Respfcr = st.selectbox("Resolución de Llamada", ["0", "1", "2"], key="respfcr")
                        Respcsat = st.selectbox("Satisfacción en Llamada", ["1", "2", "3", "4", "5"], key="respcsat")

                    with col5:
                        st.markdown("<div style='margin-top: 55px;'>", unsafe_allow_html=True)

                        enviar = st.form_submit_button("PREDECIR CHURN", use_container_width=True)
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

                            if pred == 0:
                                result_class = "result-no-churn"
                                icon = """
                                <svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" fill="white" viewBox="0 0 24 24">
                                <path d="M12 .587l3.668 7.568L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.593z"/>
                                </svg>
                                """
                                mensaje = "CLIENTE SEGURO"
                                recommendation = "Bajo riesgo de churn. Cliente estable con buena retención esperada."
                            else:
                                result_class = "result-churn"
                                icon = """
                                <svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" fill="white" viewBox="0 0 24 24">
                                <path d="M1 21h22L12 2 1 21zm12-3h-2v2h2v-2zm0-6h-2v5h2v-5z"/>
                                </svg>
                                """
                                mensaje = "ALERTA: ALTO RIESGO"
                                recommendation = "Se recomienda estrategia de retención inmediata."


                            st.markdown(f'<div class="result-box {result_class}" style="height: 320px;"><div class="result-icon">{icon}</div><div class="result-message">{mensaje}</div><div class="result-prob">{prob:.1%}</div><div class="result-recommendation">{recommendation}</div></div>', unsafe_allow_html=True)
                        else:
                           st.markdown('''
                                <div class="result-box result-waiting" style="height: 320px;">
                                    <div class="result-icon">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 50 50" fill="white">
                                        <path opacity="0.2" d="M25 5a20 20 0 1 0 20 20A20.023 20.023 0 0 0 25 5zm0 36a16 16 0 1 1 16-16 16.019 16.019 0 0 1-16 16z"/>
                                        <path d="M25 0v10a15 15 0 1 1 -15 15H0a25 25 0 1 0 25-25z">
                                            <animateTransform attributeType="xml"
                                            attributeName="transform"
                                            type="rotate"
                                            from="0 25 25"
                                            to="360 25 25"
                                            dur="1s"
                                            repeatCount="indefinite"/>
                                        </path>
                                        </svg>
                                    </div>
                                    <div class="result-message">Ingresa los datos</div>
                                    <div style="font-size: 12px; margin-top: 18px; opacity: 0.9; font-weight: 500; text-align: center; line-height: 1.5;">
                                        Completa el formulario y haz clic en <b>PREDECIR CHURN</b>
                                    </div>
                                </div>
                            ''', unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)



                st.markdown("")
                

            
                

if __name__ == "__main__":
    pageUsuario()