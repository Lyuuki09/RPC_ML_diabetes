import Pyro5.api
import joblib
import numpy as np
import streamlit as st
import subprocess

# Carrega o modelo treinado com os dados do Kaggle
modelo = joblib.load("modelo_diabetes_kaggle.joblib")

@Pyro5.api.expose
class ServidorDiagnostico:
    def diagnosticar(self, glicose, pressao, bmi, idade, pedida_por):
        dados_paciente = np.array([[glicose, pressao, bmi, idade]])

        # Obtém a probabilidade de ser diabético (classe 1)
        prob_diabetico = modelo.predict_proba(dados_paciente)[0][1]
        porcentagem = round(prob_diabetico * 100, 2)

        # Interpreta o resultado
        resultado = "ALTO RISCO" if porcentagem >= 50 else "BAIXO RISCO"
        
        return f"Diagnóstico para {pedida_por}:\n- Probabilidade de Diabetes: {porcentagem}%\n- Classificação: {resultado}"

# Inicializa o servidor
daemon = Pyro5.api.Daemon()
uri = daemon.register(ServidorDiagnostico)

# Front-End
st.title("Bem vindo ao Saboya's Medicine")
st.write("")
st.write("")

import streamlit as st

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.image("Saboya_medico.jpg", width=300, caption="Doutor Saboya")
    

st.write("")
st.write("")
st.write("Clique abaixo para solicitar uma nova URL do servidor")
st.button("Solicitar")
st.write("")
st.write("")
st.write("Servidor iniciado com URI:")
st.code(str(uri))




print("Servidor iniciado com URI:", uri)
daemon.requestLoop()