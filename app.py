import streamlit as st
import random
import pandas as pd
from datetime import datetime
import os

st.title("💪 Asistente Fitness Inteligente PRO")

# ARCHIVO DONDE SE GUARDA
archivo = "progreso.csv"

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

if st.button("Analizar y guardar progreso"):

    # CALORÍAS
    if sexo == "Mujer":
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    else:
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5

    # IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)

    st.subheader("🔎 Análisis")
    st.write("🔥 Calorías:", round(calorias, 2))
    st.write("📊 IMC:", round(imc, 2))

    # OBJETIVO
    if imc < 18.5:
        objetivo = "masa"
        st.warning("Bajo peso → Ganar masa")
    elif imc < 25:
        objetivo = "recomposicion"
        st.success("Peso normal → Mejorar físico")
    else:
        objetivo = "definicion"
        st.warning("Sobrepeso → Bajar grasa")

    # GUARDAR DATOS
    nuevo_dato = pd.DataFrame({
        "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "Peso": [peso],
        "IMC": [round(imc, 2)],
        "Objetivo": [objetivo]
    })

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)
        datos = pd.concat([datos, nuevo_dato], ignore_index=True)
    else:
        datos = nuevo_dato

    datos.to_csv(archivo, index=False)

    st.success("✅ Progreso guardado correctamente")

    # HISTORIAL
    st.subheader("📈 Tu progreso")

    st.dataframe(datos)

# 🔎 VER HISTORIAL SIN GUARDAR
if st.button("Ver historial"):

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)
        st.subheader("📊 Historial completo")
        st.dataframe(datos)
    else:
        st.warning("Aún no hay datos guardados")
