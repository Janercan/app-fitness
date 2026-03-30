import streamlit as st

st.title("💪 Asistente Fitness")

peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0)
altura = st.number_input("Altura (cm)", min_value=100.0, max_value=220.0)
edad = st.number_input("Edad", min_value=10, max_value=100)

if st.button("Calcular"):
    calorias = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    st.write("Calorías:", round(calorias, 2))
