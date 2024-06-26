import subprocess
def ping_host(host, count=1):
    comando = ["ping", f"-c {count}", host]
    try:
        result = subprocess.run(comando, capture_output=True, text=True, check=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)

def ttl_valor(valor):
    for w in valor.split():
        if w.lower().startswith("ttl="):
            return w
    return None

def identOS(ttl):
    WIN = 128
    LINUX = 64

    w = abs(ttl - WIN)
    l = abs(ttl - LINUX)
    if w < l:
        print("Alta probabilidad que sea un sistema Windows o derivado")
    elif l < w:
        print("Alta probabilidad que sea un sistema Unix o deribado")

host = '147.83.159.160'
salida = ttl_valor(ping_host(host))
print(salida)
if salida:
    s = salida.split('=')
    ttl = int(s[1])
    identOS(ttl)
