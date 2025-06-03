import streamlit as st
import pandas as pd

# Cargar datos desde archivos CSV locales o desde variables

# Cargar los archivos CSV
df_ecommerce = pd.read_csv("ecommerce_muebles.csv")
df_importaciones = pd.read_csv("importaciones_madera.csv")
df_inclusion = pd.read_csv("inclusion_sector_verde.csv")
df_valor_muebles = pd.read_csv("industria_muebles_valor.csv")
df_muebles_lujo_exteriores = pd.read_csv("muebles_lujo_exteriores.csv")
df_penetracion = pd.read_csv("penetracion_aplicacion_final.csv")
df_proyeccion_ventas = pd.read_csv("proyeccion_ventas_cliente.csv")
df_ventas_madera_tropical = pd.read_csv("ventas_madera_tropical.csv")

st.set_page_config(layout="wide")
st.title("Dashboard Interactivo del Sector Mueblero y Construcción Sostenible en Canadá")

# Sección: Ventas online vs tienda
st.subheader("Proporción de Ventas Online vs Tienda")
st.dataframe(df_ecommerce)

# Sección: Producción y exportaciones de madera
st.subheader("Importaciones y Producción de Madera")
st.dataframe(df_importaciones)

# Sección: Inversión gubernamental en construcción verde
st.subheader("Inversión en Construcción Verde y Crecimiento del Sector")
st.dataframe(df_inclusion)

# Sección: Valoración de mercado de muebles
st.subheader("Valor del Mercado de Muebles en Canadá")
st.dataframe(df_valor_muebles)

# Sección: Crecimiento de muebles de lujo y exteriores
st.subheader("Crecimiento Muebles Lujo y Exteriores")
st.dataframe(df_muebles_lujo_exteriores)

# Sección: Penetración por sector
st.subheader("Penetración del Mercado por Sector")
st.dataframe(df_penetracion)

# Sección: Proyecciones de ventas por segmento
st.subheader("Proyecciones de Ventas por Segmento")
st.dataframe(df_proyeccion_ventas)

# Sección: Ventas de madera tropical y lujo
st.subheader("Mercado de Madera Tropical y Muebles de Lujo")
st.dataframe(df_ventas_madera_tropical)

st.markdown("---")
st.caption("Datos basados en proyecciones e informes de 2024-2025. Fuente: Statista, Grand View Research, Expert Market Research, entre otros.")
