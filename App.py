import streamlit as st
import pandas as pd

# Cargar archivos CSV
@st.cache_data
def cargar_datos():
    return {
        "Ecommerce": pd.read_csv("ecommerce_muebles.csv"),
        "Importaciones": pd.read_csv("importaciones_madera.csv"),
        "Inclusion Verde": pd.read_csv("inclusion_sector_verde.csv"),
        "Valor Muebles": pd.read_csv("industria_muebles_valor.csv"),
        "Lujo y Exteriores": pd.read_csv("muebles_lujo_exteriores.csv"),
        "Penetración": pd.read_csv("penetracion_aplicacion_final.csv"),
        "Proyecciones Ventas": pd.read_csv("proyeccion_ventas_cliente.csv"),
        "Ventas Tropical": pd.read_csv("ventas_madera_tropical.csv")
    }

# Configuración de página
st.set_page_config(page_title="Dashboard Sector Mueblero", layout="wide")
st.title("📊 Dashboard del Sector Mueblero y Construcción Sostenible en Canadá")

st.markdown("""
Una mirada directa al comportamiento del mercado, importaciones, inversión y crecimiento.
""")

# Cargar los datos
bd = cargar_datos()

# Mostrar datos en secciones
st.header("🏬 Canales de Venta")
st.dataframe(bd["Ecommerce"], use_container_width=True)

st.header("🌲 Importaciones y Producción de Madera")
st.dataframe(bd["Importaciones"], use_container_width=True)

st.header("📈 Ventas de Madera Tropical y Muebles de Lujo")
st.dataframe(bd["Ventas Tropical"], use_container_width=True)

st.header("💰 Inversión en Construcción Verde y Crecimiento del Sector")
st.dataframe(bd["Inclusion Verde"], use_container_width=True)

st.header("🛋️ Valor del Mercado de Muebles")
st.dataframe(bd["Valor Muebles"], use_container_width=True)

st.header("✨ Crecimiento de Muebles de Lujo y Exteriores")
st.dataframe(bd["Lujo y Exteriores"], use_container_width=True)

st.header("📊 Penetración del Mercado por Sector")
st.dataframe(bd["Penetración"], use_container_width=True)

st.header("📈 Proyecciones de Ventas por Segmento")
st.dataframe(bd["Proyecciones Ventas"], use_container_width=True)

# Pie de página
st.markdown("""
---
**Fuentes:** Statista, Grand View Research, Expert Market Research, Made in CA, Pro Market Reports  
Desarrollado para análisis de mercado y toma de decisiones estratégicas.
""")

