import streamlit as st

st.title("💪 Asistente Fitness Inteligente")

st.write("Ingresa tus datos:")

peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

objetivo = st.selectbox(
    "¿Cuál es tu objetivo?",
    ["Bajar grasa", "Ganar músculo", "Mejorar glúteos"]
)

if st.button("Calcular y recomendar"):
    calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161

    st.subheader("🔎 Resultados")
    st.write("Calorías:", round(calorias, 2))

    st.subheader("🏋️ Recomendación")

    if objetivo == "Bajar grasa":
        st.write("👉 Cardio + entrenamiento full body 3-4 veces por semana")

    elif objetivo == "Ganar músculo":
        st.write("👉 Rutina dividida: pecho, espalda, pierna")

    elif objetivo == "Mejorar glúteos":
        st.write("👉 Hip thrust, sentadilla, peso muerto 2-3 veces por semana")
