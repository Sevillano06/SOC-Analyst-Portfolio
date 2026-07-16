import csv 

total_registros = 0 
exitosos = 0
fallidos = 0

conteo_usuarios = {}
conteo_ips = {}


with open('auth_logs.csv','r') as archivo:
    lector = csv.reader(archivo)

    next(lector)


    for fila in lector:
        total_registros +=1

        usuario = fila[1]
        ip = fila[2]
        estado = fila[3]

        if estado == 'Success':
            exitosos += 1
        elif estado == 'Failed':
            fallidos += 1 


        if usuario in conteo_usuarios:
            conteo_usuarios[usuario] += 1
        else:
            conteo_usuarios[usuario] = 1

        if ip in conteo_ips:
            conteo_ips[ip] += 1
        else:
            conteo_ips[ip] = 1


usuario_mas_comun = max(conteo_usuarios , key=conteo_usuarios.get)
veces_usuario = conteo_usuarios[usuario_mas_comun]

ip_mas_comun = max(conteo_ips , key = conteo_ips.get)
veces_ip = conteo_ips[ip_mas_comun]


print("="*40)
print("         Resultados del Analisis:      ")
print("="*40)
print(f"Total de registros analizados : { total_registros} ") 
print(f"Intentos Existosos : {exitosos}")
print(f"Intentos fallidos : {fallidos} ")
print(f"Usuario con mas activdad : {usuario_mas_comun}({veces_usuario} apariciones)")
print(f"Ip con mas actividad : {ip_mas_comun} ({veces_ip} aparaciones)")
print("="*40)