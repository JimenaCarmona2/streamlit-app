import streamlit as st
import pandas as pd
import numpy as np


def example():
    st.set_page_config(
        page_title="Propuestas",
        layout="wide"
    )

    # Aplica el CSS externo
    with open("app/styles/propuestas.css") as f:
        inicio_css = f"<style>{f.read()}</style>"
    st.markdown(inicio_css, unsafe_allow_html=True)


    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
        <div class="header-section">
            <div class="header-title">Propuestas Clave</div>
            <div class="header-subtitle">Un roadmap hacia el éxito</div>
        </div>
    """, unsafe_allow_html=True)

    # Three phase columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="phase-container phase-1"> 
                <div class="phase-number">01</div>
                <div class="phase-title">Acciones inmediatas</div>
                <div class="phase-description">
                    Acciones inmediatas para reducir el abandono mediante personalización, recompensas, venta cruzada y educación financiera.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="phase-container phase-2">
                <div class="phase-number">02</div>
                <div class="phase-title">Emotional AI Banking </div>
                <div class="phase-description">
                    Se integran tecnologías de inteligencia artificial para detectar señales de abandono y activar respuestas automáticas que mejoran la retención.
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="phase-container phase-3">
                <div class="phase-number">03</div>
                <div class="phase-title">Digital Twin</div>
                <div class="phase-description">
                    Se implementa un modelo digital que simula decisiones del cliente para anticipar comportamientos y prevenir el abandono de forma proactiva.
                </div>
            </div>
        """, unsafe_allow_html=True)
