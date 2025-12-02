import streamlit as st
import json

st.set_page_config(page_title="Sorteo Secreto", layout="centered")

st.title("🎁 Sorteo Secreto")
st.write("Ingresa tu nombre para ver tu participante asignado.")

# Cargar sorteo.json desde GitHub (incluido en el repo)
with open("sorteo.json", "r") as f:
    sorteo = json.load(f)

nombre = st.text_input("Tu nombre:")

# Mostrar botón
if st.button("🔍 Consultar amigo"):
    if nombre:
        nombre = nombre.strip().title()

        if nombre in sorteo:
            asignado = sorteo[nombre]
            st.success(f"🎉 Tu participante asignado es: **{asignado}**")
        else:
            st.error("❌ Nombre no encontrado. Escríbelo exactamente como está en la lista.")
    else:
        st.warning("⚠️ Primero escribe tu nombre antes de consultar.")

# ===============================
# MENSAJE FINAL
# ===============================
st.write("---")
st.info("Este sorteo es permanente. No cambia aunque cierres la app o la recargues.")

