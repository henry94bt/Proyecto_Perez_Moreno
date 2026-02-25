import pandas as pd
import numpy as np
import os

# Aseguramos que la carpeta 'data' exista para no tener errores de ruta
if not os.path.exists('data'):
    os.makedirs('data')

# 1. Datos crudos
datos_completos = [
    {"Nombre": "Oficinas Domingo Alonso", "Isla": "Gran Canaria", "Cat": "Reformas", "Presupuesto": 573635, "Gasto": 610000},
    {"Nombre": "Hospital Perpetuo Socorro", "Isla": "Gran Canaria", "Cat": "Salud", "Presupuesto": 2500000, "Gasto": 2450000},
    {"Nombre": "Zona Comercial Tejeda", "Isla": "Gran Canaria", "Cat": "Urbanizaciones", "Presupuesto": 1800000, "Gasto": 1950000},
    {"Nombre": "Colegio Brains La Pardilla", "Isla": "Gran Canaria", "Cat": "Social", "Presupuesto": 3200000, "Gasto": 3100000},
    {"Nombre": "Edificio Dársena", "Isla": "Gran Canaria", "Cat": "Viviendas", "Presupuesto": 12000000, "Gasto": 11800000},
    {"Nombre": "Pueblo Canario", "Isla": "Gran Canaria", "Cat": "Reformas", "Presupuesto": 2100000, "Gasto": 2300000},
    {"Nombre": "Naves FEAGA (2)", "Isla": "Fuerteventura", "Cat": "Industria", "Presupuesto": 950000, "Gasto": 980000},
    {"Nombre": "Pabellón FEAGA", "Isla": "Fuerteventura", "Cat": "Industria", "Presupuesto": 800000, "Gasto": 750000},
    {"Nombre": "Parque Puerto Rico", "Isla": "Gran Canaria", "Cat": "Urbanizaciones", "Presupuesto": 1200000, "Gasto": 1200000},
    {"Nombre": "Apartamentos Cóndor", "Isla": "Gran Canaria", "Cat": "Reformas", "Presupuesto": 1500000, "Gasto": 1650000},
    {"Nombre": "P.E. Poris de Abona", "Isla": "Tenerife", "Cat": "Energía", "Presupuesto": 18000000, "Gasto": 18500000},
    {"Nombre": "E.S. Cepsa La Hondura", "Isla": "Fuerteventura", "Cat": "Industria", "Presupuesto": 1100000, "Gasto": 1050000},
    {"Nombre": "P.E. Las Colinas", "Isla": "Gran Canaria", "Cat": "Energía", "Presupuesto": 8500000, "Gasto": 8700000},
    {"Nombre": "P.E. La Morra", "Isla": "Tenerife", "Cat": "Energía", "Presupuesto": 6000000, "Gasto": 5900000},
    {"Nombre": "P.E. Tagoro - Risco Blanco", "Isla": "Tenerife", "Cat": "Energía", "Presupuesto": 14000000, "Gasto": 14200000},
    {"Nombre": "E.S. BP Arinaga", "Isla": "Gran Canaria", "Cat": "Industria", "Presupuesto": 900000, "Gasto": 920000},
    {"Nombre": "P.E. Punta Grande", "Isla": "Lanzarote", "Cat": "Energía", "Presupuesto": 4000000, "Gasto": 4100000},
    {"Nombre": "Hotel Santa Mónica Suites", "Isla": "Gran Canaria", "Cat": "Turismo", "Presupuesto": 8000000, "Gasto": 8300000},
    {"Nombre": "Cencosu El Goro (Spar)", "Isla": "Gran Canaria", "Cat": "Industria", "Presupuesto": 8200000, "Gasto": 8100000},
    {"Nombre": "Oficinas Pérez Galdós 53", "Isla": "Gran Canaria", "Cat": "Reformas", "Presupuesto": 400000, "Gasto": 450000},
    {"Nombre": "Parque Tecnológico Fv", "Isla": "Fuerteventura", "Cat": "Industria", "Presupuesto": 7600000, "Gasto": 7800000},
    {"Nombre": "Clínica Vitaldent Gáldar", "Isla": "Gran Canaria", "Cat": "Salud", "Presupuesto": 300000, "Gasto": 320000},
    {"Nombre": "Complejo Juan Grande", "Isla": "Gran Canaria", "Cat": "Medio Ambiente", "Presupuesto": 5000000, "Gasto": 5200000},
    {"Nombre": "Nave Dipacan Telde", "Isla": "Gran Canaria", "Cat": "Industria", "Presupuesto": 1300000, "Gasto": 1250000},
    {"Nombre": "Paseo Playa Honda", "Isla": "Lanzarote", "Cat": "Urbanizaciones", "Presupuesto": 2000000, "Gasto": 2100000},
    {"Nombre": "Carretera GC-130 Tejeda", "Isla": "Gran Canaria", "Cat": "Viales", "Presupuesto": 900000, "Gasto": 950000},
    {"Nombre": "Aparcamiento Av. Rafael Puig", "Isla": "Tenerife", "Cat": "Urbanizaciones", "Presupuesto": 1100000, "Gasto": 1150000},
    {"Nombre": "Viaducto del Rincón (GC-2)", "Isla": "Gran Canaria", "Cat": "Viales", "Presupuesto": 4500000, "Gasto": 4700000},
    {"Nombre": "CEO Mogán (24 Unidades)", "Isla": "Gran Canaria", "Cat": "Social", "Presupuesto": 5500000, "Gasto": 5400000},
    {"Nombre": "Tanatorio Las Rubiesas", "Isla": "Gran Canaria", "Cat": "Social", "Presupuesto": 2800000, "Gasto": 2900000}
]

# 2. Crear DataFrame
df = pd.DataFrame(datos_completos)

# 3. Inyectar Outliers
df.loc[df['Nombre'] == 'P.E. Punta Grande', 'Gasto'] = 9500000 
df.loc[df['Nombre'] == 'Edificio Dársena', 'Gasto'] = 8800000 
df.loc[df['Nombre'] == 'Carretera GC-130 Tejeda', 'Gasto'] = 2100000 

# 4. Columnas Extra para Power BI
df['Estado'] = np.random.choice(['Finalizada', 'En Curso', 'En Pausa'], size=len(df))
df['Desviacion_Pct'] = ((df['Gasto'] - df['Presupuesto']) / df['Presupuesto'] * 100).round(2)

# 5. Guardar
# Guardamos dentro de la carpeta 'data' que creamos antes
ruta_final = os.path.join('data', 'obras_perez_moreno_final.xlsx')
df.to_excel(ruta_final, index=False)

print(f"✅ Datos creados con éxito en '{ruta_final}'")