import streamlit as st
import random
import pandas as pd

# ===============================
# FUNCIÓN DE EMPAREJAMIENTO
# ===============================
def generar_parejas(participantes):
    asignados = participantes.copy()

    while True:
        random.shuffle(asignados)
        if all(p != a for p, a in zip(participantes, asignados)):
            return dict(zip(participantes, asignados))

# ===============================
# CONFIGURACIÓN
# ===============================
st.set_page_config(page_title="Sorteo Secreto", page_icon="🎁")

st.title("🎁 Sorteo Secreto – Amigo Secreto")
st.write("Cada persona podrá ver solo a quién le tocó, sin ver el sorteo completo.")

# ===============================
# PARTICIPANTES POR DEFECTO
# ===============================
lista_defecto = [
    "Ariana", "Adrian", "Celena", "Javi", "Fabricio",
    "Theo", "Manuel", "Ivonne", "Gustavo", "Isaac", "Fernando"
]

if "participantes" not in st.session_state:
    st.session_state.participantes = lista_defecto.copy()

# Aquí guardamos las parejas (oculto, no visible a usuarios)
if "parejas" not in st.session_state:
    st.session_state.parejas = None

# ===============================
# GENERAR SORTEO AUTOMÁTICAMENTE
# ===============================
if st.session_state.parejas is None:
    if len(st.session_state.participantes) >= 2:
        st.session_state.parejas = generar_parejas(st.session_state.participantes)
        st.success("🎉 El sorteo ha sido realizado automáticamente.")
    else:
        st.error("Se necesitan al menos 2 participantes para generar el sorteo.")

# ===============================
# CONSULTAR RESULTADO INDIVIDUAL
# ===============================
st.write("---")
st.subheader("👤 Ver tu participante (solo tú lo ves)")

nombre = st.text_input("Escribe tu nombre exactamente como aparece en la lista:")

if st.button("Ver mi resultado"):
    if st.session_state.parejas is None:
        st.error("El sorteo aún no está generado.")
    else:
        if nombre in st.session_state.parejas:
            asignado = st.session_state.parejas[nombre]
            st.success(f"🎁 **{nombre}**, tu participante secreto es: **{asignado}** 🎉")
        else:
            st.error("Ese nombre no está en la lista de participantes.")

# ===============================
# NOTA FINAL
# ===============================
st.write("---")
st.info("El sorteo se genera automáticamente y no puede verse la lista completa. Cada persona solo puede ver su propio resultado.")

