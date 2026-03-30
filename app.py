import streamlit as st

st.title("💪 Asistente Fitness Inteligente PRO")

# DATOS
sexo = st.selectbox("Sexo", ["Mujer", "Hombre"])

peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

objetivo = st.selectbox(
    "¿Cuál es tu objetivo?",
    ["Bajar grasa", "Ganar masa muscular", "Mejorar glúteos"]
)

if st.button("Analizar y generar rutina"):

    # 🔥 CALORÍAS (adaptado)
    if sexo == "Mujer":
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    else:
        calorias = (10 * peso) + (6.25 * altura) - (5 * edad) + 5

    # 📊 IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)

    st.subheader("🔎 Análisis corporal")
    st.write("🔥 Calorías:", round(calorias, 2))
    st.write("📊 IMC:", round(imc, 2))

    # CLASIFICACIÓN
    if imc < 18.5:
        estado = "Bajo peso"
        st.warning("Bajo peso")
    elif imc < 25:
        estado = "Normal"
        st.success("Peso normal")
    elif imc < 30:
        estado = "Sobrepeso"
        st.warning("Sobrepeso")
    else:
        estado = "Obesidad"
        st.error("Obesidad")

    # 💡 RECOMENDACIÓN
    st.subheader("💡 Recomendación")

    if objetivo == "Bajar grasa":
        st.write("👉 Déficit calórico + cardio")

    elif objetivo == "Ganar masa muscular":
        st.write("👉 Superávit calórico + fuerza")

    elif objetivo == "Mejorar glúteos":
        st.write("👉 Frecuencia alta de tren inferior")

    # 🏋️ RUTINAS ADAPTADAS
    st.subheader("🏋️ Rutina personalizada")

    # 🔥 MUJER (más enfoque glúteo/pierna)
    if sexo == "Mujer":

        if objetivo == "Mejorar glúteos":
            st.subheader("📅 Lunes: Glúteos")
            st.write("- Hip thrust 4x12")
            st.write("- Sentadilla 4x10")
            st.write("- Abducciones 3x15")
            st.write("- Patada de glúteo 3x15")

            st.subheader("📅 Martes: Pierna")
            st.write("- Prensa 4x12")
            st.write("- Peso muerto 4x10")
            st.write("- Zancadas 3x12")

            st.subheader("📅 Miércoles: Glúteos")
            st.write("- Hip thrust 4x12")
            st.write("- Sentadilla sumo 3x12")

            st.subheader("📅 Viernes: Glúteos")
            st.write("- Hip thrust 4x12")
            st.write("- Abducciones 3x15")

        else:
            st.write("Rutina equilibrada con énfasis en tren inferior")

    # 💪 HOMBRE (más enfoque torso)
    else:

        if objetivo == "Ganar masa muscular":
            st.subheader("📅 Lunes: Pecho + Bíceps")
            st.write("- Press banca 4x10")
            st.write("- Curl bíceps 4x10")

            st.subheader("📅 Miércoles: Espalda + Tríceps")
            st.write("- Dominadas 4x8")
            st.write("- Fondos 3x10")

        else:
            st.write("Rutina equilibrada general")
