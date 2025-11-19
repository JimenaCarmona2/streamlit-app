import streamlit as st
from datetime import datetime

def dashboard():
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
                position: relative;
                overflow-x: hidden;
            }
            
            /* Enhanced background with more sophisticated design elements */
            /* Soft gradient blobs with more visible but gentle appearance */
            body::before {
                content: '';
                position: fixed;
                top: -20%;
                left: -10%;
                width: 700px;
                height: 700px;
                background: radial-gradient(circle, rgba(91, 163, 208, 0.15) 0%, rgba(91, 163, 208, 0.05) 40%, transparent 70%);
                border-radius: 45% 55% 60% 40%;
                animation: float 25s infinite ease-in-out;
                z-index: 0;
                pointer-events: none;
                filter: blur(40px);
            }
            
            body::after {
                content: '';
                position: fixed;
                bottom: -25%;
                right: -15%;
                width: 700px;
                height: 700px;
                background: radial-gradient(circle, rgba(74, 130, 180, 0.12) 0%, rgba(74, 130, 180, 0.04) 40%, transparent 70%);
                border-radius: 40% 60% 55% 45%;
                animation: float 30s infinite ease-in-out reverse;
                z-index: 0;
                pointer-events: none;
                filter: blur(40px);
            }
            
            /* Added subtle third gradient element for more depth */
            .page-wrapper::before {
                content: '';
                position: fixed;
                top: 40%;
                left: 50%;
                transform: translateX(-50%);
                width: 500px;
                height: 500px;
                background: radial-gradient(circle, rgba(91, 163, 208, 0.08) 0%, transparent 70%);
                border-radius: 50%;
                animation: float 35s infinite ease-in-out;
                z-index: 0;
                pointer-events: none;
                filter: blur(50px);
            }
            
            @keyframes float {
                0%, 100% { transform: translateY(0px) rotate(0deg); }
                50% { transform: translateY(35px) rotate(2deg); }
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
            
            /* Minimalist navigation bar - the design they loved */
            .nav-container {
                display: flex;
                justify-content: flex-end;
                margin-bottom: 60px;
                animation: fadeInDown 0.7s ease-out;
            }
            
            .nav-tabs {
                display: flex;
                gap: 14px;
                background: rgba(255, 255, 255, 0.9);
                backdrop-filter: blur(15px);
                padding: 11px 14px;
                border-radius: 32px;
                border: 1px solid rgba(91, 163, 208, 0.1);
                box-shadow: 0 2px 12px rgba(91, 163, 208, 0.05);
            }
            
            .nav-tab {
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

            }
            
            .nav-tab:first-child {
                background: linear-gradient(135deg, #5b9cce 0%, #4682b4 100%);
                color: white;
                box-shadow: 0 2px 8px rgba(70, 130, 180, 0.15);
            }
            
            .nav-tab:hover {
                color: #5b9cce;
                background: rgba(91, 163, 208, 0.06);
            }
            
            /* Premium hero section with compelling copy */
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
            
            /* Modern cards with light background and premium aesthetics */
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
                
                .nav-tabs {
                    flex-wrap: wrap;
                    gap: 10px;
                    justify-content: center;
                }
                
                .nav-tab {
                    padding: 8px 20px;
                    font-size: 13px;
                }
            }
        </style>
    </head>
    <body>
        <div class="page-wrapper">
            <div class="nav-container">
                <div class="nav-tabs">
                        <a class="nav-tab" href="?page=inicio">Inicio</a>
                        <a class="nav-tab" href="?page=propuestas">Propuestas</a>
                        <a class="nav-tab" href="?page=dashboard">Dashboard</a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """

    st.html(html_content)

    with st.sidebar:
        st.header("Filtros")

        tasa_churn = st.checkbox(
            "Tasa Churn",
            ["Silent", "Parcial", "Complete"]
        )

        usuarios = st.checkbox(
            "Usuarios",
            ["Mujer", "Hombre"]
        )

        fecha = st.slider(
            "Tiempo",
            value = datetime(2022, 1, 1),
            format="MM/YYYY"
        )

        st.markdown("---")


    
    def pageInfo():
        st.title("Información Descriptiva")
        st.write("Contenido de la página 1", tasa_churn, usuarios, fecha)

    def pageChurn():
        st.title("Análisis de Churn")
        st.write("Contenido de la página 2")

    def pageUsuario():
        st.title("Perfil del Usuario")
        st.write("Contenido de la página 3")

    pages = {
        "Páginas": [
            st.Page(pageInfo, title="Información Descriptiva"),
            st.Page(pageChurn, title="Análisis de Churn"),
            st.Page(pageUsuario, title="Perfil del Usuario")
        ]
    }

    pg = st.navigation(pages, position="sidebar")
    pg.run()


