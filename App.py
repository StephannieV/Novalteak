
import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos desde archivos CSV locales o desde variables (ejemplo con CSV)
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
              y=['Inversión_gobierno_USD_millones', 'CAGR_2020_2024_%', 'CAGR_2025_2029_%'],
              title="Inversión en Construcción Verde y Crecimiento del Sector")
st.plotly_chart(fig3, use_container_width=True)

# Valoración de mercado de muebles
fig4 = px.line(df_valor_muebles, x='Año', y='Valor_mercado_USD_mil_millones',
               title="Valor del Mercado de Muebles en Canadá")
st.plotly_chart(fig4, use_container_width=True)

# Crecimiento de muebles de lujo y exteriores
fig5 = px.bar(df_muebles_lujo_exteriores, x='Periodo', y=['Crecimiento_ventas_online_%', 'CAGR_general_%'],
              title="Crecimiento Muebles Lujo y Exteriores")
st.plotly_chart(fig5, use_container_width=True)

# Penetración por sector
fig6 = px.bar(df_penetracion, x='Sector',
              y=['Valor_2025_USD_mil_millones', 'Valor_2030_USD_mil_millones', 'Valor_2025_USD_millones'],
              title="Penetración del Mercado por Sector")
st.plotly_chart(fig6, use_container_width=True)

# Proyecciones de ventas por segmento
fig7 = px.bar(df_proyeccion_ventas, x='Segmento',
              y=['Valor_2024_USD_mil_millones', 'Valor_2025_USD_mil_millones', 'Valor_2032_USD_mil_millones', 'Proyección_2029_USD_mil_millones'],
              title="Proyecciones de Ventas por Segmento")
st.plotly_chart(fig7, use_container_width=True)

# Ventas de madera tropical y lujo
fig8 = px.bar(df_ventas_madera_tropical, x='Periodo',
              y=['Crecimiento_%', 'Proyección_2029_USD_mil_millones', 'Tamaño_mercado_global_tropical_USD_mil_millones',
                 'Proyección_muebles_lujo_USD_millones'],
              title="Mercado de Madera Tropical y Muebles de Lujo")
st.plotly_chart(fig8, use_container_width=True)

st.markdown("---")
st.caption("Datos basados en proyecciones e informes de 2024-2025. Fuente: Statista, Grand View Research, Expert Market Research, entre otros.")

