# Fuentes de Datos para el Analista SOC

## Logs de Firewall
* **Contenido:** IPs, puertos, protocolos, acciones (permitir/denegar).
* **Importancia:** Primera línea de defensa perimetral.
* **Incidentes:** Escaneo de puertos, exfiltración, ataques DoS.

## Logs de Windows (Event Logs)
* **Contenido:** Inicios de sesión (ID 4624/4625), creación de procesos (ID 4688).
* **Importancia:** Visibilidad profunda sobre el comportamiento a nivel de host.
* **Incidentes:** Movimiento lateral, escalamiento de privilegios, ejecución de malware.

## DNS (Domain Name System)
* **Contenido:** Consultas de dominios y respuestas IP.
* **Importancia:** El malware usa DNS para localizar servidores de comando (C2).
* **Incidentes:** Phishing, comunicación con dominios maliciosos, DNS tunneling.

## Correo Electrónico
* **Contenido:** Remitentes, destinatarios, adjuntos, URLs.
* **Importancia:** Sigue siendo el vector de ataque inicial más común.
* **Incidentes:** Phishing, Spear-Phishing, distribución de malware.

*(Nota: Puedes ir ampliando este archivo con Linux, DHCP, Proxy, VPN y Cloud conforme avances).*