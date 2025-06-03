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
st.markdown("""
    <style>
    .main {background-color: #f7f7f7;}
    h1 {color: #1f4e79; font-size: 38px; font-weight: 700;}
    h3 {color: #3e3e3e; margin-top: 20px;}
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 Dashboard del Sector Mueblero y Construcción Sostenible en Canadá")
st.markdown("Una mirada analítica al comportamiento del mercado, importaciones, inversión y crecimiento.")

# Cargar los datos
bd = cargar_datos()

# Función para exportar a Excel
@st.cache_data
def convertir_excel(df):
    from io import BytesIO
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Datos')
    output.seek(0)
    return output

# Diseño profesional: columnas y tabs
with st.container():
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏬 Canales de Venta",
        "🌲 Madera e Importaciones",
        "🏗️ Inversión y Crecimiento",
        "🛋️ Mercado y Segmentación"
    ])

    with tab1:
        st.subheader("📦 Proporción de Ventas Online vs Tienda")
        df = bd["Ecommerce"]
        st.dataframe(df, use_container_width=True)
        if st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="ecommerce_ventas.xlsx"):
            st.success("Archivo exportado correctamente")

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📉 Importaciones y Producción de Madera")
            df = bd["Importaciones"]
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="importaciones_madera.xlsx")
        with col2:
            st.subheader("📈 Ventas Madera Tropical y Muebles de Lujo")
            df = bd["Ventas Tropical"]
            st.dataframe(df, use_container_width=True)
            st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="ventas_madera_tropical.xlsx")

    with tab3:
        st.subheader("💰 Inversión en Construcción Verde y Crecimiento del Sector")
        df = bd["Inclusion Verde"]
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="inclusion_sector_verde.xlsx")

    with tab4:
        st.subheader("💼 Valor del Mercado de Muebles")
        df = bd["Valor Muebles"]
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="valor_mercado_muebles.xlsx")

        st.subheader("✨ Crecimiento de Muebles de Lujo y Exteriores")
        df = bd["Lujo y Exteriores"]
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="lujo_exteriores.xlsx")

        st.subheader("📊 Penetración del Mercado por Sector")
        df = bd["Penetración"]
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="penetracion_sector.xlsx")

        st.subheader("📈 Proyecciones de Ventas por Segmento")
        df = bd["Proyecciones Ventas"]
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Descargar Excel", convertir_excel(df), file_name="proyeccion_ventas.xlsx")

# Footer profesional
st.markdown("""
---
**Fuentes:** Statista, Grand View Research, Expert Market Research, Made in CA, Pro Market Reports  
Desarrollado para análisis de mercado y toma de decisiones estratégicas.
""")
