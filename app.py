import streamlit as st

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

    st.subheader("🔎 Análisis corporal")
    st.write("🔥 Calorías:", round(calorias, 2))
    st.write("📊 IMC:", round(imc, 2))

    # OBJETIVO AUTOMÁTICO
    if imc < 18.5:
        objetivo = "Ganar masa muscular"
        st.warning("Bajo peso")
    elif imc < 25:
        objetivo = "Mejorar físico"
        st.success("Peso normal")
    elif imc < 30:
        objetivo = "Bajar grasa"
        st.warning("Sobrepeso")
    else:
        objetivo = "Bajar grasa intensivo"
        st.error("Obesidad")

    st.subheader("🎯 Objetivo automático")
    st.write(objetivo)

    st.subheader("🏋️ Rutina semanal (6 días)")

    # 🔥 LUNES
    st.subheader("📅 Lunes: Pecho + Bíceps")

    if "Bajar grasa" in objetivo:
        st.write("- Press banca 4x12")
        st.write("- Press inclinado 4x12")
        st.write("- Aperturas 4x15")
        st.write("- Flexiones 3x15")
        st.write("Bíceps:")
        st.write("- Curl barra 4x12")
        st.write("- Curl alterno 4x12")
        st.write("- Curl martillo 4x12")
        st.write("- Curl polea 3x15")
    else:
        st.write("- Press banca 4x8")
        st.write("- Press inclinado 4x8")
        st.write("- Aperturas 4x10")
        st.write("- Cruce poleas 4x10")
        st.write("Bíceps:")
        st.write("- Curl barra 4x10")
        st.write("- Curl alterno 4x10")
        st.write("- Curl martillo 4x10")
        st.write("- Curl concentrado 4x10")

    # 🔥 MARTES (PIERNA)
    st.subheader("📅 Martes: Pierna completa")

    if sexo == "Mujer":
        st.write("- Hip thrust 4x12")
        st.write("- Sentadilla 4x10")
        st.write("- Prensa 4x12")
        st.write("- Abducciones 4x15")
    else:
        st.write("- Sentadilla 4x10")
        st.write("- Prensa 4x12")
        st.write("- Peso muerto 4x10")
        st.write("- Curl femoral 4x12")

    # 🔥 MIÉRCOLES
    st.subheader("📅 Miércoles: Espalda + Tríceps")

    st.write("Espalda:")
    st.write("- Dominadas 4x8")
    st.write("- Jalón pecho 4x10")
    st.write("- Remo barra 4x10")
    st.write("- Remo mancuerna 4x10")

    st.write("Tríceps:")
    st.write("- Fondos 4x10")
    st.write("- Extensión polea 4x12")
    st.write("- Press francés 4x10")
    st.write("- Patada tríceps 4x12")

    # 🔥 JUEVES
    st.subheader("📅 Jueves: Hombro + Trapecio")

    st.write("- Press militar 4x10")
    st.write("- Elevaciones laterales 4x12")
    st.write("- Elevaciones frontales 4x12")
    st.write("- Pájaros 4x12")
    st.write("- Encogimientos 4x15")

    # 🔥 VIERNES (PIERNA)
    st.subheader("📅 Viernes: Pierna completa")

    if sexo == "Mujer":
        st.write("- Hip thrust 4x12")
        st.write("- Sentadilla sumo 4x10")
        st.write("- Abducciones 4x15")
        st.write("- Peso muerto 4x10")
    else:
        st.write("- Sentadilla 4x10")
        st.write("- Peso muerto 4x10")
        st.write("- Prensa 4x12")
        st.write("- Curl femoral 4x12")

    # 🔥 SÁBADO
    st.subheader("📅 Sábado: Cardio + Abdominales")

    if "Bajar grasa" in objetivo:
        st.write("- Cardio 40-50 min")
    else:
        st.write("- Cardio 20-30 min")

    st.write("- Crunch 4x20")
    st.write("- Elevación piernas 4x15")
    st.write("- Plancha 4x30s")
    st.write("- Bicicleta 4x20")

    st.subheader("😴 Domingo: Descanso")
