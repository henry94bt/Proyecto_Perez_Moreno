import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de la Página
st.set_page_config(page_title="BI Pérez Moreno", layout="wide", page_icon="🏗️")

# Estética personalizada
st.markdown("<style> .main { background-color: #f8f9fa; } </style>", unsafe_allow_html=True)

# 2. Carga de datos segura
@st.cache_data
def load_data():
    # Apuntamos a la carpeta data que creamos
    return pd.read_excel('data/obras_perez_moreno_final.xlsx')

try:
    df = load_data()
except Exception as e:
    st.error(f"❌ No se encuentra el archivo en data/. Asegúrate de correr primero el script de datos.")
    st.stop()

# 3. SIDEBAR - Filtros
st.sidebar.image("https://www.perezmoreno.com/images/logo.png", width=200) 
st.sidebar.header("🕹️ Filtros de Auditoría")

islas = st.sidebar.multiselect("Seleccionar Isla", df['Isla'].unique(), default=df['Isla'].unique())
categorias = st.sidebar.multiselect("Seleccionar Sector", df['Cat'].unique(), default=df['Cat'].unique())

# Filtrado dinámico
df_filtrado = df[(df['Isla'].isin(islas)) & (df['Cat'].isin(categorias))]

# 4. CABECERA
st.title("🏗️ Control de Operaciones - Grupo Pérez Moreno")

# El bloque que me preguntaste (¡Perfecto!)
with st.expander("ℹ️ Notas de la Auditoría (Haz clic para leer)"):
    st.write("""
        Este panel analiza la eficiencia presupuestaria del Grupo Pérez Moreno. 
        - **Colores Rojos:** Proyectos con sobrecoste (Outliers).
        - **Colores Verdes:** Proyectos con ahorro o gestión eficiente.
        - **Treemap:** El tamaño del cuadro indica el presupuesto total invertido.
    """)

st.divider()

# 5. KPIs (Métricas con Delta)
m1, m2, m3 = st.columns(3)
total_gasto = df_filtrado['Gasto'].sum()
desv_media = df_filtrado['Desviacion_Pct'].mean()
obras_riesgo = len(df_filtrado[df_filtrado['Desviacion_Pct'] > 15])

m1.metric("Gasto Total Acumulado", f"{total_gasto:,.0f} €")
m2.metric(
    label="Desviación Media", 
    value=f"{desv_media:.1f} %",
    delta=f"{'⚠️ Riesgo' if desv_media > 10 else '✅ Estable'}",
    delta_color="inverse"
)
m3.metric("Obras en Alerta (>15%)", obras_riesgo)

# 6. GRÁFICOS
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Desviación por Proyecto")
    fig1 = px.bar(df_filtrado, x='Nombre', y='Desviacion_Pct', color='Desviacion_Pct',
                 color_continuous_scale='RdYlGn_r', title="Desviación %")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🗺️ Mapa de Inversión (Treemap)")
    fig2 = px.treemap(df_filtrado, path=['Cat', 'Nombre'], values='Gasto',
                     color='Desviacion_Pct', color_continuous_scale='RdYlGn_r')
    st.plotly_chart(fig2, use_container_width=True)

# 7. TABLA Y DESCARGA
st.subheader("📋 Detalle de Proyectos")
st.dataframe(df_filtrado.sort_values(by="Desviacion_Pct", ascending=False), use_container_width=True)

# Botón de descarga
csv = df_filtrado.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Descargar datos filtrados (CSV)",
    data=csv,
    file_name='auditoria_perez_moreno.csv',
    mime='text/csv',
)