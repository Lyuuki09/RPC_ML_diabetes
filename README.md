CONSULTORIA ESPECIALIZADA DE APOIO AO PROJETO INTEGRADO: SISTEMAS DISTRIBUÍDOS

Clínica Médica Carlos Saboya LTDA

LEANDRO YUUKI DE MOURA CARVALHO (RA00333040)
MIGUEL PAIXAO DE ALMEIDA (RA00333320)
YGOR REIS GORNI (RA00326865)

São Paulo, 16 de abril de 2025
 
Introdução
O presente projeto tem como objetivo integrar os conhecimentos da disciplina de Redes de Computadores, com foco em RPC (Remote Procedure Call), e os fundamentos de Ciência de Dados, simulando um sistema de diagnóstico médico distribuído. Utilizando a biblioteca Pyro5 em Python, criamos um modelo funcional onde um cliente pode solicitar diagnósticos médicos a um servidor remoto que utiliza um modelo de machine learning para realizar previsões com base em dados reais de pacientes.
Objetivo

O objetivo principal desta Prova de Conceito (POC) foi demonstrar a viabilidade de um sistema distribuído de diagnóstico médico simples, utilizando chamadas de procedimento remoto (RPC) com a biblioteca Pyro5. A proposta é simular uma arquitetura onde o cliente envia dados de um paciente para um servidor que realiza o diagnóstico com base em um modelo treinado de classificação médica. Além de reforçar o conteúdo de Redes de Computadores (especialmente RPC e RMI), o projeto também visa integrar conceitos de Ciência de Dados no contexto prático de um sistema realista.

A POC possui alta escalabilidade e reduz latência das comunicações, sendo eficaz para implementar a RPC e gerenciar o sistema da clínica. Ocorre a interoperabilidade entre os sistemas, unindo o prontuário eletrônico, atendimento, monitoramento glicêmico e farmácia.

Implementação
Servidor RPC: Foi criado um servidor que hospeda um objeto remoto responsável por receber dados de pacientes (como glicose, idade, pressão, etc.) e retornar um diagnóstico médico baseado em um modelo simples de aprendizado de máquina treinado com um conjunto de dados público sobre diabetes.

Cliente: Uma aplicação cliente se conecta ao servidor via URI fornecida pelo Pyro5 e envia os dados do paciente. O cliente então recebe e exibe o diagnóstico retornado pelo servidor.

Diferença entre RPC e RMI
O RMI é uma versão específica do RPC para Java, porém não é aplicável para sistemas distribuídos. Há permissão de invocar objetos presentes em outra máquina, enquanto o RPC utiliza uma outra máquina como se fosse local. Em resumo, o RPC utiliza um procedimento servidor remoto (em Python), enquanto o RMI utiliza um método em servidor remoto (Java).

Funcionamento do projeto ao qual foi dividido em três partes principais:

Treinamento do Modelo (Machine Learning):
Foi utilizado o dataset de diabetes do Scikit-learn para treinar um modelo de classificação. O modelo foi salvo em disco usando joblib.

Servidor RPC (Pyro5):
O servidor carrega o modelo e expõe um método diagnosticar() que recebe os dados do paciente e retorna o diagnóstico.

Cliente RPC:
O cliente se conecta ao servidor por meio do URI gerado e envia os dados do paciente para obter o diagnóstico.

Resultados:

O projeto foi executado com sucesso em um ambiente local, permitindo que o cliente se conectasse remotamente ao servidor via Pyro5. O modelo de Machine Learning conseguiu fazer previsões básicas, simulando o diagnóstico de diabetes com entradas simplificadas.


Tecnologias e Middleware Utilizados:
Python 3.13
Pyro5 – Remote Object Library para RPC.
Scikit-learn – Para treinamento do modelo de ML.
Pandas – Para manipulação de dados.
Joblib – Para salvar e carregar o modelo treinado.
Visual Studio Code – Para desenvolvimento e execução do projeto.
Referências Bibliográficas
PEDREGOSA, F. et al. Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, v. 12, p. 2825-2830, 2011. https://scikit-learn.org.

PYTHON SOFTWARE FOUNDATION. Python 3.12 Documentation. 2024. https://docs.python.org/3.12/.

DE BOER, I. Pyro5 Documentation – Python Remote Objects. 2021. https://pyro5.readthedocs.io/. 

MCKINNEY, W. Data structures for statistical computing in Python. In: PROC. 9TH PYTHON IN SCIENCE CONF., 2010, Austin. Anais [...]. Austin: SciPy, 2010. p. 51–56. https://pandas.pydata.org/. 

SILBERSCHATZ, A.; GALVIN, P. B.; GAGNE, G. Operating system concepts. 10. ed. Hoboken: Wiley, 2018.
