import streamlit as st
from components.styles import load_css

# Configurações da página
st.set_page_config(
    page_title="Controle Financeiro Familiar",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar estilos CSS
st.markdown(load_css(), unsafe_allow_html=True)

# Título da Home
st.markdown("<div class='title'>🏠 Bem-vindo ao Controle Financeiro Familiar</div>", unsafe_allow_html=True)

# Mensagem de instrução
st.markdown("""
    Esta aplicação permite que você controle:
    - 💸 Seus **gastos**
    - 💼 Suas **rendas fixas**
    
    Use o **menu lateral** para navegar entre as páginas do sistema.
    
    ---
    """)
