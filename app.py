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
