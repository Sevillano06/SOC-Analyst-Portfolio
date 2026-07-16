# 04 - Data and Tools for Defense Analysts

## 🎯 Objetivo
Comprender las diversas fuentes de datos de una organización (red, endpoint, servidores y nube) para supervisar la seguridad, detectar amenazas e investigar incidentes correlacionando eventos en entornos híbridos. 

## 🧠 Conceptos principales
- **Análisis Posterior vs. Tiempo Real:** El análisis posterior (Hindsight) permite la comprensión profunda de incidentes pasados, mientras que el análisis en tiempo real busca la detección inmediata y automatizada.
- **Sourcetype:** Es un campo predeterminado que identifica la estructura de datos de un evento, siendo crucial para el parseo y análisis correcto en Splunk.
- **Regla de oro de investigación:** El analista debe investigar primero y bloquear después, ya que la evidencia es más valiosa que la velocidad de respuesta.

## 🛠️ Herramientas vistas
- **Splunk ES (SIEM):** Actúa como la sala de control del estadio, alertando al analista cuando suceden incidentes importantes.
- **Splunk SOAR:** Funciona como un asistente robótico que ejecuta tareas repetitivas y automatiza respuestas después de obtener evidencia.
- **Wireshark / tcpdump:** Sirven como binoculares con zoom para ver el tráfico de red en vivo y realizar inspección profunda de paquetes.
- **CyberChef:** Es la navaja suiza digital del analista, utilizada para traducir, descifrar y transformar datos inusuales.

## 📋 Tipos de logs estudiados
- **Capturas PCAP y Registros de Flujo:** PCAP almacena copias exactas del tráfico para análisis forense profundo, mientras que los flujos (como VPC Flow) capturan metadatos de red con menor volumen.
- **Logs de IDS/IPS:** Monitorean actividad sospechosa; los sistemas IDS solo detectan y alertan fuera de banda, mientras que los IPS actúan en línea para bloquear el tráfico malicioso.
- **Logs de Firewall:** Protegen los límites de la red y son vitales para detectar tráfico inusual, denegaciones excesivas o exfiltración de datos entre diferentes zonas de seguridad.
- **Logs de Endpoints:** Proporcionan alta fidelidad sobre la actividad del usuario y el sistema, permitiendo investigar eventos críticos como bloqueos de cuenta a través del Event ID 4740 en Windows.
- **Logs de Nube:** Incluyen registros como AWS CloudTrail para auditar llamadas de API y Azure AD Sign-in para monitorear inicios de sesión anómalos o ataques de fuerza bruta.

## 💡 Lo que aprendí
- Bloquear una amenaza antes de investigar es un error de novato, ya que se pierde la evidencia forense y el atacante desaparece del radar.
- Ignorar los logs de autenticación es peligroso porque muchos ataques comienzan con credenciales robadas, por lo que siempre se debe verificar quién inició sesión y desde dónde.

## 🚀 Aplicación en un SOC real
En un flujo de investigación real, utilizaría Splunk ES como mi primer filtro para identificar "Eventos Notables" entre todo el ruido del tráfico normal. Ante una alerta de seguridad, revisaría los logs de Firewall e IDS/IPS para rastrear el origen y destino del tráfico sospechoso. Posteriormente, analizaría los logs del Endpoint y los registros de autenticación para confirmar si el ataque logró comprometer una cuenta o escalar privilegios antes de ejecutar playbooks de contención.