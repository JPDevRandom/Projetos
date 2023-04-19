import socket

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((host, port))
        return True
    except:
        return False

host = 'localhost'

portas = [80, 443, 8080, 3306]

for port in portas:
    if scan_port(host, port):
        print(f"A porta {port} está aberta.")
    else:
        print(f"A porta {port} está fechada.")