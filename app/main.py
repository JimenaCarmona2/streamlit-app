import streamlit as st
from example_extra import example
from pageInfo import pageInfo
from pageChurn import pageChurn
from pageUsuario import pageUsuario

st.set_page_config(
    page_title="DanuCard - Churn Prediction & Retention Intelligence",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def navbar():
    current_page = st.query_params.get("page", "inicio")

    def get_tab_class(page_name):
        return "nav-tab active" if current_page == page_name else "nav-tab"
    
    with open("app/styles/navbar.css") as f:
        navbar_css = f"<style>{f.read()}</style>"

    with open("app/js/navbar.js") as f:
        navbar_js = f"<script>{f.read()}</script>"

    st.html(navbar_css + f"""

        <div class="nav-container">
            <div class="nav-tabs">
                <a class="{get_tab_class('inicio')}" href="?page=inicio">Inicio</a>
                <a class="{get_tab_class('propuestas')}" href="?page=propuestas">Propuestas</a>

                <div class="dropdown" id="mainDropdown">
                <button class="dropbtn {'nav-tab active' if current_page in ['pageInfo', 'pageChurn', 'pageUsuario'] else 'nav-tab'}" id="dropBtn" aria-haspopup="true" aria-expanded="false" tabindex="0">
                    Dashboard ▾
                </button>

                <div class="dropdown-content" role="menu" aria-labelledby="dropBtn">
                    <a href="?page=pageInfo" role="menuitem">Información Descriptiva</a>
                    <a href="?page=pageChurn" role="menuitem">Análisis de Churn</a>
                    <a href="?page=pageUsuario" role="menuitem">Perfil del Usuario</a>
                </div>
            </div>
                
            </div>
        </div>
    """ + navbar_js)

def inicio():

    with open("app/styles/inicio.css") as f:
        inicio_css = f"<style>{f.read()}</style>"

    # Inyectar CSS + Bootstrap Icons
    st.markdown(inicio_css, unsafe_allow_html=True)
    st.markdown("""
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <style>
        .card-title i {
            margin-right: 10px;
            font-size: 20px;
            vertical-align: middle;
        }
    </style>
    """, unsafe_allow_html=True)

    # Contenido HTML
    html_content = """
    <html lang="es">
    <div class="inicio-wrapper">
        <div class="hero-section">
            <h1 class="inicio-title">DanuCard</h1>
            <p class="inicio-subtitle">Predicción de churn y estrategias data-driven para mejorar la fidelización de usuarios.</p>
        </div>

        <div class="cards-container">

            <div class="card">
                <div class="card-title"><i class="bi bi-people-fill"></i> ¿Quiénes somos?</div>
                <div class="card-content contenedor-texto">
                    En SHECODES transformamos datos en soluciones inteligentes usando machine learning para resolver problemas reales y generar valor.
                </div>
            </div>

            <div class="card">
                <div class="card-title"><i class="bi bi-bullseye"></i> Nuestro reto</div>
                <div class="card-content contenedor-texto">
                   DanuCard sufre una alta deserción inicial. Buscamos predecir el abandono temprano y proponer acciones eficaces para mejorar la retención.
                </div>
            </div>

            <div class="card">
                <div class="card-title"><i class="bi bi-rocket-takeoff-fill"></i> Nuestra visión</div>
                <div class="card-content contenedor-texto">
                    Crear un modelo predictivo robusto que anticipe el churn, analice patrones de comportamiento y potencie estrategias efectivas de fidelización sostenible.
                </div>
            </div>

        </div>

    </div>
    """ 
    st.html(html_content)

if "page" not in st.session_state:
    st.session_state.page = "inicio"

url_page = st.query_params.get("page")

if url_page in ["incio", "propuestas", "pageInfo", "pageChurn", "pageUsuario"]:
    st.session_state.page = url_page
else:
    st.query_params["page"] = st.session_state.page

navbar()

page = st.session_state.page

if page == "inicio":
    inicio()
elif page == "propuestas":
    example()
elif page == "pageInfo":
    pageInfo()
elif page == "pageChurn":
    pageChurn()
elif page == "pageUsuario":
    pageUsuario()
