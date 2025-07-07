# Prueba Práctica - TS Automatización e Integración de API Simulada

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Objetivo del Proyecto

Este proyecto es la solución a una prueba técnica para el cargo de Analista de Datos e Insight Junior. El objetivo es desarrollar un script en Python que simule un proceso de ETL (Extracción, Transformación y Carga) para la validación, análisis y limpieza de datos de clientes, automatizando la clasificación de registros y la creación de reportes clave para una posterior integración con un sistema CRM.

## Contexto de la prueba

La tarea consiste en:
> Simular una integración entre un sistema externo y un CRM como HubSpot, sin acceso real.
>
> * Parte A: Simular una validación de contactos existentes con una "API ficticia".
>
> * Parte B: Generar un archivo JSON con los nuevos contactos "a crear".
>
> * Parte C: Crear un archivo Excel con un resumen de la información cuantificada de los contactos.

## Aplicación

* **Procesamiento y Clasificación de Datos**: El script lee directamente el archivo de datos `clientes_challenge.csv` y lo procesa para:
    * Identificar y separar registros con **datos incompletos**, bajo la condición de que no exista información en los campos `motivo_perdida` ni `motivo_ganancia`.
    * Utilizar una función que simula una **API de validación de forma dinámica**. El script primero analiza todos los correos, identifica el dominio más frecuente, y lo usa como criterio para clasificar los contactos como "Existentes" en la simulación.

* **Generación de Entregables**: El proceso finaliza con la creación de tres archivos de salida:

    1.  **Archivo JSON de Nuevos Contactos**: Crea un archivo `nuevos_contactos.json` que contiene únicamente los contactos cuyo campo `estado` en el archivo original es "nuevo". Este archivo está listo para ser usado en la creación de nuevos registros en el CRM.
    2.  **Archivo JSON de la Simulación API**: Genera un segundo archivo, `contactos_existentes_api.json`, que contiene los contactos identificados como "existentes" por la simulación de la API (aquellos cuyo correo pertenece al dominio más frecuente).
    3.  **Reporte en Excel**: Genera un reporte completo (`reporte_final_clientes.xlsx`) con dos hojas:
        * **Resumen**: Una tabla que cuantifica los contactos según su `estado` original (`Nuevo`, `Activo`, `Perdido`) y el total de registros con datos incompletos.
        * **Detalle de Contactos**: Una lista completa de todos los contactos del archivo original, cuenta con una columna `Clasificacion_General` que detalla el resultado de la simulación de la API y el estado de integridad de los datos.

Juan Nicolás Ortega Giraldo  
**[LinkedIn](https://www.linkedin.com/in/juan-nicolas-ortega-giraldo-485985265/)**
