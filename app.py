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

    # CLASIFICACIÓN Y OBJETIVO AUTOMÁTICO
    if imc < 18.5:
        estado = "Bajo peso"
        objetivo = "Ganar masa muscular"
        st.warning("Bajo peso")
    elif imc < 25:
        estado = "Normal"
        objetivo = "Mejorar físico"
        st.success("Peso normal")
    elif imc < 30:
        estado = "Sobrepeso"
        objetivo = "Bajar grasa"
        st.warning("Sobrepeso")
    else:
        estado = "Obesidad"
        objetivo = "Bajar grasa intensivo"
        st.error("Obesidad")

    st.subheader("🎯 Objetivo asignado automáticamente")
    st.write(objetivo)

    # RUTINA SEGÚN OBJETIVO
    st.subheader("🏋️ Rutina personalizada")

    # 🔥 GANAR MASA
    if objetivo == "Ganar masa muscular":

        st.subheader("📅 Lunes: Pecho + Bíceps")
        st.write("- Press banca 4x10")
        st.write("- Press inclinado 4x10")
        st.write("- Aperturas 3x12")
        st.write("- Curl bíceps 4x10")

        st.subheader("📅 Martes: Pierna")
        st.write("- Sentadilla 4x12")
        st.write("- Prensa 4x12")
        st.write("- Peso muerto 3x10")
        st.write("- Curl femoral 3x12")

        st.subheader("📅 Miércoles: Espalda + Tríceps")
        st.write("- Dominadas 4x8")
        st.write("- Remo 4x10")
        st.write("- Fondos 3x10")
        st.write("- Extensión tríceps 3x12")

        st.subheader("📅 Jueves: Hombro")
        st.write("- Press militar 4x10")
        st.write("- Elevaciones 3x12")

        st.subheader("📅 Viernes: Pierna")
        st.write("- Sentadilla 4x12")
        st.write("- Peso muerto 4x10")

        st.subheader("📅 Sábado: Core")
        st.write("- Abdominales 3x20")

    # 🔥 BAJAR GRASA
    elif "Bajar grasa" in objetivo:

        st.subheader("📅 Lunes: Full Body")
        st.write("- Sentadilla 4x12")
        st.write("- Press banca 3x10")
        st.write("- Remo 3x12")
        st.write("- Plancha 3x30s")

        st.subheader("📅 Martes: Cardio")
        st.write("- 40 min caminata")

        st.subheader("📅 Miércoles: Full Body")
        st.write("- Peso muerto 4x10")
        st.write("- Flexiones 3x12")
        st.write("- Abdominales 3x20")

        st.subheader("📅 Jueves: Cardio")
        st.write("- HIIT 20 min")

        st.subheader("📅 Viernes: Full Body")
        st.write("- Sentadilla 4x12")
        st.write("- Press militar 3x10")
        st.write("- Remo 3x12")

        st.subheader("📅 Sábado: Cardio + Core")
        st.write("- 30 min caminata")
        st.write("- Abdominales")

    # 🔥 MANTENIMIENTO
    else:

        st.subheader("📅 Lunes: Pecho + Bíceps")
        st.write("- Press banca 4x10")
        st.write("- Curl bíceps 4x10")

        st.subheader("📅 Miércoles: Espalda + Tríceps")
        st.write("- Dominadas 4x8")
        st.write("- Fondos 3x10")

        st.subheader("📅 Viernes: Pierna")
        st.write("- Sentadilla 4x12")

    st.subheader("😴 Domingo: Descanso")
