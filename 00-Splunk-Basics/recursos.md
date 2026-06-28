# 📚 Centro de Recursos y Referencias Técnicas

Este documento centraliza las fuentes de información indispensables que consultaré durante las operaciones cotidianas de análisis, investigación y diseño de detecciones.

---

### 📝 Documentación Tecnológica y de Herramientas

#### [Splunk Official Documentation](https://docs.splunk.com/)
* **Propósito en el SOC:** Manual de cabecera para la sintaxis avanzada de comandos en **SPL (Splunk Processing Language)**. Lo consultaré para optimizar consultas de búsqueda, comandos de agregación (`stats`, `chart`) y comandos de transformación de datos durante incidentes.

#### [Splunk Blogs](https://www.splunk.com/en_us/blog)
* **Propósito en el SOC:** Seguimiento de tendencias, metodologías de ingeniería de detección escritas por el equipo de *Splunk Threat Research*, y despliegue de nuevos casos de uso prácticos para el SIEM.

---

### ⚔️ Inteligencia de Amenazas y Estándares de la Industria

#### [MITRE ATT&CK Framework](https://attack.mitre.org/)
* **Propósito en el SOC:** Mapeo y contextualización de alertas. Utilizaré la matriz para entender el objetivo de un atacante cuando se dispara una regla de detección (ej. si la técnica detectada pertenece a la táctica de *Persistencia* o *Movimiento Lateral*) y diseñar contramedidas efectivas.

#### [CISA Alerts & Advisories](https://www.cisa.gov/news-events/cybersecurity-advisories)
* **Propósito en el SOC:** Fuente primaria de Threat Intelligence sobre vulnerabilidades Zero-Day y campañas activas de grupos APT. La consultaré para extraer **IOCs** (hashes, IPs) y realizar búsquedas retroactivas (*retro-hunting*) en Splunk de forma inmediata.

#### [OWASP Top 10](https://owasp.org/www-project-top-ten/)
* **Propósito en el SOC:** Guía metodológica para comprender los riesgos más críticos en aplicaciones web. Me servirá para modelar búsquedas sobre ataques a servidores web corporativos (identificando firmas de inyecciones, fallos de autenticación, etc.).

---

### 🎓 Desarrollo Profesional y Fundamentos

#### [Cisco Networking Academy](https://www.netacad.com/)
* **Propósito en el SOC:** Base teórica sobre arquitectura de redes, protocolos (TCP/IP, UDP, ICMP) y asignación de puertos. Esencial para interpretar correctamente los logs crudos provenientes de Firewalls y sistemas de detección de intrusos (IDS).