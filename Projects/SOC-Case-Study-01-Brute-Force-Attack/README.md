# SOC Case Study #1: Brute Force Attack Investigation

## 🎯 Objetivo del Proyecto
Documentar y simular el ciclo completo de investigación de un ataque de fuerza bruta, desde el análisis de logs en crudo hasta la redacción del informe de incidente y la propuesta de medidas de mitigación corporativas.

## 📝 Escenario
Se detectó una ráfaga de intentos fallidos de inicio de sesión contra el servidor de autenticación principal enfocados en la cuenta `admin`. Minutos después, se confirmó un acceso exitoso desde la IP atacante. La misión fue confirmar el compromiso y reportar los hallazgos.

## 🛠️ Herramientas y Frameworks Utilizados
* **Markdown:** Para la estructuración profesional de reportes.
* **Git/GitHub:** Para el control de versiones y publicación del portafolio.
* **Archivos CSV:** Para la simulación y análisis manual de logs de eventos de Windows (EventIDs 4624, 4625).
* **MITRE ATT&CK Framework:** Para la categorización de tácticas y técnicas de los adversarios (TA0006, T1110).

## 📁 Estructura de Archivos
* `scenario.md`: Descripción del contexto del incidente.
* `auth_logs.csv`: Conjunto de datos crudos con los logs analizados.
* `timeline.md`: Reconstrucción cronológica de los eventos.
* `incident_report.md`: Documento ejecutivo detallando qué, quién, cómo y el impacto del evento.
* `mitre_mapping.md`: Categorización técnica del comportamiento del atacante.
* `recommendations.md`: Acciones preventivas y correctivas propuestas.

## 🧠 Habilidades Desarrolladas
1. **Análisis de Logs (Log Analysis):** Identificación de patrones de ataque en crudo sin depender exclusivamente de alertas automáticas.
2. **Incident Response (IR):** Redacción de reportes estructurados que traducen datos técnicos en evaluaciones de riesgo (Impacto y Prioridad) para la gerencia.
3. **Threat Intelligence:** Aplicación de metodologías estándar de la industria (MITRE) para describir comportamientos maliciosos.

## 💡 Qué aprendí
Este caso práctico me enseñó que la cacería de amenazas comienza mucho antes de abrir un SIEM. Entender la diferencia entre un evento aislado y una cadena de eventos (como múltiples fallos seguidos de un éxito) es crucial para determinar si un sistema ha sido comprometido o si es solo ruido de red.