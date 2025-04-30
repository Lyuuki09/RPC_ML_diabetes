import Pyro5.api
import streamlit as st



# Dados de exemplo

# glicose = 88
# pressao = 120
# bmi = 33
# idade = 44
# medico = "Dra Andrea"

st.title("Seja bem vindo, Doutor(a)!")

# Use o URI exibido pelo servidor
uri = st.text_input("Digite a URI do servidor", 
placeholder="",
help="Cole aqui a URI fornecida pelo servidor")

# Inicializa servidor como None
servidor = None
st.text("")
st.text("")
st.header("Realize abaixo o diagnóstico do seu paciente")


glicose = st.number_input("Digite a glicose do paciente", step=0.1)
pressao = st.number_input("Digite a pressão média do paciente", step=0.1)
bmi = st.number_input("Digite o IMC do paciente", step=0.1)
idade = st.number_input("Digite a idade do paciente", min_value=0, step=1)
medico = st.text_input("Digite o nome do seu paciente")

if st.button("Enviar Dados", key="enviar_diagnostico"):
    if not uri:
        st.error("Por favor, insira a URI do servidor primeiro!")
    elif not all(isinstance(x, (int, float)) for x in [glicose, pressao, bmi, idade]):
        st.error("Nem todos os valores são numéricos.")
    else:
        try:
            # Conecta ao servidor usando a URI fornecida
            servidor = Pyro5.api.Proxy(uri)
  
            # Faz o diagnóstico
            resultado = servidor.diagnosticar(glicose, pressao, bmi, idade, medico)
            resultado = resultado.encode('utf-8').decode('utf-8')
            
            # Exibe o resultado em um box destacado
            st.success("Dados enviados com sucesso!")
            st.markdown("### Resultado do Diagnóstico")
            st.text_area("", value=resultado, height=200, disabled=True)
        except Exception as e:
            st.error(f"Erro ao conectar com o servidor: {str(e)}") 
# Faz o diagnóstico
resultado = servidor.diagnosticar(glicose, pressao, bmi, idade, medico)
resultado = resultado.encode('utf-8').decode('utf-8')


print(resultado)

