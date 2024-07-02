import re
def leer_file_dhcp(path):
    configuracion = []
    try:
        with open(path, 'r') as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea.startswith('#') or not linea:
                    continue
                configuracion.append(linea)
    except FileNotFoundError:
        print(f"El archivo {path} no se encontro")
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    return configuracion

def es_ip_valida(ip):
    patron_ipv4 = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return patron_ipv4.match(ip) is not None


def subredes(configuracion):
    redes = []
    bloque = []
    zone = False
    for l in configuracion:
        try:
            if l.startswith('subnet '):
                ip = l.split(' ')[1]
                if ip:
                    if es_ip_valida(ip):
                        redes.append(ip)
            if l.startswith('host '):
                zone = True
            if zone:
                bloque.append(l)
                if '}' in l:
                    zone = False

        except Exception as e:
            zone = False
            print(f"Ocurrio un error: {e}")
    list_ip(bloque)
    print(f"listado de redes\n{redes}")
    #4print(f" Listado de ips\n{bloque}")

def list_ip(bloque):
    i = 0
    dict_host = {}
    while i < len(bloque):
        salto = 1
        if bloque[i].startswith('host '):
            clave = bloque[i].split(' ')[1]
            if '{' in bloque[i]: # inicio de bloque
                while not ((i + salto > len(bloque)) or ('}' in bloque[i + salto]) or (bloque[i + salto].startswith('fixed-address '))):
                    salto += 1
                if bloque[i + salto].startswith('fixed-address '):
                    valor = bloque[i + salto].split(' ')[1]
                    if valor[-1] == ';':
                        valor = valor[:-1]
            dict_host[clave] = valor
        i += salto
    print(dict_host)
ruta_fichero = './doc/dhcpd.conf'
config = leer_file_dhcp(ruta_fichero)
subredes(config)
