# Mapeo MITRE ATT&CK

Este incidente ha sido clasificado utilizando el marco de trabajo MITRE ATT&CK para estandarizar la comprensión de las tácticas y técnicas del adversario.

* **Táctica Principal:** `TA0006 - Credential Access` (Acceso a Credenciales). El objetivo inicial del atacante era obtener credenciales válidas para ingresar al sistema.
* **Técnica Específica:** `T1110 - Brute Force` (Fuerza Bruta) y más específicamente la subtécnica `T1110.001 - Password Guessing` (Adivinación de Contraseñas).

**Justificación:** 
Se selecciona la técnica T1110 porque la evidencia en los logs (6 intentos fallidos en menos de 4 minutos seguidos de un éxito) es el comportamiento clásico de un script o herramienta iterando sobre un diccionario de contraseñas comunes contra una sola cuenta de usuario hasta encontrar la correcta.