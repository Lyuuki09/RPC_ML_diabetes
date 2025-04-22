import Pyro5.api
import joblib
import numpy as np

# Carrega o modelo treinado com os dados do Kaggle
modelo = joblib.load("modelo_diabetes_kaggle.joblib")

@Pyro5.api.expose
class ServidorDiagnostico:
    def diagnosticar(self, glicose, pressao, bmi, idade, pedida_por):
        # Cria um vetor com os dados recebidos
        dados_paciente = np.array([[glicose, pressao, bmi, idade]])
        
        # Faz a previsão
        previsao = modelo.predict(dados_paciente)[0]

        # Interpretação do resultado
        resultado = "DIABÉTICO" if previsao == 1 else "NÃO DIABÉTICO"
        return f"Diagnóstico para {pedida_por}: {resultado}"

# Inicializa o servidor Pyro
daemon = Pyro5.api.Daemon()
uri = daemon.register(ServidorDiagnostico)

print("Servidor iniciado com URI:", uri)
daemon.requestLoop()