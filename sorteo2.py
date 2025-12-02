import streamlit as st
import random
import pandas as pd
import json
import os

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
# CARGAR O CREAR PAREJAS
# ===============================
def cargar_parejas():
    if os.path.exists("parejas.json"):
        with open("parejas.json", "r") as f:
            return json.load(f)
    return None

def guardar_parejas(parejas):
    with open("parejas.json", "w") as f:
        json.dump(parejas, f)

# ===============================
# CONFIGURACIÓN
# ===============================
st.set_page_config(page_title="Sorteo Secreto", page_icon="🎁")

st.title("🎁 Sorteo Secreto – Amigo Secreto")


# PARTICIPANTES POR DEFECTO
lista_defecto = [
    "Ariana", "Adrian", "Celena", "Javi", "Fabricio",
    "Theo", "Manuel", "Ivonne", "Gustavo", "Isaac", "Fernando"
]

# Cargar participantes en sesión
if "participantes" not in st.session_state:
    st.session_state.participantes = lista_defecto.copy()

# Cargar parejas persistentes
parejas_guardadas = cargar_parejas()

# Si no hay sorteo guardado → generarlo y guardarlo
if parejas_guardadas is None:
    if len(st.session_state.participantes) >= 2:
        parejas_generadas = generar_parejas(st.session_state.participantes)
        guardar_parejas(parejas_generadas)
        st.session_state.parejas = parejas_generadas
        st.success("🎉 Sorteo generado automáticamente y guardado permanentemente.")
else:
    st.session_state.parejas = parejas_guardadas
    st.info("🔒 Sorteo cargado desde memoria. No cambiará.")

# ===============================
# CONSULTAR RESULTADO INDIVIDUAL
# ===============================
st.write("---")
st.subheader("👤 Ver tu participante")

nombre = st.text_input("Escribe tu nombre:")

if st.button("Ver mi resultado"):
    if nombre in st.session_state.parejas:
        asignado = st.session_state.parejas[nombre]
        st.success(f"🎁 **{nombre}**, tu participante secreto es: **{asignado}** 🎉")
    else:
        st.error("Ese nombre no está en la lista de participantes.")

# ===============================
# MENSAJE FINAL
# ===============================
st.write("---")
st.info("Este sorteo es permanente. No cambia aunque cierres la app o la recargues.")



