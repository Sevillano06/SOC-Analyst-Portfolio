# Recomendaciones y Remediación (Playbook)

Para prevenir futuros incidentes de esta naturaleza, el equipo SOC recomienda al departamento de TI y Arquitectura implementar los siguientes controles:

1. **Implementar Autenticación Multifactor (MFA):** Requerir MFA obligatorio para todas las cuentas, especialmente las de administradores. Esto neutraliza los ataques de adivinación de contraseñas, ya que el atacante no posee el segundo factor.
2. **Configurar Bloqueo de Cuentas (Account Lockout):** Establecer una política estricta que bloquee temporalmente la cuenta (ej. por 15 minutos) después de 5 intentos fallidos consecutivos de autenticación.
3. **Restricción de Acceso a IP (Geoblocking/Whitelisting):** Limitar el acceso a los servidores de administración únicamente a direcciones IP de confianza o requerir conexión mediante VPN corporativa.
4. **Fortalecer Políticas de Contraseñas:** Auditar las credenciales actuales y forzar la adopción de contraseñas robustas (mínimo 12 caracteres, complejidad).
5. **Generar Alertas Automatizadas en el SIEM:** Configurar una regla en Splunk/SIEM que dispare una alerta de criticidad media si se detectan >5 EventIDs 4625 seguidos de un EventID 4624 hacia la misma cuenta en una ventana de 5 minutos.