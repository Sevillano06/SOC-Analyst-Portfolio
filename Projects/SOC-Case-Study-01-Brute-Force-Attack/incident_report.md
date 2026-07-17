# Informe de Incidente de Seguridad

* **ID del Incidente:** INC-2026-001
* **Analista:** Angel Sevillano
* **Fecha del Reporte:** 17 de Julio de 2026

## Resumen Ejecutivo
Se identificó un compromiso exitoso de la cuenta de administrador del sistema tras un ataque de fuerza bruta/adivinación de contraseñas. El atacante logró evadir los controles perimetrales y accedió al servidor interno `10.0.0.5`.

## Detalles Técnicos
* **¿Qué ocurrió?** Un actor de amenazas ejecutó múltiples intentos de autenticación contra el servidor en un periodo de 4 minutos, culminando en un acceso exitoso y posterior intento de ejecución de acciones privilegiadas.
* **¿Quién fue el usuario afectado?** La cuenta de alto privilegio `admin`.
* **¿Desde qué IP?** El ataque se originó desde la IP externa `203.0.113.45`.
* **¿Qué evidencia apoya tu conclusión?** El archivo `auth_logs.csv` muestra 6 eventos de fallo de inicio de sesión (EventID 4625) continuos seguidos de un evento de éxito (EventID 4624) exactamente desde la misma IP. El espaciado de tiempo (segundos) sugiere el uso de una herramienta automatizada.

## Evaluación de Impacto y Prioridad
* **Impacto Potencial:** Crítico. Al ser la cuenta `admin`, el atacante tiene control total sobre el servidor (10.0.0.5), pudiendo exfiltrar datos, instalar malware o pivotar hacia otras máquinas en la red.
* **Prioridad:** **ALTA**. Requiere respuesta inmediata (aislamiento del host y rotación de credenciales) debido a que el inicio de sesión fue exitoso y hay indicios de actividad post-compromiso.