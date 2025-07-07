import pandas as pd
import json

# ==============================================================================
# CONFIGURACIÓN INICIAL
# ==============================================================================

archivo_clientes = 'clientes_challenge.csv'
json_nuevos_estado_filename = 'nuevos_contactos.json'
json_existentes_api_filename = 'contactos_existentes_api.json'
excel_filename = 'reporte_final_clientes.xlsx'


# ==============================================================================
# PARTE A: LECTURA Y SIMULACIÓN DE API
# ==============================================================================

try:
    df_contactos = pd.read_csv(archivo_clientes)
    print(f"{archivo_clientes} leído con éxito. Se encontraron {len(df_contactos)} registros.")
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_clientes}' asegurate de tenerlo en la carpeta del proyecto.")
    exit()

# --- Identificar el dominio de correo más frecuente ---
dominios = df_contactos['correo'].dropna().str.split('@').str[1]
if not dominios.empty:
    dominio_mas_frecuente = dominios.mode()[0]
    print(f"El dominio más frecuente para la simulación de API es: @{dominio_mas_frecuente}")
else:
    dominio_mas_frecuente = "" 
    print("No se encontraron correos para determinar un dominio frecuente.")

def simular_api_dinamica(email):
    if isinstance(email, str) and email.lower().endswith(f'@{dominio_mas_frecuente}'):
        return True
    return False

# ==============================================================================
# PROCESAMIENTO DE CONTACTOS (PARA REPORTE EXCEL Y JSON DE API)
# ==============================================================================

contactos_existentes_api = []
contactos_incompletos = []

for index, row in df_contactos.iterrows():
    # Identificar contactos incompletos según la regla de los motivos
    if pd.isna(row['motivo_perdida']) and pd.isna(row['motivo_ganancia']):
        contactos_incompletos.append(row.to_dict())
    else:
        # De los contactos completos, identificar los existentes según la API
        if pd.notna(row['correo']) and simular_api_dinamica(row['correo']):
            contactos_existentes_api.append(row.to_dict())

print("Procesamiento de contactos para reportes finalizado.")
print("-" * 100)

# ==============================================================================
# PARTE B: GENERACIÓN DE ARCHIVOS JSON
# ==============================================================================

df_nuevos_por_estado = df_contactos[df_contactos['estado'] == 'nuevo']
# Se convierten los resultados a una lista de diccionarios
nuevos_contactos_list = df_nuevos_por_estado.to_dict(orient='records')

with open(json_nuevos_estado_filename, 'w', encoding='utf-8') as json_file:
    json.dump(nuevos_contactos_list, json_file, indent=4, ensure_ascii=False)
print(f"Se ha creado el archivo '{json_nuevos_estado_filename}' con {len(nuevos_contactos_list)} contactos cuyo estado es 'nuevo'.")

with open(json_existentes_api_filename, 'w', encoding='utf-8') as json_file:
    json.dump(contactos_existentes_api, json_file, indent=4, ensure_ascii=False)
print(f"Se ha creado el archivo '{json_existentes_api_filename}' con {len(contactos_existentes_api)} contactos existentes según la API.")

# ==============================================================================
# PARTE C: CREACIÓN DE REPORTE EN EXCEL
# ==============================================================================

resumen_por_estado = df_contactos['estado'].value_counts().reset_index()
resumen_por_estado.columns = ['Estado', 'Cantidad']
total_incompletos = len(contactos_incompletos)
df_incompletos = pd.DataFrame([{'Métrica': 'Contactos con datos incompletos', 'Cantidad': total_incompletos}])
df_resumen = pd.DataFrame({
    'Métrica': [f"Contactos {estado.capitalize()}" for estado in resumen_por_estado['Estado']],
    'Cantidad': resumen_por_estado['Cantidad'].tolist()
})
df_resumen = pd.concat([df_resumen, df_incompletos], ignore_index=True)

df_detalle = df_contactos.copy()

def obtener_clasificacion_general(row):
    if pd.isna(row['motivo_perdida']) and pd.isna(row['motivo_ganancia']):
        return 'Datos Incompletos'
    if pd.notna(row['correo']) and simular_api_dinamica(row['correo']):
        return 'Existente (API)'
    else:
        return 'Nuevo (API)'

df_detalle['Clasificacion_General'] = df_detalle.apply(obtener_clasificacion_general, axis=1)

# --- Escritura del archivo Excel ---
with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
    df_resumen.to_excel(writer, sheet_name='Resumen', index=False)
    df_detalle.to_excel(writer, sheet_name='Detalle de Contactos', index=False)

print(f"Se ha creado el reporte en Excel '{excel_filename}'.")
print("-" * 100)
print("\n¡Proceso completado! Revisa los 3 archivos generados.")