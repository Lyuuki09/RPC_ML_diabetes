import streamlit as st

st.title("Meu App com Streamlit")

st.header("Exemplo simples")
st.write("Olá, mundo! Bem-vindo ao Streamlit.")

# Entrada do usuário
nome = st.text_input("Digite seu nome:")

# Botão
if st.button("Dizer oi"):
    st.success(f"Oi, {nome}!")

# Gráfico
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'y': np.sin(np.linspace(0, 10, 100))
})

st.line_chart(data.set_index('x'))
