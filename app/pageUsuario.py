import streamlit as st

def pageUsuario():
        st.title("Perfil del Usuario")
        st.write("Contenido de la página 3")
        with st.sidebar:
            st.header("Filtros")
            st.text("Segmentación del cliente")
            st.checkbox("Perfil 1")
            st.checkbox("Perfil 2")
            st.checkbox("Perfil 3")