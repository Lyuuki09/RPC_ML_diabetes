import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Lê o CSV baixado
df = pd.read_csv("diabetes.csv")

# Seleciona colunas de entrada (features) e a saída (label)
X = df[["Glucose", "BloodPressure", "BMI", "Age"]]
y = df["Outcome"]  # 0 = não diabético, 1 = diabético

# Divide entre treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Salva o modelo treinado
joblib.dump(modelo, "modelo_diabetes_kaggle.joblib")

print("Modelo treinado com sucesso com os dados do Kaggle!")