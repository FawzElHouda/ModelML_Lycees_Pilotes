
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Prédiction des Affectations aux Lycées Pilotes")

cre = st.number_input("CRE encodé", min_value=0)
type_candidature = st.number_input("Type candidature encodé", min_value=0)
genre = st.number_input("Genre encodé", min_value=0)
effectif_inscrits = st.number_input("Effectif inscrits", min_value=0)
effectif_presentes = st.number_input("Effectif présentés", min_value=0)
taux_presence = st.number_input("Taux présence", min_value=0.0, max_value=1.0)

if st.button("Prédire"):
    data = np.array([[cre, type_candidature, genre,
                      effectif_inscrits,
                      effectif_presentes,
                      taux_presence]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    st.success(f"Nombre prédit d'élèves affectés : {prediction[0]:.0f}")
