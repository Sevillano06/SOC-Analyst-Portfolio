# Fuentes de Datos para el Analista SOC

Una visibilidad completa es fundamental para la defensa. A continuación, se detallan las principales fuentes de telemetría que un analista debe monitorear para detectar y responder a incidentes.

## 1. Logs de Firewall
* **¿Qué información contiene?** Direcciones IP (origen y destino), puertos, protocolos (TCP/UDP), interfaces de red utilizadas, bytes transferidos y la acción tomada por el equipo (permitir, denegar o descartar).
* **¿Por qué es importante?** Es la primera línea de visibilidad en el perímetro y entre segmentos internos de la red. Te permite saber exactamente qué tráfico intenta entrar o salir de tu entorno.
* **¿Qué tipo de incidentes ayuda a detectar?** Escaneos de red (reconocimiento), comunicaciones con servidores de comando y control (C2), intentos de exfiltración de datos masivos y ataques de denegación de servicio (DoS/DDoS).

## 2. Logs de Windows (Event Logs)
* **¿Qué información contiene?** Registros categorizados en Sistema, Seguridad y Aplicación. Incluye IDs de eventos específicos (como 4624 para inicio de sesión exitoso o 4688 para creación de procesos), cuentas de usuario involucradas y hashes de procesos.
* **¿Por qué es importante?** Proporciona la granularidad del "quién, qué y cuándo" a nivel del sistema operativo donde operan la mayoría de los usuarios corporativos. Es esencial para rastrear la actividad a nivel de host.
* **¿Qué tipo de incidentes ayuda a detectar?** Movimiento lateral, escalamiento de privilegios, ejecución de malware (procesos anómalos), ataques *Pass-the-Hash* y evasión de defensas (como cuando un atacante borra los logs).

## 3. Logs de Linux (Syslog, Auth.log)
* **¿Qué información contiene?** Eventos de autenticación (intentos de acceso por SSH, uso del comando `sudo`), mensajes del kernel, ejecución de tareas programadas (`cron`) y registros de demonios o servicios web/bases de datos.
* **¿Por qué es importante?** Linux es la columna vertebral de la mayoría de los servidores críticos, aplicaciones web y contenedores. Asegurar el backend de una empresa requiere un monitoreo profundo de estos sistemas.
* **¿Qué tipo de incidentes ayuda a detectar?** Ataques de fuerza bruta por SSH, acceso de usuarios no autorizados a privilegios `root`, establecimiento de persistencia mediante tareas programadas maliciosas y explotación de vulnerabilidades web que escalan al servidor.

## 4. DNS (Domain Name System)
* **¿Qué información contiene?** El dominio específico que se está consultando, la dirección IP del dispositivo que realiza la consulta, el tipo de registro (A, MX, TXT) y la respuesta entregada por el servidor DNS.
* **¿Por qué es importante?** Es el "directorio telefónico" de internet. Casi todo el malware o tráfico malicioso necesita resolver un nombre de dominio para comunicarse con su creador.
* **¿Qué tipo de incidentes ayuda a detectar?** *DNS Tunneling* (técnica para ocultar exfiltración de datos dentro de consultas DNS), algoritmos de generación de dominios (DGA) usados por ransomware para evadir bloqueos, y navegación hacia sitios de *phishing* recién creados.

## 5. DHCP (Dynamic Host Configuration Protocol)
* **¿Qué información contiene?** La dirección IP asignada, la dirección física del dispositivo (dirección MAC), el nombre del host (*hostname*) y el tiempo de concesión de esa dirección (*lease time*).
* **¿Por qué es importante?** En la respuesta a incidentes, es crucial para retroceder en el tiempo. Si detectas que una IP hizo algo malicioso ayer a las 3:00 PM, el log de DHCP te dirá exactamente qué máquina física (MAC) tenía esa IP en ese minuto exacto.
* **¿Qué tipo de incidentes ayuda a detectar?** Conexión de dispositivos no autorizados a la red corporativa (*Rogue Devices* o *Shadow IT*) y ataques de agotamiento de recursos DHCP (*DHCP Starvation*).

## 6. Proxy
* **¿Qué información contiene?** URLs completas visitadas, métodos HTTP (GET, POST), códigos de estado (200, 404, etc.), *User-Agents* (identificador del navegador o aplicación) y la categorización del sitio web.
* **¿Por qué es importante?** A diferencia de un firewall tradicional que solo ve IPs y puertos, el proxy proporciona visibilidad profunda a nivel de aplicación (Capa 7) sobre el tráfico web de los empleados.
* **¿Qué tipo de incidentes ayuda a detectar?** Descargas invisibles de malware (*drive-by downloads*), herramientas maliciosas encubiertas en *User-Agents* extraños, y exfiltración de datos hacia plataformas de almacenamiento personal.

## 7. VPN (Virtual Private Network)
* **¿Qué información contiene?** Cuenta de usuario, dirección IP pública de origen (desde dónde se conecta), dirección IP privada asignada, marcas de tiempo de conexión y desconexión, y volumen de datos transferidos.
* **¿Por qué es importante?** Monitorea la puerta de acceso remoto a la red interna. Con el trabajo remoto, la VPN es uno de los objetivos más buscados por los atacantes para obtener un acceso corporativo inicial.
* **¿Qué tipo de incidentes ayuda a detectar?** Compromiso de credenciales corporativas (ej. un inicio de sesión desde Perú y 10 minutos después uno desde Rusia, conocido como "Viaje Imposible"), ataques de fuerza bruta (*Password Spraying*) y conexiones en horarios anómalos.

## 8. Correo electrónico
* **¿Qué información contiene?** Remitente, destinatario, asunto del correo, direcciones IP de los servidores de tránsito, enlaces (URLs) dentro del cuerpo del mensaje, y nombres/hashes de los archivos adjuntos.
* **¿Por qué es importante?** El correo electrónico sigue siendo, estadísticamente, el vector de acceso inicial número uno para los ciberataques en el mundo empresarial.
* **¿Qué tipo de incidentes ayuda a detectar?** Campañas de *Phishing* masivo, ataques dirigidos de *Spear-Phishing*, compromiso de correos corporativos (BEC - *Business Email Compromise*) y distribución de malware a través de documentos con macros habilitadas.

## 9. Active Directory (AD)
* **¿Qué información contiene?** Eventos de autenticación (Kerberos y NTLM), creación o eliminación de cuentas de usuario, modificaciones en grupos de seguridad (especialmente grupos de administradores), bloqueos de cuentas y cambios en políticas de grupo (GPO).
* **¿Por qué es importante?** AD es el corazón de la gestión de identidades y accesos en un entorno Windows empresarial. Quien controla el Active Directory, controla toda la empresa.
* **¿Qué tipo de incidentes ayuda a detectar?** Intentos de escalamiento de privilegios, ataques de robo de tickets Kerberos (*Golden Ticket*, *Kerberoasting*), creación de cuentas *backdoor* para mantener persistencia y compromiso de cuentas de administrador de dominio.

## 10. Cloud (AWS, Azure, GCP)
* **¿Qué información contiene?** Logs de auditoría a nivel de API (ej. AWS CloudTrail). Incluye la identidad que realiza la acción (Usuario/Rol IAM), llamadas específicas a la API, la IP de origen, la región geográfica y el recurso modificado.
* **¿Por qué es importante?** En la nube, el perímetro de red tradicional desaparece. Todo se controla mediante identidades y permisos de API. Una mala configuración aquí puede exponer bases de datos globales en cuestión de segundos.
* **¿Qué tipo de incidentes ayuda a detectar?** Exfiltración de datos desde repositorios mal configurados (como *S3 buckets* públicos), creación no autorizada de máquinas virtuales de alto costo para minería de criptomonedas, y robo o abuso de credenciales de roles en la nube.