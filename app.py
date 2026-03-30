import streamlit as st

st.title("💪 Asistente Fitness PRO")

# DATOS DEL USUARIO
peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

if st.button("Analizar y ver rutina"):

    # 🔥 CALORÍAS
    calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    # 📊 IMC
    altura_m = altura / 100
    imc = peso / (altura_m ** 2)

    st.subheader("🔎 Análisis corporal")
    st.write("🔥 Calorías diarias:", round(calorias, 2))
    st.write("📊 IMC:", round(imc, 2))

    # Clasificación IMC
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

    # Recomendación
    st.subheader("💡 Recomendación")
    if estado == "Bajo peso":
        st.write("👉 Enfócate en ganar masa muscular")
    elif estado == "Normal":
        st.write("👉 Mantén tu rutina y mejora rendimiento")
    else:
        st.write("👉 Enfócate en perder grasa y hacer cardio")

    # 🏋️ RUTINA COMPLETA
    st.subheader("🏋️ Rutina semanal")

    st.subheader("📅 Lunes: Pecho + Bíceps")
    st.write("Pecho:")
    st.write("- Press de banca 4x10")
    st.write("- Press inclinado 4x10")
    st.write("- Aperturas 3x12")
    st.write("- Cruce de poleas 3x12")
    st.write("Bíceps:")
    st.write("- Curl con barra 4x10")
    st.write("- Curl alterno 3x12")
    st.write("- Curl martillo 3x12")
    st.write("- Curl concentrado 3x10")

    st.subheader("📅 Martes: Pierna completa")
    st.write("- Sentadilla 4x12")
    st.write("- Prensa 4x12")
    st.write("- Peso muerto 3x10")
    st.write("- Curl femoral 3x12")
    st.write("- Extensión de cuádriceps 3x12")
    st.write("- Elevación de talones 4x15")

    st.subheader("📅 Miércoles: Espalda + Tríceps")
    st.write("Espalda:")
    st.write("- Dominadas 4x8")
    st.write("- Jalón al pecho 4x10")
    st.write("- Remo con barra 3x10")
    st.write("- Remo con mancuerna 3x12")
    st.write("Tríceps:")
    st.write("- Fondos 3x10")
    st.write("- Extensión en polea 3x12")
    st.write("- Press francés 3x10")
    st.write("- Patada de tríceps 3x12")

    st.subheader("📅 Jueves: Hombro + Trapecio")
    st.write("- Press militar 4x10")
    st.write("- Elevaciones laterales 3x12")
    st.write("- Elevaciones frontales 3x12")
    st.write("- Pájaros 3x12")
    st.write("- Encogimientos 4x15")

    st.subheader("📅 Viernes: Pierna completa")
    st.write("- Sentadilla 4x12")
    st.write("- Peso muerto 4x10")
    st.write("- Prensa 3x12")
    st.write("- Curl femoral 3x12")
    st.write("- Extensiones 3x12")
    st.write("- Pantorrilla 4x15")

    st.subheader("📅 Sábado: Cardio + Abdominales")
    st.write("Cardio:")
    st.write("- 30-40 min trote o caminata")
    st.write("Abdominales:")
    st.write("- Crunch 3x20")
    st.write("- Elevación de piernas 3x15")
    st.write("- Plancha 3x30s")
    st.write("- Abdominal bicicleta 3x20")

    st.subheader("😴 Domingo: Descanso")
