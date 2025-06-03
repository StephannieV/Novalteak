import streamlit as st
import pandas as pd

# Verificar si Plotly está instalado
try:
    import plotly.express as px
except ModuleNotFoundError:
    st.error("""
    ❌ El módulo 'plotly' no está instalado.
    
    ▶ Por favor, ejecuta en tu terminal:

        pip install plotly

    💡 Si estás usando Streamlit Cloud, agrega `plotly` en el archivo `requirements.txt`.
    """)
    st.stop()

# Cargar datos desde archivos CSV
try:
    df_ecommerce = pd.read_csv("ecommerce_muebles.csv")
    df_importaciones = pd.read_csv("importaciones_madera.csv")
    df_inclusion = pd.read_csv("inclusion_sector_verde.csv")
    df_valor_muebles = pd.read_csv("industria_muebles_valor.csv")
    df_muebles_lujo_exteriores = pd.read_csv("muebles_lujo_exteriores.csv")
    df_penetracion = pd.read_csv("penetracion_aplicacion_final.csv")
    df_proyeccion_ventas = pd.read_csv("proyeccion_ventas_cliente.csv")
    df_ventas_madera_tropical = pd.read_csv("ventas_madera_tropical.csv")
except FileNotFoundError as e:
    st.error(f"❌ Error al cargar archivos CSV: {e}")
    st.stop()

st.set_page_config(layout="wide")
st.title("📊 Dashboard Interactivo: Muebles y Construcción Sostenible en Canadá")

# Ventas online vs tienda
df_ecommerce.dropna(subset=['Año'], inplace=True)
fig1 = px.bar(df_ecommerce, x='Año', y=['Ventas_online_%', 'Ventas_tienda_%'], barmode='group',
              title="Proporción de Ventas Online vs Tienda (2025)")
st.plotly_chart(fig1, use_container_width=True)

# Producción y exportaciones de madera
fig2 = px.bar(df_importaciones, x='Periodo',
              y=['Reducción_envíos_millones_m3', 'Producción_millones_m3', 'Exportaciones_EEUU_millones_m3'],
              title="Importaciones y Producción de Madera")
st.plotly_chart(fig2, use_container_width=True)

# Inversión gubernamental en construcción verde
fig3 = px.bar(df_inclusion, x='Año',
              y=['Inversión_gobierno_USD_millones', 'CAGR_2020_2024_%', 'CAGR_2025_]()
