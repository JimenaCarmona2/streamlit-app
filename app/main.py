import streamlit as st
from example_extra import example
from dashboard import dashboard
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

    st.html(f"""
        <style>
            @keyframes fadeInDown {{
                from {{
                    opacity: 0;
                    transform: translateY(-20px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0)
                }}
            }}
            
            .nav-container {{
                display: flex;
                justify-content: flex-end;
                margin-bottom: 40px;
                animation: fadeInDown 0.7s ease-out 0.1s backwards;
            }}

            .nav-tabs {{
                display: flex;
                gap: 14px;
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(15px);
                padding: 11px 14px;
                border-radius: 32px;
                border: 1px solid rgba(91, 163, 208, 0.1);
                box-shadow: 0 2px 12px rgba(91, 163, 208, 0.05);
            }}

            .nav-tab {{
                background-color: transparent;
                color: #777;
                padding: 9px 28px;
                border: none;
                cursor: pointer;
                font-size: 14px;
                font-weight: 600;
                transition: all 0.3s ease;
                border-radius: 24px;
                letter-spacing: 0.3px;
                text-decoration: none;
                display: inline-block;
            }}

            .nav-tab.active {{
                background: linear-gradient(135deg, #5b9cce 0%, #4682b4 100%);
                color: white;
                box-shadow: 0 2px 8px rgba(70, 130, 180, 0.15);
            }}

            .nav-tab:hover {{
                color: #5b9cce;
                background: rgba(91, 163, 208, 0.06);
            }}

            .nav-tabs, .dropdown, .dropdown-content {{
                position: relative;
                z-index: 9999999;
            }}

            .dropdown {{
                position: relative;
                display: inline-block;
                -webkit-tap-highlight-color: transparent;
                z-index: 10000;
                pointer-events: auto;
            }}

            .dropbtn {{
                background-color: transparent;
                color: #777;
                padding: 9px 28px;
                font-size: 14px;
                font-weight: 600;
                border: none;
                border-radius: 24px;
                cursor: pointer;
                letter-spacing: 0.3px;
                transition: all 0.25s ease;
            }}

            .dropdown-content {{
                display: none;
                position: absolute;
                top: calc(100% - 1px);
                left: 0;
                min-width: 140px;
                background: rgba(255,255,255,0.98);
                backdrop-filter: blur(15px);
                border-radius: 14px;
                border: 1px solid rgba(91,163,208,0.1);
                box-shadow: 0 2px 12px rgba(91,163,208,0.08);
                z-index: 2147483647;
                padding: 6px 0;
                pointer-events: auto;
                -webkit-user-select: none;
            }}

            .dropdown-content a {{
                display: block;
                padding: 10px 22px;
                color: #777;
                font-size: 14px;
                font-weight: 600;
                text-decoration: none;
                transition: all .3s ease;
            }}

            .dropdown-content a:hover {{
                background: rgba(91,163,208,0.06);
                color: #5b9cce;
            }}

            .dropdown.open > .dropdown-content,
            .dropdown:focus-within > .dropdown-content {{
                display: block;
            }}

            .dropdown.open > .dropbtn,
            .dropdown:focus-within > .dropbtn {{
                background: rgba(91,163,208,0.06);
                color: #5b9cce;
            }}
        </style>

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

        <script>
            (function() {{
                const dropdown = document.getElementById('mainDropdown');
                const btn = document.getElementById('dropBtn');

                btn.addEventListener('click', function(e) {{
                    e.stopPropagation();
                    const isOpen = dropdown.classList.contains('open');
                    dropdown.classList.toggle('open', !isOpen);
                    btn.setAttribute('aria-expanded', String(!isOpen));
                }});

                dropdown.addEventListener('mouseenter', () => {{
                    dropdown.classList.add('open');
                    btn.setAttribute('aria-expanded', 'true');
                }});
                dropdown.addEventListener('mouseleave', () => {{
                    if (!dropdown.matches(':focus-within')) {{
                        dropdown.classList.remove('open');
                        btn.setAttribute('aria-expanded', 'false');
                    }}
                }});

                document.addEventListener('click', function(e) {{
                    if (!dropdown.contains(e.target)) {{
                        dropdown.classList.remove('open');
                        btn.setAttribute('aria-expanded', 'false');
                    }}
                }});

                dropdown.querySelectorAll('a').forEach(a => {{
                    a.addEventListener('click', () => {{
                        dropdown.classList.remove('open');
                        btn.setAttribute('aria-expanded', 'false');
                    }});
                }});
            }})();
        </script>
    """)

def inicio():
    html_content = """
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: linear-gradient(135deg, #f5f9fc 0%, #e8f0f7 25%, #f0f6fa 50%, #e8f1f8 75%, #f5f9fc 100%);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
            min-height: 100vh;
            overflow-x: hidden;
        }

        body:before, body:after, .page-wrapper:before {
            pointer-events: none !important;
        }

        body::before {
            content: '';
            position: absolute;
            top: -20%;
            left: -10%;
            width: 700px;
            height: 700px;
            background: radial-gradient(circle, rgba(91, 163, 208, 0.15) 0%, rgba(91, 163, 208, 0.05) 40%, transparent 70%);
            border-radius: 45% 55% 60% 40%;
            animation: float 25s infinite ease-in-out;
            z-index: -10;
            filter: blur(40px);
        }

        body::after {
            content: '';
            position: absolute;
            bottom: -25%;
            right: -15%;
            width: 700px;
            height: 700px;
            background: radial-gradient(circle, rgba(74, 130, 180, 0.12) 0%, rgba(74, 130, 180, 0.04) 40%, transparent 70%);
            border-radius: 40% 60% 55% 45%;
            animation: float 30s infinite ease-in-out reverse;
            z-index: -10;
            filter: blur(40px);
        }

        .page-wrapper::before {
            content: '';
            position: absolute;
            top: 40%;
            left: 50%;
            transform: translateX(-50%);
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(91, 163, 208, 0.08) 0%, transparent 70%);
            border-radius: 50%;
            animation: float 35s infinite ease-in-out;
            z-index: -10;
            pointer-events: none;
            filter: blur(50px);
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(35px); }
        }

        .page-wrapper {
            position: relative;
            z-index: 1;
            padding: 40px 80px;
            max-width: 1400px;
            margin: 0 auto;
        }

        @keyframes fadeInDown {
            from {
            opacity: 0;
            transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-section {
            text-align: center;
            margin-bottom: 80px;
            animation: fadeInUp 0.9s ease-out 0.2s backwards;
            padding: 30px 40px;
        }

        .hero-title {
            font-size: 72px;
            font-weight: 800;
            background: linear-gradient(135deg, #4682b4 0%, #5ba3d0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 16px;
            letter-spacing: -0.8px;
            line-height: 1.1;
        }

        .hero-subtitle {
            font-size: 17px;
            color: #666;
            margin-bottom: 0;
            font-weight: 500;
            letter-spacing: 0.2px;
            line-height: 1.7;
            max-width: 680px;
            margin-left: auto;
            margin-right: auto;
        }

        .cards-container {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
            animation: fadeInUp 1.1s ease-out 0.4s backwards;
        }

        .card {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.97) 0%, rgba(249, 251, 253, 0.97) 100%);
            border-radius: 28px;
            padding: 40px 32px;
            box-shadow: 0 2px 12px rgba(91, 163, 208, 0.05);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            border: 1px solid rgba(91, 163, 208, 0.08);
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: linear-gradient(90deg, transparent, rgba(91, 163, 208, 0.3), transparent);
        }

        .card:hover {
            transform: translateY(-6px);
            background: linear-gradient(135deg, #ffffff 0%, #f9fbfd 100%);
            box-shadow: 0 6px 20px rgba(91, 163, 208, 0.1);
            border-color: rgba(91, 163, 208, 0.15);
        }

        .card-title {
            font-size: 20px;
            font-weight: 700;
            color: #1a1a1a;
            margin-bottom: 22px;
            line-height: 1.4;
            letter-spacing: -0.3px;
        }

        .card-icon {
            width: 100%;
            height: 110px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 22px;
        }

        .card-icon svg {
            width: 90px;
            height: 90px;
            transition: transform 0.4s ease, filter 0.4s ease;
            filter: drop-shadow(0 1px 4px rgba(91, 163, 208, 0.1));
        }

        .card:hover .card-icon svg {
            transform: scale(1.08) rotate(2deg);
            filter: drop-shadow(0 3px 10px rgba(91, 163, 208, 0.15));
        }

        .card-content {
            font-size: 14.5px;
            color: #666;
            line-height: 1.8;
            text-align: justify;
            font-weight: 500;
            letter-spacing: 0.15px;
        }

        @media (max-width: 1024px) {
            .cards-container {
                grid-template-columns: repeat(2, 1fr);
                gap: 24px;
            }
                
            .hero-title {
                font-size: 56px;
            }
                
            .page-wrapper {
                padding: 30px 40px;
            }
        }
            
        @media (max-width: 640px) {
            .cards-container {
                grid-template-columns: 1fr;
                gap: 20px;
            }
                
            .page-wrapper {
                padding: 20px 16px;
            }
                
            .hero-title {
                font-size: 42px;
            }
                
            .hero-section {
                margin-bottom: 60px;
                padding: 24px 12px;
            }
                
            .card {
                padding: 32px 24px;
            }
    </style>

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
