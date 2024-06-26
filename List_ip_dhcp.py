import subprocess
import ipaddress

def cat_dhcpd():
    comando = ["grep", "lease", "./doc/dhcpd.leases"]
    try:
        result = subprocess.run(comando, capture_output=True, text=True, check=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def es_ip_valida(cadena):
    try:
        # Intenta crear una dirección IP (IPv4 o IPv6) a partir de la cadena
        ipaddress.ip_address(cadena)
        return True
    except ValueError:
        # Si hay un error de valor, significa que la cadena no es una dirección IP válida
        return False

print("salida")
text = cat_dhcpd()

lista = text.split(' ')
list_ip = []
for t in lista:
    if es_ip_valida(t):
        list_ip.append(t)

print(list_ip)
