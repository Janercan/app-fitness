import streamlit as st
import random

st.title("💪 Asistente Fitness Inteligente PRO")

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

if st.button("Analizar y generar rutina"):

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

    st.subheader("🎯 Objetivo")
    st.write(objetivo)

    # 🍽️ ALIMENTACIÓN
    st.subheader("🍽️ Alimentación recomendada")

    st.write("🔴 Proteínas (para músculo):")
    st.write("- Pollo, huevo, carne, pescado, atún, lentejas")

    st.write("🟡 Carbohidratos (energía):")
    st.write("- Arroz, papa, avena, pan, pasta")

    st.write("🟢 Grasas saludables:")
    st.write("- Aguacate, frutos secos, aceite de oliva")

    if objetivo == "masa":
        st.write("👉 Come más cantidad de estos alimentos")

    elif objetivo == "definicion":
        st.write("👉 Reduce azúcares y controla porciones")

    else:
        st.write("👉 Mantén equilibrio entre todos")

    # 📌 BASE DE EJERCICIOS (LISTAS GRANDES)

    pecho_lista = ["Press banca", "Press inclinado", "Aperturas", "Cruce poleas", "Fondos", "Flexiones"]
    biceps_lista = ["Curl barra", "Curl alterno", "Curl martillo", "Curl concentrado", "Curl polea"]
    espalda_lista = ["Dominadas", "Jalón pecho", "Remo barra", "Remo mancuerna", "Pullover"]
    triceps_lista = ["Fondos", "Extensión polea", "Press francés", "Patada tríceps"]
    hombro_lista = ["Press militar", "Elevaciones laterales", "Frontales", "Pájaros"]
    pierna_lista = ["Sentadilla", "Prensa", "Peso muerto", "Zancadas", "Hip thrust", "Abducciones"]
    core_lista = ["Crunch", "Elevaciones piernas", "Plancha", "Bicicleta"]

    # FUNCIÓN PARA ELEGIR 4 EJERCICIOS ALEATORIOS
    def elegir(lista):
        return random.sample(lista, 4)

    # 📅 DISTRIBUCIÓN SEGÚN OBJETIVO

    if objetivo == "masa":
        dias = [
            ("Lunes", "Pecho + Bíceps", elegir(pecho_lista), elegir(biceps_lista)),
            ("Martes", "Pierna", elegir(pierna_lista), []),
            ("Miércoles", "Espalda + Tríceps", elegir(espalda_lista), elegir(triceps_lista)),
            ("Jueves", "Hombro", elegir(hombro_lista), []),
            ("Viernes", "Pierna", elegir(pierna_lista), []),
            ("Sábado", "Core", elegir(core_lista), [])
        ]

    elif objetivo == "definicion":
        dias = [
            ("Lunes", "Full Body", elegir(pecho_lista + espalda_lista), []),
            ("Martes", "Pierna", elegir(pierna_lista), []),
            ("Miércoles", "Torso", elegir(pecho_lista + espalda_lista), []),
            ("Jueves", "Cardio + Core", elegir(core_lista), []),
            ("Viernes", "Pierna", elegir(pierna_lista), []),
            ("Sábado", "Cardio", elegir(core_lista), [])
        ]

    else:
        dias = [
            ("Lunes", "Pecho + Bíceps", elegir(pecho_lista), elegir(biceps_lista)),
            ("Martes", "Pierna", elegir(pierna_lista), []),
            ("Miércoles", "Espalda + Tríceps", elegir(espalda_lista), elegir(triceps_lista)),
            ("Jueves", "Hombro", elegir(hombro_lista), []),
            ("Viernes", "Pierna", elegir(pierna_lista), []),
            ("Sábado", "Core", elegir(core_lista), [])
        ]

    # 🏋️ MOSTRAR RUTINA
    st.subheader("🏋️ Rutina semanal")

    for dia, nombre, lista1, lista2 in dias:
        st.subheader(f"📅 {dia}: {nombre}")
        
        for e in lista1:
            st.write("-", e)

        for e in lista2:
            st.write("-", e)

    st.subheader("😴 Domingo: Descanso")
