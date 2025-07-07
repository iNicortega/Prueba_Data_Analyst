import pandas as pd

# === CARGA DE DATOS ===
ventas_df = pd.read_csv('ventas_challenge.csv')
clientes_df = pd.read_csv('clientes_challenge.csv')

# === LIMPIEZA Y ANÁLISIS DE DATOS VENTAS ===
print("\n=== LIMPIEZA Y ANÁLISIS DE DATOS DE VENTAS ===")

# Duplicados y nulos
print("Duplicados:", ventas_df.duplicated().sum())
ventas_df = ventas_df.drop_duplicates()

print("\nValores nulos:\n", ventas_df.isnull().sum())

# Conversión de fecha y columnas adicionales (Ventas)
ventas_df['fecha'] = pd.to_datetime(ventas_df['fecha'])
ventas_df['total_venta'] = ventas_df['precio_unitario'] * ventas_df['cantidad']
ventas_df['total_margen'] = ventas_df['margen_unitario'] * ventas_df['cantidad']
ventas_df['año_mes'] = ventas_df['fecha'].dt.to_period('M')

# Estadística descriptiva (Ventas)
print("\n--- Estadística Descriptiva Ventas DF ---")
print(ventas_df.describe())

print("\n--- Estadística Categórica ---")
print(ventas_df.describe(include=['object']))

print("\n--- Rango de Fechas ---")
print("Desde:", ventas_df['fecha'].min().date())
print("Hasta:", ventas_df['fecha'].max().date())

# Frecuencias (Ventas)
print("\n--- Productos más frecuentes ---")
print(ventas_df['producto'].value_counts())

print("\n--- Categorías ---")
print(ventas_df['categoria'].value_counts())

print("\n--- Tipos de producto ---")
print(ventas_df['tipo_producto'].value_counts())

# Porcentaje promedio de margen (Ventas)
ventas_df['porcentaje_margen'] = ventas_df['margen_unitario'] / ventas_df['precio_unitario'] * 100
print("\n--- Promedio Porcentaje Margen ---")
print(f"{ventas_df['porcentaje_margen'].mean():.2f}%")

print("\nPrimeras filas de ventas:\n", ventas_df.head())

# === LIMPIEZA Y ANÁLISIS DE DATOS CLIENTES ===
print("\n\n=== LIMPIEZA Y ANÁLISIS DE DATOS DE CLIENTES ===")

# Duplicados y nulos
print("Duplicados:", clientes_df.duplicated().sum())
clientes_df = clientes_df.drop_duplicates()

print("\nValores nulos:\n", clientes_df.isnull().sum())

print("\n--- Estadística Categórica ---")
print(clientes_df.describe(include=['object']))

print("\nPrimeras filas de clientes:\n", clientes_df.head())