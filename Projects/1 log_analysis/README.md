# Resultados del Análisis de Logs - Laboratorio 01

## Objetivo 
Automatizar la ingesta  y el analisis de registros de seguridad  utilizando Python, y diseñar la estructura relacional en SQL para escalar la deteccion de comportamiento anomalos.

## Resumen del Análisis (Python)
Tras procesar el archivo `auth_logs.csv` con nuestro script `log_analyzer.py`, se obtuvieron las siguientes métricas clave de actividad:

- **Total de eventos de autenticación analizados:** 10
- **Intentos de inicio de sesión exitosos (Success):** 5
- **Intentos de inicio de sesión fallidos (Failed):** 5

### Hallazgos Críticos
1. **Usuario más activo:** El usuario `angel` registra la mayor actividad con **3 apariciones** (todas exitosas).
2. **IP más activa:** La dirección IP `192.168.1.10` generó el mayor volumen de tráfico con **3 peticiones**.
3. **Comportamiento sospechoso:** El usuario `juan` desde la IP `192.168.1.20` presenta múltiples intentos fallidos consecutivos antes de lograr un acceso exitoso. Esto amerita monitoreo por posible intento de fuerza bruta menor.

---

## Estructura de Datos Propuesta (SQL)
Para llevar este análisis a gran escala, se diseñó la estructura de la base de datos y las consultas necesarias en `consultas.sql` para responder a preguntas de investigación comunes en un SOC, tales como:
- Identificación de IPs con comportamiento anómalo.
- Conteo de fallas de autenticación por usuario para detectar ataques de fuerza bruta.


## Conclusiones y Mitigacion
 - Se comprobo la viabilidad de usar scripts de Python para el triaje inicial de logs.
 - Se identifico un posible intento de fuerza bruta menor  que requiere agregar la IP 192.168.1.20 a una lista de monitoreo preventivo.