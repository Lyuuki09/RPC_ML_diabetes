import Pyro5.api

# Use o URI exibido pelo servidor
uri = "PYRONAME://localhost:59204"
servidor = Pyro5.api.Proxy(uri)

# Dados de exemplo
glicose = 150
pressao = 85
bmi = 30.1
idade = 50
medico = "Dra. Paula"

# Faz o diagnóstico
resultado = servidor.diagnosticar(glicose, pressao, bmi, idade, medico)
print(resultado)