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

    html_content = """
    """ + inicio_css + """

    <div class="page-wrapper">

        <div class="hero-section">
            <h1 class="hero-title">DanuCard</h1>
            <p class="hero-subtitle">Predicción de churn y estrategias data-driven para mejorar la fidelización de usuarios.</p>
        </div>

        <div class="cards-container">
            <div class="card">
                <div class="card-title">¿Quiénes somos?</div>
                <p class="card-content">
                    Somos SHECODES, un equipo especializado en transformar datos en soluciones inteligentes.
    A través de machine learning y análisis avanzado, ayudamos a las organizaciones a resolver problemas reales, optimizar decisiones y generar valor estratégico.
                </p>
            </div>

            <div class="card">
                <div class="card-title">Nuestro reto</div>
                <p class="card-content">
                    DanuCard enfrenta una alta tasa de abandono durante los primeros meses de uso.
    Nuestro proyecto busca predecir este comportamiento y diseñar soluciones accionables que fortalezcan la retención y mejoren la experiencia del usuario.
                </p>
            </div>

            <div class="card">
                <div class="card-title">Nuestra visión</div>
                <p class="card-content">
                    Desarrollar un modelo predictivo capaz de anticipar el churn, analizar los patrones de comportamiento de los usuarios e impulsar estrategias innovadoras de retención que fortalezcan la relación de DanuCard con sus clientes.
                </p>
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
