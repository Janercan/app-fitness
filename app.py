import streamlit as st
import random
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt
from PIL import Image

st.title("💪 Asistente Fitness Inteligente PRO + IA")

archivo = "progreso.csv"

# 📸 FOTOS
st.subheader("📸 Análisis corporal con IA")

frente = st.file_uploader("Foto de frente", type=["jpg", "png", "jpeg"])
espalda = st.file_uploader("Foto de espalda", type=["jpg", "png", "jpeg"])
lado_izq = st.file_uploader("Foto lado izquierdo", type=["jpg", "png", "jpeg"])
lado_der = st.file_uploader("Foto lado derecho", type=["jpg", "png", "jpeg"])

fotos_completas = frente and espalda and lado_izq and lado_der

if fotos_completas:
    st.success("✅ Fotos completas cargadas")

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

# FUNCIÓN IA SIMULADA
def analisis_ia(imc, objetivo):
    resultado = []

    if objetivo == "masa":
        resultado.append("🔎 Se recomienda aumentar masa muscular general")
        resultado.append("💪 Priorizar pecho, espalda y pierna")

    elif objetivo == "definicion":
        resultado.append("🔥 Enfocar en pérdida de grasa")
        resultado.append("🏃 Añadir cardio y core")

    else:
        resultado.append("⚖️ Buen equilibrio corporal")
        resultado.append("💪 Mejorar definición muscular")

    # Simulación más avanzada
    if imc > 25:
        resultado.append("⚠️ Posible acumulación de grasa en abdomen")
    elif imc < 18.5:
        resultado.append("⚠️ Bajo desarrollo muscular general")
    else:
        resultado.append("✅ Composición corporal estable")

    return resultado

# FUNCIÓN EJERCICIOS
def elegir(lista, cantidad, tipo):
    if cantidad > len(lista):
        cantidad = len(lista)
    seleccion = random.sample(lista, cantidad)

    resultado = []
    for e in seleccion:
        if tipo == "masa":
            resultado.append(f"{e} - 4x8")
        elif tipo == "definicion":
            resultado.append(f"{e} - 4x12")
        else:
            resultado.append(f"{e} - 4x10")
    return resultado

if st.button("Analizar con IA"):

    altura_m = altura / 100
    imc = peso / (altura_m ** 2)

    # OBJETIVO
    if imc < 18.5:
        objetivo = "masa"
    elif imc < 25:
        objetivo = "recomposicion"
    else:
        objetivo = "definicion"

    st.subheader("🧠 Análisis IA del cuerpo")

    if fotos_completas:
        resultados = analisis_ia(imc, objetivo)

        for r in resultados:
            st.write("-", r)
    else:
        st.warning("Sube las 4 fotos para mejor análisis")

    # RUTINA (igual que antes)
    pecho = ["Press banca", "Press inclinado", "Aperturas", "Cruce poleas"]
    pierna = ["Sentadilla", "Prensa", "Peso muerto", "Zancadas", "Hip thrust"]
    core = ["Crunch", "Plancha"]

    st.subheader("🏋️ Recomendación rápida")

    for e in elegir(pecho + pierna + core, 6, objetivo):
        st.write("-", e)
