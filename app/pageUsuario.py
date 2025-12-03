import streamlit as st
import pandas as pd
import joblib
import os

def pageUsuario():
    st.set_page_config(layout="wide", page_title="Dashboard Churn")

    # Inyectar CSS
    with open("app/styles/perfil.css") as f:
        inicio_css = f"<style>{f.read()}</style>"
        st.markdown(inicio_css, unsafe_allow_html=True)

    if "perfil_index" not in st.session_state:
        st.session_state.perfil_index = 0

    perfiles = [
        {
            "titulo": "Perfil 1",
            "descripcion": "Transacciones bajas; no contestó canal.",
            "churn": "91.99%",
            "riesgo": "Riesgo muy alto",
            "color": "#dc2626"
        },
        {
            "titulo": "Perfil 2",
            "descripcion": "Transacciones bajas-moderadas; calificación de llamada baja; no contestó canal.",
            "churn": "87.06%",
            "riesgo": "Riesgo alto",
            "color": "#dc2626"
        },
        {
            "titulo": "Perfil 3",
            "descripcion": "Transacciones moderadas; calificación de llamada alta; no contestó canal.",
            "churn": "81.08%",
            "riesgo": "Riesgo alto",
            "color": "#f97316"
        },
        {
            "titulo": "Perfil 4",
            "descripcion": "Transacciones moderadas; no contestó canal.",
            "churn": "75.87%",
            "riesgo": "Riesgo elevado",
            "color": "#f97316"
        },
        {
            "titulo": "Perfil 5",
            "descripcion": "Transacciones muy bajas; calificación de llamada baja; sí contestó canal.",
            "churn": "74.29%",
            "riesgo": "Riesgo elevado",
            "color": "#facc15"
        },
        {
            "titulo": "Perfil 6",
            "descripcion": "Transacciones media-altas; no contestó canal.",
            "churn": "67.22%",
            "riesgo": "Riesgo medio-alto",
            "color": "#facc15"
        },
        {
            "titulo": "Perfil 7",
            "descripcion": "Transacciones altas; sin motivos de Operaciones/Transacciones; no contestó canal.",
            "churn": "60.10%",
            "riesgo": "Riesgo medio",
            "color": "#eab308"
        },
        {
            "titulo": "Perfil 8",
            "descripcion": "Transacciones bajas-moderadas; calificación de llamada baja; sí contestó canal.",
            "churn": "60.02%",
            "riesgo": "Riesgo medio-alto",
            "color": "#eab308"
        },
        {
            "titulo": "Perfil 9",
            "descripcion": "Transacciones muy bajas; calificación de llamada alta; sí contestó canal.",
            "churn": "60.02%",
            "riesgo": "Riesgo medio",
            "color": "#eab308"
        },
    ]

    def get_index(i):
        return i % len(perfiles)

    idx = st.session_state.perfil_index
    visible = [
        perfiles[(idx + 0) % len(perfiles)],
        perfiles[(idx + 1) % len(perfiles)],
        perfiles[(idx + 2) % len(perfiles)]
    ]

    cols = st.columns([1, 3, 3, 3, 1], gap="small")

    # Mostrar las tarjetas
    for i in range(3):
        with cols[i + 1]:
            perfil = perfiles[get_index(idx + i)]
            st.markdown(f"""
                <div class="perfil-box uniform-card" style="border-left: 3px solid {perfil['color']}">
                    <div class="perfil-title">{perfil['titulo']}</div>
                    <div class="perfil-subtitle" style="font-size: 13px; opacity: 0.9; margin-bottom: 6px;">{perfil['descripcion']}</div>
                    <div class="perfil-churn" style="color: {perfil['color']}; font-size: 28px; font-weight: bold;">{perfil['churn']}</div>
                    <div class="perfil-subtitle" style="font-size: 14px; opacity: 0.85; margin-top: 6px;">{perfil['riesgo']}</div>
                </div>
            """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<div style='text-align: center; margin-top: -10px;'>", unsafe_allow_html=True)
        flechas = st.columns([5, 1, 1, 5])

        GRUPO_TAM = 3
        TOTAL = len(perfiles)
        MAX_INDEX = TOTAL - GRUPO_TAM

        if "perfil_index" not in st.session_state:
            st.session_state.perfil_index = 0

        with flechas[1]:
            if st.button("◀", use_container_width=True):
                st.session_state.perfil_index = (st.session_state.perfil_index - GRUPO_TAM) % TOTAL
                # Redondear hacia abajo al múltiplo más cercano
                st.session_state.perfil_index -= st.session_state.perfil_index % GRUPO_TAM

        with flechas[2]:
            if st.button("▶", use_container_width=True):
                st.session_state.perfil_index = (st.session_state.perfil_index + GRUPO_TAM) % TOTAL
                st.session_state.perfil_index -= st.session_state.perfil_index % GRUPO_TAM

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### Predicción en Tiempo Real")

    def safe_index(lista, valor_default, valor_usuario):
        return lista.index(valor_usuario) if valor_usuario in lista else lista.index(valor_default)

    # === Usuarios Mock-up para autollenado ===
    usuarios_prueba = {
         "Ninguno": {
            "Cat_age": "Joven Adulto",
            "Gender": "female",
            "Age": 30,
            "Cat_occupation": "Sin actividad laboral",
            "State": "VE",
            "Usertype": "HYBRID",
            "Qualification": "1",
            "Cat_turn": "Nocturno",
            "Evento2": "Deposito",
            "Amount": 0.0,
            "Trnx": 0.0,
            "ComoConocio": "No contestó",
            "Cat_motive": "No especificado",
            "Canal": "No especificó",
            "Avg_aht": "Fuera de rango",
            "Respfcr": "0",
            "Respcsat": "1"
        },
        "Juan Ernesto López Montalvo": {
            "Cat_age": "Adulto de la Tercera Edad",
            "Gender": "male",
            "Age": 60,
            "Cat_occupation": "Sin actividad laboral",
            "State": "DF",
            "Usertype": "ANALOG",
            "Qualification": "2",
            "Cat_turn": "Matutino",
            "Evento2": "Compra con Tarjeta",
            "Amount": 1300.0,
            "Trnx": 4.0,
            "ComoConocio": "Publicidad en la tienda DANU",
            "Cat_motive": "Consulta/Informacion",
            "Canal": "Llamada",
            "Avg_aht": "Dentro de rango",
            "Respfcr": "1",
            "Respcsat": "4"
        },
        "Ana Paula González Figueroa": {
            "Cat_age": "Adulto",
            "Gender": "female",
            "Age": 32,
            "Cat_occupation": "Independiente/Negocio",
            "State": "NL",
            "Usertype": "HYBRID",
            "Qualification": "1",
            "Cat_turn": "Vespertino",
            "Evento2": "Deposito",
            "Amount": 50671.0,
            "Trnx": 56.0,
            "ComoConocio": "Promotor",
            "Cat_motive": "Operaciones/Transacciones",
            "Canal": "Llamada",
            "Avg_aht": "Fuera de rango",
            "Respfcr": "0",
            "Respcsat": "3"
        }
    }
    # === Selector de usuario ===
    usuario_seleccionado = st.selectbox(
        "Ingresa el nombre del cliente (opcional)",
        list(usuarios_prueba.keys()),  # ya incluye "Ninguno"
        key="mock_selector"
    )

    user_data = usuarios_prueba.get(usuario_seleccionado, {})

    # Inicializar last_usuario la primera vez
    if "last_usuario" not in st.session_state:
        st.session_state.last_usuario = "Ninguno"

    # Detectar cambio de usuario
    if usuario_seleccionado != st.session_state.last_usuario:
        st.session_state.last_usuario = usuario_seleccionado
        for campo, valor in user_data.items():
            st.session_state[campo] = valor
        st.rerun()

    # === Cargar tu modelo directamente (sin dropdown) ===
    models_dir = "models"
    model_name = "modelo_final.joblib"
    model_path = os.path.join(models_dir, model_name)

    try:
        model = joblib.load(model_path)
    except Exception as e:
        st.error("No se pudo cargar el modelo.")
        st.exception(e)
    else:
        st.markdown("")
        with st.form("formulario"):
            col1, col2, col3, col4, col5 = st.columns(5, gap="small")

            # --- COLUMNA 1 ---
            with col1:
                st.markdown('<div class="form-section-title">Información</div>', unsafe_allow_html=True)

                opciones_cat_age = ['Joven Adulto', 'Adulto', 'Adulto de la Tercera Edad']
                Cat_age = st.selectbox(
                    "Edad",
                    opciones_cat_age,
                    index=opciones_cat_age.index(st.session_state.get("Cat_age", opciones_cat_age[0])),
                    key="Cat_age"
                )

                opciones_gender = ["female", "male"]
                Gender = st.selectbox(
                    "Género",
                    opciones_gender,
                    index=opciones_gender.index(st.session_state.get("Gender", opciones_gender[0])),
                    key="Gender"
                )

                Age = st.number_input(
                "Edad",
                min_value=0,
                max_value=120,
                value=st.session_state.get("Age", 30),
                key="Age"
            )

                opciones_occ = ['Sin actividad laboral', 'Otros/No especificado', 'Independiente/Negocio', 'Estudiante', 'Empleado(a)']
                Cat_occupation = st.selectbox(
                    "Ocupación",
                    opciones_occ,
                    index=opciones_occ.index(st.session_state.get("Cat_occupation", opciones_occ[0])),
                    key="Occupation"
                )

            # --- COLUMNA 2 ---
            with col2:
                st.markdown('<div class="form-section-title">Ubicación y tipo</div>', unsafe_allow_html=True)

                opciones_state = ['VE', 'NL', 'SO', 'BC', 'EM', 'DF', 'JA', 'CM', 'AG', 'PU', 'MI', 'CL', 'HG', 'CO', 'QR', 'CH', 'SI', 'YU', 'OA', 'TL', 'CS', 'TM', 'QT', 'GT', 'BS', 'TB', 'GR', 'MO', 'SL', 'No especificó', 'DG', 'ZA']
                State = st.selectbox(
                    "Estado",
                    opciones_state,
                    index=opciones_state.index(st.session_state.get("State", opciones_state[0])),
                    key="State"
                )

                opciones_user = ["HYBRID", "DIGITAL", "ANALOG"]
                Usertype = st.selectbox(
                    "Tipo Usuario",
                    opciones_user,
                    index=opciones_user.index(st.session_state.get("Usertype", opciones_user[0])),
                    key="Usertype"
                )

                opciones_qual = ["1", "2", "3"]
                Qualification = st.selectbox(
                    "Nivel Tarjeta",
                    opciones_qual,
                    index=opciones_qual.index(st.session_state.get("Qualification", opciones_qual[0])),
                    key="Qualification"
                )

                opciones_turn = ['Nocturno', 'Matutino', 'Vespertino']
                Cat_turn = st.selectbox(
                    "Horario de contacto",
                    opciones_turn,
                    index=opciones_turn.index(st.session_state.get("Cat_turn", opciones_turn[0])),
                    key="Cat_turn"
                )

            # --- COLUMNA 3 ---
            with col3:
                st.markdown('<div class="form-section-title">Transacciones</div>', unsafe_allow_html=True)

                opciones_evento = ['Deposito', 'Envio de Dinero', 'Compra con Tarjeta', 'Retiro', 'Compra in App']
                Evento2 = st.selectbox(
                    "Tipo de Movimiento",
                    opciones_evento,
                    index=opciones_evento.index(st.session_state.get("Evento2", opciones_evento[0])),
                    key="Evento2"
                )

                Amount = st.number_input(
                    "Monto Total", 0.0,
                    value=float(st.session_state.get("Amount", 0.0)),
                    key="Amount"
                )

                Trnx = st.number_input(
                    "Transacciones", 0.0,
                    value=float(st.session_state.get("Trnx", 0.0)),
                    key="Trnx"
                )

                opciones_conocio = ['No contestó', 'Facebook', 'Publicidad en la tienda DANU', 'Boca a boca (conversacion)', 'Promotor', 'Otro', 'Otras redes sociales', 'Television', 'Internet', 'Anuncios en redes sociales', 'Modulo de servicio', 'Radio', 'Periodico', 'Volante', 'Publicidad pagada en redes sociales (influencer)', 'Correo electronico', 'Sitio Web', 'Instagram', 'Twitter']
                ComoConocio = st.selectbox(
                    "Cómo nos conoció",
                    opciones_conocio,
                    index=opciones_conocio.index(st.session_state.get("ComoConocio", opciones_conocio[0])),
                    key="ComoConocio"
                )

            # --- COLUMNA 4 ---
            with col4:
                st.markdown('<div class="form-section-title">Soporte</div>', unsafe_allow_html=True)

                opciones_motive = ['No especificado', 'Operaciones/Transacciones', 'Consulta/Informacion', 'Acceso/Soporte tecnico', 'Fraude/Cargos no reconocidos', 'Productos/Altas-Bajas']
                Cat_motive = st.selectbox(
                    "Motivo de Contacto",
                    opciones_motive,
                    index=opciones_motive.index(st.session_state.get("Cat_motive", opciones_motive[0])),
                    key="Cat_motive"
                )

                opciones_canal = ['No especificó', 'Llamada', 'App Chat']
                Canal = st.selectbox(
                    "Canal de Contacto",
                    opciones_canal,
                    index=opciones_canal.index(st.session_state.get("Canal", opciones_canal[0])),
                    key="Canal"
                )

                opciones_aht = ['Fuera de rango', 'Dentro de rango']
                Avg_aht = st.selectbox(
                    "Duración de Llamada",
                    opciones_aht,
                    index=opciones_aht.index(st.session_state.get("Avg_aht", opciones_aht[0])),
                    key="Avg_aht"
                )

                opciones_fcr = ["0", "1", "2"]
                Respfcr = st.selectbox(
                    "Resolución de Llamada",
                    opciones_fcr,
                    index=opciones_fcr.index(st.session_state.get("Respfcr", opciones_fcr[0])),
                    key="Respfcr"
                )

                opciones_csat = ["1", "2", "3", "4", "5"]
                Respcsat = st.selectbox(
                    "Satisfacción en Llamada",
                    opciones_csat,
                    index=opciones_csat.index(st.session_state.get("Respcsat", opciones_csat[0])),
                    key="Respcsat"
                )

            # --- COLUMNA 5 ---
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
                        icon = """<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" fill="white" viewBox="0 0 24 24"><path d="M12 .587l3.668 7.568L24 9.748l-6 5.848 1.416 8.268L12 19.771l-7.416 4.093L6 15.596 0 9.748l8.332-1.593z"/></svg>"""
                        mensaje = "CLIENTE SEGURO"
                        recommendation = "Bajo riesgo de churn. Cliente estable con buena retención esperada."
                    else:
                        result_class = "result-churn"
                        icon = """<svg xmlns="http://www.w3.org/2000/svg" width="56" height="56" fill="white" viewBox="0 0 24 24"><path d="M1 21h22L12 2 1 21zm12-3h-2v2h2v-2zm0-6h-2v5h2v-5z"/></svg>"""
                        mensaje = "ALERTA: ALTO RIESGO"
                        recommendation = "Se recomienda estrategia de retención inmediata."

                    st.markdown(f'''
                        <div class="result-box {result_class}" style="height: 320px;">
                            <div class="result-icon">{icon}</div>
                            <div class="result-message">{mensaje}</div>
                            <div class="result-prob">{prob:.1%}</div>
                            <div class="result-recommendation">{recommendation}</div>
                        </div>
                    ''', unsafe_allow_html=True)

                else:
                    st.markdown('''
                        <div class="result-box result-waiting" style="height: 320px;">
                            <div class="result-icon">
                                <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" viewBox="0 0 24 24" fill="white">
                                    <path d="M4 12l1.41 1.41L11 7.83V20h2V7.83l5.59 5.58L20 12l-8-8z"/>
                                </svg>
                            </div>
                            <div class="result-message">Ingresa los datos</div>
                            <div style="font-size: 12px; margin-top: 18px; opacity: 0.9; font-weight: 500; text-align: center; line-height: 1.5;">
                                Completa el formulario y haz clic en <b>PREDECIR CHURN</b>
                            </div>
                        </div>
                    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    pageUsuario()