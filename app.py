import streamlit as st

st.title("💪 Asistente Fitness Inteligente")

peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

objetivo = st.selectbox(
    "¿Cuál es tu objetivo?",
    ["Bajar grasa", "Ganar músculo", "Mejorar glúteos"]
)

if st.button("Calcular y recomendar"):
    calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    st.subheader("🔎 Calorías")
    st.write(round(calorias, 2))

    st.subheader("🏋️ Rutina recomendada")

    if objetivo == "Bajar grasa":
        st.write("🔥 Día 1: Full Body")
        st.write("- Sentadilla 3x12")
        st.write("- Flexiones 3x10")
        st.write("- Plancha 3x30s")

        st.write("🔥 Día 2: Cardio")
        st.write("- 30 min caminata o trote")

    elif objetivo == "Ganar músculo":
        st.write("💪 Día 1: Pecho y tríceps")
        st.write("- Press de banca 4x10")
        st.write("- Fondos 3x10")

        st.write("💪 Día 2: Espalda y bíceps")
        st.write("- Dominadas 3x8")
        st.write("- Curl bíceps 3x12")

        st.write("💪 Día 3: Pierna")
        st.write("- Sentadilla 4x12")
        st.write("- Peso muerto 3x10")

    elif objetivo == "Mejorar glúteos":
        st.write("🍑 Día 1: Glúteos")
        st.write("- Hip thrust 4x12")
        st.write("- Sentadilla 4x10")
        st.write("- Abducciones 3x15")

        st.write("🍑 Día 2: Pierna")
        st.write("- Peso muerto 4x10")
        st.write("- Zancadas 3x12")

        st.write("🍑 Día 3: Glúteos")
        st.write("- Hip thrust 4x12")
        st.write("- Patada de glúteo 3x15")
