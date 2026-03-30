import streamlit as st

st.title("💪 Asistente Fitness Inteligente PRO")

# DATOS
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

objetivo = st.selectbox(
    "¿Cuál es tu objetivo?",
    ["Bajar grasa", "Ganar masa muscular", "Mejorar glúteos"]
)

if st.button("Analizar y generar rutina"):

    # 🔥 CALORÍAS
    calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

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
        st.write("👉 Déficit calórico + cardio + entrenamiento")

    elif objetivo == "Ganar masa muscular":
        st.write("👉 Superávit calórico + entrenamiento de fuerza")

    elif objetivo == "Mejorar glúteos":
        st.write("👉 Enfócate en tren inferior y frecuencia alta")

    # 🏋️ RUTINA ADAPTADA
    st.subheader("🏋️ Rutina personalizada")

    # 🔥 BAJAR GRASA
    if objetivo == "Bajar grasa":
        st.subheader("📅 Lunes: Full Body")
        st.write("- Sentadilla 4x12")
        st.write("- Press de banca 3x10")
        st.write("- Remo 3x12")
        st.write("- Plancha 3x30s")

        st.subheader("📅 Martes: Cardio")
        st.write("- 30-40 min trote")

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
        st.write("- Abdominales 3x20")

    # 💪 GANAR MASA
    elif objetivo == "Ganar masa muscular":
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

    # 🍑 GLÚTEOS
    elif objetivo == "Mejorar glúteos":
        st.subheader("📅 Lunes: Glúteos")
        st.write("- Hip thrust 4x12")
        st.write("- Sentadilla 4x10")
        st.write("- Abducciones 3x15")
        st.write("- Patada de glúteo 3x15")

        st.subheader("📅 Martes: Pierna")
        st.write("- Prensa 4x12")
        st.write("- Peso muerto 4x10")

        st.subheader("📅 Miércoles: Glúteos")
        st.write("- Hip thrust 4x12")
        st.write("- Sentadilla sumo 3x12")

        st.subheader("📅 Jueves: Hombro")
        st.write("- Elevaciones 3x12")

        st.subheader("📅 Viernes: Glúteos")
        st.write("- Hip thrust 4x12")
        st.write("- Abducciones 3x15")

        st.subheader("📅 Sábado: Cardio + Core")
        st.write("- Caminata 30 min")
        st.write("- Abdominales")
