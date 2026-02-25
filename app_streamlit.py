import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pérez Moreno Dashboard", layout="wide")
st.title("🏗️ Grupo Pérez Moreno - Control de Costes")

df = pd.read_excel('obras_perez_moreno_final.xlsx')

# KPIs principales
c1, c2, c3 = st.columns(3)
c1.metric("Gasto Total", f"{df['Gasto'].sum():,.0f} €")
c2.metric("Desviación Media", f"{df['Desviacion_Pct'].mean():.2f} %")
c3.metric("Obras Críticas", len(df[df['Desviacion_Pct'] > 15]))

# Gráfico de Dispersión (Detección visual de Outliers)
st.subheader("Análisis de Anomalías (Presupuesto vs Gasto)")
fig = px.scatter(df, x="Presupuesto", y="Gasto", color="Desviacion_Pct",
                 size="Gasto", hover_name="Nombre",
                 color_continuous_scale="RdYlGn_r")
st.plotly_chart(fig, use_container_width=True)