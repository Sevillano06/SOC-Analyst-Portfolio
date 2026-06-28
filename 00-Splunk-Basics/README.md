# 🛡️ Fundamentos de SIEM y Gestión de Logs

Este módulo cubre el entendimiento teórico de los sistemas de Gestión de Eventos e Información de Seguridad (SIEM) y la arquitectura básica de Splunk, estableciendo las bases antes de la operación en entornos de laboratorio.

---

## 🔎 Introducción a SIEM

### ¿Qué es un SIEM?
Un **SIEM** (Security Information and Event Management) es una plataforma centralizada que recolecta, normaliza y analiza registros de actividad (logs) generados por toda la infraestructura tecnológica de una organización (servidores, redes, bases de datos, endpoints). Funciona como el cerebro analítico del Centro de Operaciones de Seguridad (SOC).

### ¿Para qué sirve?
Su propósito principal es proporcionar **visibilidad holística y detección de amenazas en tiempo real**. Permite correlacionar eventos dispersos que, de forma aislada, parecerían inofensivos, transformándolos en alertas de seguridad accionables.

### ¿Por qué las empresas utilizan SIEM?
Debido a la complejidad de las redes modernas, inspeccionar cada firewall, servidor o antivirus de manera independiente es inviable. Las empresas implementan un SIEM para centralizar la telemetría, acelerar la respuesta ante incidentes, reducir el tiempo de permanencia del atacante (*Dwell Time*) y cumplir con normativas de auditoría legal (como ISO 27001, PCI-DSS).

### ¿Qué problemas resuelve?
* **Silogismos de información:** Elimina los puntos ciegos unificando logs de diferentes fabricantes.
* **Lentitud en la detección:** Automatiza la búsqueda de patrones maliciosos mediante reglas de correlación.
* **Falta de contexto:** Agrega datos de inteligencia de amenazas (Threat Intelligence) a los eventos locales para facilitar la investigación.

---

## 🔄 Diferencias Clave en el Ecosistema de Seguridad

| Característica | SIEM | Antivirus / EDR | Firewall |
| :--- | :--- | :--- | :--- |
| **Enfoque Principal** | Análisis global, correlación y centralización de logs. | Protección del host (endpoint), detección de malware y procesos. | Control de acceso perimetral y filtrado de tráfico de red. |
| **Acción** | Detecta patrones complejos, genera alertas y centraliza auditorías. | Bloquea, aísla y elimina archivos o ejecuciones sospechosas. | Permite o deniega conexiones basándose en puertos, IPs o reglas. |
| **Visibilidad** | **Toda la infraestructura** (Red, Nube, Servidores, Aplicaciones). | **Local** (Solo el dispositivo donde está instalado). | **Perimetral o Segmentada** (Tráfico que cruza sus interfaces). |

---

## 🎯 Investigación: Ecosistema Splunk

### Productos Principales
* **Splunk Enterprise:** Solución On-Premise que se despliega en la infraestructura propia del cliente para indexar y analizar datos a gran escala.
* **Splunk Cloud:** El mismo motor de análisis de Splunk, pero entregado como un software como servicio (SaaS) completamente administrado en la nube.
* **Splunk Enterprise Security (ES):** El módulo SIEM premium especializado para equipos de seguridad que añade tableros de incidentes, flujos de investigación y frameworks de correlación avanzados.

### Fuentes de Datos Analizadas por el SOC
* **Windows Logs (Security, System, Application, Sysmon):** Monitoreo de creación de procesos, escalada de privilegios e inicios de sesión.
* **Linux Logs (auth.log, syslog):** Auditoría de accesos por SSH, ejecución de comandos con privilegios (`sudo`) y demonios del sistema.
* **Firewall (Cisco, Palo Alto, Fortinet):** Análisis de conexiones bloqueadas, escaneos de puertos y tráfico hacia IPs maliciosas.
* **Active Directory:** Vigilancia sobre modificaciones en grupos de administración, bloqueos de cuentas y ataques de fuerza bruta.
* **Endpoint Data:** Visibilidad directa sobre la actividad en laptops y estaciones de trabajo corporativas.
* **DNS Logs:** Detección de técnicas de exfiltración de datos (DNS Tunneling) o consultas a dominios maliciosos (DGA).
* **Proxy & Web Logs:** Rastreo de navegación de usuarios, intentos de Phishing y ataques dirigidos a aplicaciones web (SQLi, XSS).
* **Cloud Environments (AWS CloudTrail, Azure Monitor):** Monitoreo de cambios de configuración en la infraestructura cloud y accesos API.
* **VPN Logs:** Verificación de teletrabajo legítimo y detección de anomalías como inicios de sesión concurrentes (*Impossible Travel*).

---

## ⚙️ Flujo de Trabajo de un Analista SOC (Tier 1)

```text
[ Recibir Alerta ] 
       ↓
[ Revisar Contexto e Historial de Logs ] 
       ↓
[ Buscar Indicadores de Compromiso (IOCs) ] 
       ↓
[ Investigar Línea de Tiempo del Evento ] 
       ↓
[ Clasificar Incidente (Verdadero vs Falso Positivo) ] 
       ↓
[ Escalar a Tier 2 / Contención ] 
       ↓
[ Documentar y Cerrar Ticket ]