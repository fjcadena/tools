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
    for l in configuracion:
        try:
            if l.startswith('subnet '):
                ip = l.split(' ')[1]
                if ip:
                    if es_ip_valida(ip):
                        print(f"{ip} es una ip valida")
                        redes.append(ip)
        except Exception as e:
            print(f"Ocurrio un error: {e}")
    print(f"listado de redes\n{redes}")

def list_ip():
    pass

ruta_fichero = './doc/dhcpd.conf'
config = leer_file_dhcp(ruta_fichero)
subredes(config)