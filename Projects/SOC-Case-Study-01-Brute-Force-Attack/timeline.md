# Línea de Tiempo del Incidente

La siguiente tabla detalla la secuencia cronológica de los eventos de autenticación sospechosos asociados a la cuenta `admin`.

| Hora (UTC) | Dirección IP Origen | Evento | Estado | Notas del Analista |
| :--- | :--- | :--- | :--- | :--- |
| 09:00:01 | 203.0.113.45 | Intento de inicio de sesión | Fallido | Comienza la ráfaga de intentos. |
| 09:00:15 | 203.0.113.45 | Intento de inicio de sesión | Fallido | Segundo intento en menos de 15 seg. |
| 09:00:33 | 203.0.113.45 | Intento de inicio de sesión | Fallido | |
| 09:01:05 | 203.0.113.45 | Intento de inicio de sesión | Fallido | |
| 09:01:42 | 203.0.113.45 | Intento de inicio de sesión | Fallido | |
| 09:03:15 | 203.0.113.45 | Intento de inicio de sesión | Fallido | |
| **09:04:22** | **203.0.113.45** | **Inicio de sesión** | **Exitoso** | **¡Compromiso de credenciales!** |
| 09:05:01 | 203.0.113.45 | Uso de privilegios | Intento | El atacante intenta usar los privilegios de administrador. |