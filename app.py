import streamlit as st
import random
import pandas as pd
from datetime import datetime
import os
import matplotlib.pyplot as plt

st.title("💪 Asistente Fitness Inteligente PRO")

archivo = "progreso.csv"

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

# FUNCIÓN SEGURA
def elegir(lista, cantidad):
    if cantidad > len(lista):
        cantidad = len(lista)
    return random.sample(lista, cantidad)

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
    st.write("🔥 Calorías estimadas:", round(calorias, 2))
    st.write("📊 IMC:", round(imc, 2))

    # OBJETIVO
    if imc < 18.5:
        objetivo = "masa"
        st.warning("Bajo peso → Ganar masa muscular")
    elif imc < 25:
        objetivo = "recomposicion"
        st.success("Peso normal → Mejorar físico")
    else:
        objetivo = "definicion"
        st.warning("Sobrepeso → Bajar grasa")

    st.subheader("🎯 Objetivo detectado")
    st.write(objetivo)

    # 🍽️ ALIMENTACIÓN
    st.subheader("🍽️ Alimentación (qué aporta cada alimento)")

    st.write("🔴 PROTEÍNAS (construyen músculo):")
    st.write("- Pollo, huevo, carne, pescado, atún, lentejas")

    st.write("🟡 CARBOHIDRATOS (energía):")
    st.write("- Arroz, papa, avena, pan, pasta")

    st.write("🟢 GRASAS SALUDABLES:")
    st.write("- Aguacate, frutos secos, aceite de oliva")

    if objetivo == "masa":
        st.write("👉 Come más cantidad (superávit calórico)")
    elif objetivo == "definicion":
        st.write("👉 Controla porciones y reduce azúcar")
    else:
        st.write("👉 Mantén equilibrio")

    # LISTAS DE EJERCICIOS
    pecho = ["Press banca", "Press inclinado", "Aperturas", "Cruce poleas", "Fondos", "Flexiones"]
    biceps = ["Curl barra", "Curl alterno", "Curl martillo", "Curl concentrado", "Curl polea"]
    espalda = ["Dominadas", "Jalón pecho", "Remo barra", "Remo mancuerna", "Pullover"]
    triceps = ["Fondos", "Extensión polea", "Press francés", "Patada tríceps"]
    hombro = ["Press militar", "Elevaciones laterales", "Frontales", "Pájaros"]
    pierna = ["Sentadilla", "Prensa", "Peso muerto", "Zancadas", "Hip thrust", "Abducciones"]
    core = ["Crunch", "Elevaciones piernas", "Plancha", "Bicicleta"]

    st.subheader("🏋️ Rutina semanal")

    # 🔥 DEFINICIÓN (full body mejorado)
    if objetivo == "definicion":

        st.subheader("Lunes: Full Body")
        for e in elegir(pecho + espalda + pierna, 8):
            st.write("-", e)

        st.subheader("Martes: Pierna")
        for e in elegir(pierna, 4):
            st.write("-", e)

        st.subheader("Miércoles: Torso")
        for e in elegir(pecho + espalda + hombro, 6):
            st.write("-", e)

        st.subheader("Jueves: Cardio + Core")
        for e in elegir(core, 4):
            st.write("-", e)

        st.subheader("Viernes: Pierna")
        for e in elegir(pierna, 4):
            st.write("-", e)

        st.subheader("Sábado: Core + Cardio")
        for e in elegir(core, 4):
            st.write("-", e)

    # 🔥 MASA / RECOMPOSICIÓN
    else:

        st.subheader("Lunes: Pecho + Bíceps")
        for e in elegir(pecho, 4):
            st.write("-", e)
        for e in elegir(biceps, 4):
            st.write("-", e)

        st.subheader("Martes: Pierna")
        for e in elegir(pierna, 4):
            st.write("-", e)

        st.subheader("Miércoles: Espalda + Tríceps")
        for e in elegir(espalda, 4):
            st.write("-", e)
        for e in elegir(triceps, 4):
            st.write("-", e)

        st.subheader("Jueves: Hombro")
        for e in elegir(hombro, 4):
            st.write("-", e)

        st.subheader("Viernes: Pierna")
        for e in elegir(pierna, 4):
            st.write("-", e)

        st.subheader("Sábado: Core")
        for e in elegir(core, 4):
            st.write("-", e)

    st.subheader("😴 Domingo: Descanso")

    # GUARDAR PROGRESO
    nuevo = pd.DataFrame({
        "Fecha": [datetime.now().strftime("%Y-%m-%d %H:%M")],
        "Peso": [peso],
        "IMC": [round(imc, 2)]
    })

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)
        datos = pd.concat([datos, nuevo], ignore_index=True)
    else:
        datos = nuevo

    datos.to_csv(archivo, index=False)

    st.success("✅ Progreso guardado correctamente")

# 📊 GRÁFICAS
if st.button("Ver gráficas de progreso"):

    if os.path.exists(archivo):
        datos = pd.read_csv(archivo)

        st.subheader("📈 Evolución del peso")
        fig1, ax1 = plt.subplots()
        ax1.plot(datos["Peso"])
        ax1.set_title("Peso")
        ax1.set_xlabel("Registros")
        ax1.set_ylabel("Kg")
        st.pyplot(fig1)

        st.subheader("📈 Evolución del IMC")
        fig2, ax2 = plt.subplots()
        ax2.plot(datos["IMC"])
        ax2.set_title("IMC")
        ax2.set_xlabel("Registros")
        ax2.set_ylabel("IMC")
        st.pyplot(fig2)

    else:
        st.warning("Aún no hay datos guardados")
