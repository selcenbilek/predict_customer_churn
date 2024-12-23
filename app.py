import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Modeli yükleyin
model_pkl_file = "churn_model.pkl"
with open(model_pkl_file, 'rb') as file:
    model = pickle.load(file)

# Streamlit uygulaması başlat
st.title("Müşteri Churn Tahmini")
st.write("Lütfen müşteri bilgilerini girin ve tahmin sonucunu görün.")

# Kullanıcıdan veri alabilmek için gerekli özellikleri listeleyin
features = [
    "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", 
    "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", 
    "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", 
    "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", 
    "MonthlyCharges", "TotalCharges"
]

user_input = {}

# Kullanıcı girdilerini alın
for feature in features:
    if feature in ["tenure", "MonthlyCharges", "TotalCharges"]:
        user_input[feature] = st.number_input(f"{feature}", min_value=0.0, step=0.1)
    else:
        user_input[feature] = st.selectbox(
            f"{feature}", ["Yes", "No"] if feature not in ["gender", "InternetService", "Contract", "PaymentMethod"] else 
            (["Male", "Female"] if feature == "gender" else 
             ["DSL", "Fiber optic", "No"] if feature == "InternetService" else 
             ["Month-to-month", "One year", "Two year"] if feature == "Contract" else 
             ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        )

# Kullanıcı girdilerini dataframe'e çevirin
user_df = pd.DataFrame([user_input])

# Veriyi işleme adımları
for column in user_df.columns:
    if user_df[column].dtype == np.number:
        continue
    user_df[column] = LabelEncoder().fit_transform(user_df[column])

# Özellikleri standartlaştırma
scaler = StandardScaler()
user_features = scaler.fit_transform(user_df)

# Tahmin yap
if st.button("Tahmin Yap"):
    prediction = model.predict(user_features)

    # Sonucu göster
    if prediction[0] == 1:
        st.error("Tahmin: Bu müşteri şirketten ayrılabilir.")
    else:
        st.success("Tahmin: Bu müşteri şirkette kalabilir.")


