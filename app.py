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

    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open(frente), caption="Frente")
        st.image(Image.open(lado_izq), caption="Lado izquierdo")

    with col2:
        st.image(Image.open(espalda), caption="Espalda")
        st.image(Image.open(lado_der), caption="Lado derecho")
else:
    st.warning("⚠️ Sube las 4 fotos para análisis completo")

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

# IA SIMULADA
def analisis_ia(imc, objetivo):
    resultado = []

    if objetivo == "masa":
        resultado.append("💪 Necesitas ganar masa muscular")
        resultado.append("🔥 Priorizar ejercicios compuestos")

    elif objetivo == "definicion":
        resultado.append("🔥 Necesitas reducir grasa corporal")
        resultado.append("🏃 Añadir cardio y core")

    else:
        resultado.append("⚖️ Buen estado general")
        resultado.append("💪 Mejorar definición muscular")

    if imc > 25:
        resultado.append("⚠️ Posible grasa abdominal")
    elif imc < 18.5:
        resultado.append("⚠️ Bajo desarrollo muscular")
    else:
        resultado.append("✅ Composición equilibrada")

    return resultado

# EJERCICIOS
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

if st.button("Analizar, generar y guardar"):

    # CALORÍAS
    if sexo == "Mujer":
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    else:
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5

    # IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)

    st.subheader("🔎 Análisis corporal")
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

    st.subheader("🎯 Objetivo")
    st.write(objetivo)

    # 🧠 IA
    st.subheader("🧠 Análisis IA")

    if fotos_completas:
        resultados = analisis_ia(imc, objetivo)
        for r in resultados:
            st.write("-", r)
    else:
        st.info("Sube las 4 fotos para un análisis más preciso")

    # 🍽️ ALIMENTACIÓN
    st.subheader("🍽️ Alimentación")
    st.write("Proteínas: pollo, huevo, carne, pescado, lentejas")
    st.write("Carbohidratos: arroz, papa, avena, pasta")
    st.write("Grasas: aguacate, frutos secos")

    # LISTAS
    pecho = ["Press banca", "Press inclinado", "Aperturas", "Cruce poleas", "Fondos", "Flexiones"]
    biceps = ["Curl barra", "Curl alterno", "Curl martillo", "Curl concentrado", "Curl polea"]
    espalda = ["Dominadas", "Jalón pecho", "Remo barra", "Remo mancuerna", "Pullover"]
    triceps = ["Fondos", "Extensión polea", "Press francés", "Patada tríceps"]
    hombro = ["Press militar", "Elevaciones laterales", "Frontales", "Pájaros"]
    pierna = ["Sentadilla", "Prensa", "Peso muerto", "Zancadas", "Hip thrust", "Abducciones", "Extensiones", "Curl femoral"]
    core = ["Crunch", "Elevaciones piernas", "Plancha", "Bicicleta"]

    st.subheader("🏋️ Rutina semanal")

    if objetivo == "definicion":

        st.subheader("Lunes: Full Body")
        for e in elegir(pecho + espalda + pierna, 8, objetivo):
            st.write("-", e)

        st.subheader("Martes: Pierna")
        for e in elegir(pierna, 6, objetivo):
            st.write("-", e)

        st.subheader("Miércoles: Torso")
        for e in elegir(pecho + espalda + hombro, 6, objetivo):
            st.write("-", e)

        st.subheader("Jueves: Cardio + Core")
        for e in elegir(core, 4, objetivo):
            st.write("-", e)

        st.subheader("Viernes: Pierna")
        for e in elegir(pierna, 6, objetivo):
            st.write("-", e)

        st.subheader("Sábado: Core")
        for e in elegir(core, 4, objetivo):
            st.write("-", e)

    else:

        st.subheader("Lunes: Pecho + Bíceps")
        for e in elegir(pecho, 4, objetivo):
            st.write("-", e)
        for e in elegir(biceps, 4, objetivo):
            st.write("-", e)

        st.subheader("Martes: Pierna")
        for e in elegir(pierna, 6, objetivo):
            st.write("-", e)

        st.subheader("Miércoles: Espalda + Tríceps")
        for e in elegir(espalda, 4, objetivo):
            st.write("-", e)
        for e in elegir(triceps, 4, objetivo):
            st.write("-", e)

        st.subheader("Jueves: Hombro")
        for e in elegir(hombro, 4, objetivo):
            st.write("-", e)

        st.subheader("Viernes: Pierna")
        for e in elegir(pierna, 6, objetivo):
            st.write("-", e)

        st.subheader("Sábado: Core")
        for e in elegir(core, 4, objetivo):
            st.write("-", e)

    st.subheader("😴 Domingo: Descanso")

    # GUARDAR
    nuevo = pd.DataFrame({
        "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "Peso": [peso],
        "IMC": [round(imc, 2)],
        "Objetivo": [objetivo]
    })

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)
        datos = pd.concat([datos, nuevo], ignore_index=True)
    else:
        datos = nuevo

    datos.to_csv(archivo, index=False)

    st.success("✅ Progreso guardado")

# 📊 GRÁFICAS + ANÁLISIS
if st.button("Ver gráficas de progreso"):

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)

        st.subheader("📈 Peso")
        fig1, ax1 = plt.subplots()
        ax1.plot(datos["Peso"])
        st.pyplot(fig1)

        st.subheader("📈 IMC")
        fig2, ax2 = plt.subplots()
        ax2.plot(datos["IMC"])
        st.pyplot(fig2)

    else:
        st.warning("No hay datos aún")
