# Escenario del Incidente: Posible Ataque de Fuerza Bruta

**Fecha de Detección:** 17 de Julio de 2026
**Analista a Cargo:** [Tu Nombre/Usuario]

## Descripción Inicial
El equipo de TI ha reportado una anomalía en el servidor de autenticación principal (SRV-AUTH-01). El sistema de monitoreo detectó una ráfaga de intentos fallidos de inicio de sesión dirigidos específicamente a la cuenta `admin` en un lapso de tiempo muy corto. 

Minutos después de esta ráfaga de errores, los registros muestran un inicio de sesión exitoso hacia la misma cuenta y desde la misma dirección IP de origen.

## Misión del SOC
Como analista SOC de turno, mi objetivo es investigar estos registros de autenticación, reconstruir la línea de tiempo del ataque, determinar si se trata de un ataque de fuerza bruta exitoso o de un falso positivo (como un usuario olvidando su contraseña), y emitir un reporte formal con recomendaciones de mitigación.