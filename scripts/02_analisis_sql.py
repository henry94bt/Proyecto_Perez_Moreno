import pandas as pd
import sqlite3
import os

# Definimos las rutas apuntando a la carpeta 'data'
ruta_excel = os.path.join('data', 'obras_perez_moreno_final.xlsx')
ruta_db = os.path.join('data', 'PerezMoreno_Business_Intelligence.db')

# 1. Comprobar si el Excel existe en la carpeta data
if not os.path.exists(ruta_excel):
    print(f"❌ Error: No se encuentra el archivo en {ruta_excel}")
    print("👉 Ejecuta primero 'scripts/01_crear_datos.py'")
    exit()

# 2. Conexión a la Base de Datos (la guardamos también en la carpeta 'data')
conn = sqlite3.connect(ruta_db)
df = pd.read_excel(ruta_excel)
df.to_sql('obras', conn, if_exists='replace', index=False)

# --- QUERY 1: ANÁLISIS POR ISLA ---
query_islas = """
SELECT 
    Isla,
    COUNT(*) as Num_Proyectos,
    SUM(Gasto) as Gasto_Total,
    ROUND(AVG(Desviacion_Pct), 2) as Desv_Media_Pct
FROM obras
GROUP BY Isla
ORDER BY Gasto_Total DESC
"""

# --- QUERY 2: ALERTAS CRÍTICAS (Outliers) ---
# Aquí buscamos los que se desvían mucho (lo que hablamos de los outliers)
query_alertas = """
SELECT Nombre, Isla, Presupuesto, Gasto, Desviacion_Pct
FROM obras
WHERE Desviacion_Pct > 15 OR Desviacion_Pct < -10
ORDER BY Desviacion_Pct DESC
"""

# 3. Ejecución y Visualización
print("\n🌍 [1] RENDIMIENTO POR ISLAS")
print(pd.read_sql(query_islas, conn))

print("\n🚩 [2] DETECCIÓN DE ANOMALÍAS (Outliers)")
df_alertas = pd.read_sql(query_alertas, conn)
print(df_alertas)

# 4. Lógica de Negocio (El toque del analista)
print("\n" + "="*40)
print("📢 NOTAS DEL ANALISTA PARA DIRECCIÓN")
print("="*40)

for _, row in df_alertas.iterrows():
    if row['Desviacion_Pct'] > 20:
        print(f"⚠️ PELIGRO: '{row['Nombre']}' ({row['Isla']}) tiene un sobrecoste del {row['Desviacion_Pct']}%. Revisar subcontratas.")
    elif row['Desviacion_Pct'] < -5:
        print(f"💎 EXCELENCIA: '{row['Nombre']}' presenta un ahorro del {abs(row['Desviacion_Pct'])}%. Estudiar método de éxito.")

conn.close()