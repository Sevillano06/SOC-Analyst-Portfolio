#### 📄 Archivo 2: `00-Splunk-Basics/conceptos.md`
*(Este es tu glosario de términos técnicos explicados de forma clara para que cualquier reclutador vea que dominas el vocabulario de ciberseguridad).*

```markdown
# 📖 Glosario de Operaciones de Seguridad (SOC)

Este glosario contiene las definiciones fundamentales estructuradas bajo un enfoque práctico para el análisis y defensa de infraestructura.

### Conceptos de Arquitectura y Equipos
* **SIEM (Security Information and Event Management):** Plataforma tecnológica encargada de centralizar, almacenar y correlacionar registros de actividad para la detección temprana de eventos de seguridad.
* **SOC (Security Operations Center):** El equipo humano, físico e infraestructural encargado de monitorear y defender la postura de seguridad de una organización de forma continua.
* **SOC Analyst:** Profesional especializado en la monitorización de alertas, triaje inicial de eventos y validación de actividades anómalas en la red.
* **Blue Team:** Conjunto de profesionales enfocados en la defensa activa, endurecimiento de sistemas (*hardening*), respuesta a incidentes y análisis forense.
* **Red Team:** Grupo ofensivo que simula tácticas, técnicas y procedimientos de adversarios reales con el fin de evaluar la efectividad de los controles del Blue Team.

### Marcos de Trabajo y Amenazas
* **Threat Hunting:** Búsqueda proactiva e iterativa en los datos y redes para detectar amenazas persistentes avanzadas (APTs) que han evadido las defensas automatizadas.
* **IOC (Indicador de Compromiso):** Evidencia forense en un sistema o red que confirma de manera reactiva que una intrusión ya ha tenido lugar (ej. un hash de archivo comprometido, una IP de Command & Control).
* **IOA (Indicador de Ataque):** Evidencia del comportamiento dinámico de un atacante enfocado en la intención y el estado real de la intrusión mientras ocurre (ej. ejecución de comandos de persistencia, movimientos laterales).
* **MITRE ATT&CK:** Base de conocimiento y matriz global que documenta de forma estandarizada las tácticas, técnicas y procedimientos (TTPs) observados en ciberataques reales.
* **Cyber Kill Chain:** Modelo lineal que describe las fases consecutivas necesarias que un ciberdelincuente debe completar para lograr sus objetivos dentro de un ataque.

### Gestión de Datos e Incidentes
* **Correlation (Correlación):** Lógica matemática y condicional que asocia eventos dispares de múltiples fuentes de datos para identificar un patrón malicioso unificado.
* **Security Event (Evento de Seguridad):** Cualquier cambio de estado detectable en un sistema, red o servicio que sea de interés para la infraestructura (ej. un inicio de sesión).
* **Security Incident (Incidente de Seguridad):** Un evento o conjunto de eventos confirmados que violan de forma directa las políticas de seguridad y comprometen la confidencialidad, integridad o disponibilidad.
* **Alert (Alerta):** Notificación automática generada por una regla de detección cuando la telemetría coincide con un criterio de riesgo predefinido.
* **Log:** Registro secuencial e inmutable de eventos generados por el software o hardware, esencial para el análisis forense y la auditoría.
* **Dashboard (Tablero):** Interfaz gráfica interactiva que compila métricas, gráficos y KPIs basados en búsquedas de logs para proporcionar visualización de estado en tiempo real.

### Terminología Específica de Splunk
* **Search (Búsqueda):** Consulta ejecutada en la base de datos de Splunk (generalmente utilizando SPL) para filtrar, transformar e investigar la telemetría indexada.
* **Index (Índice):** Repositorio o base de datos lógica dentro de Splunk donde se transforman, almacenan y optimizan los logs crudos para consultas rápidas.
* **Source (Fuente):** El origen físico o la ruta específica del archivo de donde Splunk extrae los datos (ej. una ruta de archivo local o un puerto de red).
* **Source Type (Tipo de Fuente):** Clasificación del formato de datos que le indica a Splunk cómo debe parsear, romper las líneas de texto e interpretar los campos del log (ej. `syslog`, `WinEventLog:Security`).
* **Event (Evento en Splunk):** Una única fila o registro individual de datos indexados que contiene una marca de tiempo (*timestamp*) única y su cuerpo de texto crudo.

### Gobierno y Lógica de Control
* **Risk (Riesgo):** La medida que combina la probabilidad de que una amenaza aproveche una vulnerabilidad existente y el impacto negativo que causaría al negocio.
* **Detection Rule (Regla de Detección):** Lógica analítica estructurada (código o query) programada dentro del SIEM encargada de evaluar los datos entrantes para identificar actividad maliciosa conocida.