import streamlit as st
from datetime import datetime
from components.styles import load_css
from services.renda_fixa import read_rendas, append_renda, delete_renda, update_pago

st.set_page_config(page_title="💼 Rendas Fixas", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)
st.markdown("<div class='title'>💼 Rendas Fixas</div>", unsafe_allow_html=True)

df_renda = read_rendas()
if not df_renda.empty:
    for i, row in df_renda.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([3, 2, 2, 2, 2, 1])
        with col1:
            st.markdown(f"**{row['Descrição']}**")
        with col2:
            st.markdown(f"R$ {row['Valor']:.2f}")
        with col3:
            st.markdown(row['Responsável'])
        with col4:
            st.markdown(row['Data'])
        with col5:
            pago = row['Pago']
            checkbox = st.checkbox("Pago", value=(pago == "Sim"), key=f"pago_{i}")
            if checkbox != (pago == "Sim"):
                novo_valor = "Sim" if checkbox else "Não"
                update_pago(i, novo_valor)
                st.rerun()
        with col6:
            if st.button("❌", key=f"del_{i}"):
                delete_renda(i)
                st.success("Renda removida!")
                st.rerun()
else:
    st.info("Nenhuma renda fixa cadastrada ainda.")

st.markdown("### Adicionar Nova Renda Fixa")
descricao_r = st.text_input("Descrição da Renda")
valor_r = st.number_input("Valor da Renda (R$)", min_value=0.0, step=0.01)
responsavel_r = st.selectbox("Responsável", ["Alan", "Chloe", "Nayza"], key="renda_resp")
pago_r = st.selectbox("Pago?", ["Sim", "Não"])

if st.button("Adicionar Renda Fixa"):
    if descricao_r and valor_r > 0:
        data = datetime.now().strftime("%d/%m/%Y")
        append_renda([descricao_r, valor_r, responsavel_r, data, pago_r])
        st.success("Renda fixa adicionada!")
        st.rerun()
    else:
        st.error("Preencha todos os campos.")
