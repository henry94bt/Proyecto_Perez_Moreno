import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Pérez Moreno BI", layout="wide", page_icon="🏗️")

# Estilo personalizado simple
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# Carga de datos
@st.cache_data
def load_data():
    df = pd.read_excel('data/obras_perez_moreno_final.xlsx')
    return df

df = load_data()

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("🕹️ Panel de Control")
isla_filter = st.sidebar.multiselect("Selecciona Isla:", df['Isla'].unique(), default=df['Isla'].unique())
cat_filter = st.sidebar.multiselect("Categoría de Obra:", df['Cat'].unique(), default=df['Cat'].unique())

df_filtered = df[(df['Isla'].isin(isla_filter)) & (df['Cat'].isin(cat_filter))]

# --- CABECERA ---
st.title("🏗️ Business Intelligence: Grupo Pérez Moreno")
st.markdown(f"Análisis de **{len(df_filtered)} proyectos** activos en Canarias")

# --- KPIs ---
c1, c2, c3, c4 = st.columns(4)
total_pres = df_filtered['Presupuesto'].sum()
total_gasto = df_filtered['Gasto'].sum()
desv_global = ((total_gasto - total_pres) / total_pres) * 100

c1.metric("Inversión Total", f"{total_pres/1e6:.1f}M €")
c2.metric("Gasto Real", f"{total_gasto/1e6:.1f}M €")
c3.metric("Desviación Global", f"{desv_global:.1f}%", delta=f"{desv_global:.1f}%", delta_color="inverse")
c4.metric("Proyecto Más Crítico", df_filtered.loc[df_filtered['Desviacion_Pct'].idxmax()]['Nombre'])

st.divider()

# --- GRÁFICOS AVANZADOS ---
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("📍 Desviación por Proyecto")
    # Gráfico de barras horizontales
    fig_bar = px.bar(df_filtered.sort_values('Desviacion_Pct'), 
                     x='Desviacion_Pct', y='Nombre', color='Desviacion_Pct',
                     color_continuous_scale='RdYlGn_r', orientation='h',
                     labels={'Desviacion_Pct': 'Desviación (%)'})
    st.plotly_chart(fig_bar, use_container_width=True)

with col_b:
    st.subheader("💰 Eficiencia por Sector")
    # Treemap para ver dónde está el dinero
    fig_tree = px.treemap(df_filtered, path=['Cat', 'Nombre'], values='Gasto',
                          color='Desviacion_Pct', color_continuous_scale='RdYlGn_r')
    st.plotly_chart(fig_tree, use_container_width=True)

# --- TABLA DE DATOS INTERACTIVA ---
st.subheader("📋 Auditoría Detallada")
st.dataframe(df_filtered.sort_values('Desviacion_Pct', ascending=False), use_container_width=True)