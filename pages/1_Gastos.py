import streamlit as st
from datetime import datetime
from components.styles import load_css
from services.google_sheets import read_data, append_data, update_pago_linha, delete_linha

st.set_page_config(page_title="💸 Gastos", layout="wide")
st.markdown(load_css(), unsafe_allow_html=True)
st.markdown("<div class='title'>💸 Controle de Gastos</div>", unsafe_allow_html=True)

df = read_data()

if not df.empty:
    for i, row in df.iterrows():
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
            pago = row.get('Pago', 'Não')
            checkbox = st.checkbox("Pago", value=(pago == "Sim"), key=f"pago_gasto_{i}")
            if checkbox != (pago == "Sim"):
                novo_valor = "Sim" if checkbox else "Não"
                update_pago_linha(i, novo_valor)
                st.rerun()
        with col6:
            if st.button("❌", key=f"del_gasto_{i}"):
                delete_linha(i)
                st.success("Gasto removido!")
                st.rerun()
else:
    st.info("Nenhum gasto registrado ainda.")

st.markdown("---")
st.markdown("### Adicionar Novo Gasto")
descricao = st.text_input("Descrição")
valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
responsavel = st.selectbox("Responsável", ["Alan", "Chloe", "Nayza"])

if st.button("Adicionar Gasto"):
    if descricao and valor > 0:
        data = datetime.now().strftime("%d/%m/%Y")
        append_data([descricao, valor, responsavel, data, "Não"])
        st.success("Gasto adicionado!")
        st.rerun()
    else:
        st.error("Preencha todos os campos corretamente.")
