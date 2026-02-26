# 🏗️ BI & Cost Control - Grupo Pérez Moreno

Sistema integral de Business Intelligence diseñado para la monitorización de costes y detección de anomalías en proyectos de construcción.

## 🚀 Tecnologías Utilizadas
- **Python (Streamlit & Plotly):** Dashboard interactivo para visualización de KPIs y anomalías.
- **SQL (SQLite):** Estructuración de datos y consultas de auditoría para identificar sobrecostes.
- **Power BI:** Reporte corporativo avanzado con modelado de datos DAX.
- **Web Scraping (Experimental):** Investigación inicial para la extracción automatizada de datos de obras.

## 📊 Funcionalidades Clave
- **Detección de Anomalías:** Identificación visual de proyectos con desviaciones superiores al 15%.
- **Análisis por Isla:** Desglose del rendimiento operativo en Canarias.
- **Exportación de Datos:** Botón integrado para descargar informes de auditoría en CSV.

## 📂 Estructura del Proyecto
- `app2.py`: Aplicación principal del Dashboard.
- `scripts/`: Procesos ETL y análisis de base de datos.
- `data/`: Repositorio de datos maestros (Excel y SQLite).
- `powerbi/`: Archivos .pbix con el modelado corporativo.

## 🛠️ Cómo ejecutarlo
1. Instalar dependencias: `pip install -r requirements.txt`
2. Lanzar la app: `streamlit run app2.py`
