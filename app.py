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

    # 🍽️ ALIMENTACIÓN
    st.subheader("🍽️ Alimentación")

    st.write("🔴 Proteínas: pollo, huevo, carne, pescado, lentejas")
    st.write("🟡 Carbohidratos: arroz, papa, avena, pasta")
    st.write("🟢 Grasas: aguacate, frutos secos")

    if objetivo == "masa":
        st.write("👉 Comer más (superávit calórico)")
    elif objetivo == "definicion":
        st.write("👉 Controlar porciones y reducir azúcares")
    else:
        st.write("👉 Mantener equilibrio")

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

        st.subheader("📈 Evolución del peso")
        fig1, ax1 = plt.subplots()
        ax1.plot(datos["Peso"])
        st.pyplot(fig1)

        st.subheader("📈 Evolución del IMC")
        fig2, ax2 = plt.subplots()
        ax2.plot(datos["IMC"])
        st.pyplot(fig2)

        # 🧠 ANÁLISIS AUTOMÁTICO
        st.subheader("🧠 Análisis de progreso")

        if len(datos) > 1:
            peso_inicial = datos["Peso"].iloc[0]
            peso_actual = datos["Peso"].iloc[-1]

            diferencia = peso_actual - peso_inicial

            st.write(f"Cambio de peso: {round(diferencia,2)} kg")

            objetivo_actual = datos["Objetivo"].iloc[-1]

            if objetivo_actual == "masa":
                if diferencia > 0:
                    st.success("Vas bien: estás ganando masa")
                else:
                    st.warning("Debes comer más para subir masa")

            elif objetivo_actual == "definicion":
                if diferencia < 0:
                    st.success("Vas bien: estás perdiendo grasa")
                else:
                    st.warning("Debes ajustar dieta o cardio")

            else:
                if abs(diferencia) < 1:
                    st.success("Peso estable, buen progreso")
                else:
                    st.warning("Mucho cambio, revisa tu plan")

        else:
            st.info("Necesitas más registros")

    else:
        st.warning("No hay datos aún")
