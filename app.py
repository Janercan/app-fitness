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

    st.subheader("🔎 Análisis")
    st.write("Calorías:", round(calorias, 2))
    st.write("IMC:", round(imc, 2))

    # OBJETIVO AUTOMÁTICO
    if imc < 18.5:
        objetivo = "masa"
        st.warning("Bajo peso → Ganar masa")
    elif imc < 25:
        objetivo = "recomposicion"
        st.success("Peso normal → Mejorar físico")
    else:
        objetivo = "definicion"
        st.warning("Sobrepeso → Bajar grasa")
# 🍽️ CONSEJOS DE ALIMENTACIÓN
st.subheader("🍽️ Consejos de alimentación")

if objetivo == "masa":
    st.write("👉 Estás en etapa de ganancia muscular")

    st.write("✔ Comer más calorías de las que gastas")
    st.write("✔ Aumentar proteína (pollo, huevos, carne, pescado)")
    st.write("✔ Incluir carbohidratos (arroz, papa, avena)")
    st.write("✔ Grasas saludables (aguacate, frutos secos)")

    st.write("❌ Evitar comer muy poco")
    st.write("❌ Saltarse comidas")

elif objetivo == "definicion":
    st.write("👉 Estás en etapa de pérdida de grasa")

    st.write("✔ Comer menos calorías de las que gastas")
    st.write("✔ Priorizar proteína (pollo, atún, huevos)")
    st.write("✔ Verduras en todas las comidas")
    st.write("✔ Tomar suficiente agua")

    st.write("❌ Evitar comida chatarra")
    st.write("❌ Evitar bebidas azucaradas")

else:  # recomposición
    st.write("👉 Estás en etapa de mantenimiento/mejora")

    st.write("✔ Comer balanceado")
    st.write("✔ Buena cantidad de proteína")
    st.write("✔ Combinar carbohidratos y grasas saludables")

    st.write("❌ Evitar excesos")
    # 📌 LISTAS DE EJERCICIOS (AQUÍ ESTÁ LA MAGIA)

    if objetivo == "masa":
        pecho = ["Press banca 4x8", "Press inclinado 4x8", "Fondos 4x10", "Aperturas 4x10"]
        biceps = ["Curl barra 4x10", "Curl alterno 4x10", "Curl martillo 4x10", "Curl concentrado 4x10"]
        pierna = ["Sentadilla 4x8", "Prensa 4x10", "Peso muerto 4x8", "Curl femoral 4x10"]
    
    elif objetivo == "definicion":
        pecho = ["Press banca 4x12", "Flexiones 4x15", "Aperturas 4x15", "Cruce poleas 4x15"]
        biceps = ["Curl barra 4x12", "Curl alterno 4x12", "Curl polea 4x15", "Curl martillo 4x12"]
        pierna = ["Sentadilla 4x12", "Zancadas 4x12", "Prensa 4x15", "Saltos 3x15"]

    else:  # recomposición
        pecho = ["Press banca 4x10", "Press inclinado 4x10", "Aperturas 4x12", "Cruce poleas 4x12"]
        biceps = ["Curl barra 4x10", "Curl alterno 4x12", "Curl martillo 4x12", "Curl polea 4x12"]
        pierna = ["Sentadilla 4x10", "Prensa 4x12", "Peso muerto 4x10", "Curl femoral 4x12"]

    # Ajuste MUJER (más glúteo)
    if sexo == "Mujer":
        pierna = ["Hip thrust 4x12", "Sentadilla 4x10", "Abducciones 4x15", "Peso muerto 4x10"]

    # OTROS GRUPOS (constantes pero buenos)
    espalda = ["Dominadas 4x8", "Jalón pecho 4x10", "Remo barra 4x10", "Remo mancuerna 4x10"]
    triceps = ["Fondos 4x10", "Extensión polea 4x12", "Press francés 4x10", "Patada 4x12"]
    hombro = ["Press militar 4x10", "Elevaciones laterales 4x12", "Frontales 4x12", "Pájaros 4x12"]
    trapecio = ["Encogimientos 4x15", "Remo al cuello 4x12", "Face pull 4x12", "Farmer walk 3x30s"]

    # 🏋️ RUTINA
    st.subheader("🏋️ Rutina semanal")

    st.subheader("Lunes: Pecho + Bíceps")
    for e in pecho:
        st.write("-", e)
    for e in biceps:
        st.write("-", e)

    st.subheader("Martes: Pierna")
    for e in pierna:
        st.write("-", e)

    st.subheader("Miércoles: Espalda + Tríceps")
    for e in espalda:
        st.write("-", e)
    for e in triceps:
        st.write("-", e)

    st.subheader("Jueves: Hombro + Trapecio")
    for e in hombro:
        st.write("-", e)
    for e in trapecio:
        st.write("-", e)

    st.subheader("Viernes: Pierna")
    for e in pierna:
        st.write("-", e)

    st.subheader("Sábado: Cardio + Abs")
    if objetivo == "definicion":
        st.write("- Cardio 40-50 min")
    else:
        st.write("- Cardio 20-30 min")

    st.write("- Crunch 4x20")
    st.write("- Elevaciones 4x15")
    st.write("- Plancha 4x30s")
    st.write("- Bicicleta 4x20")

    st.subheader("Domingo: Descanso")
