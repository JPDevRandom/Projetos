import socket

def scan_port(host, port):
    # Cria um objeto socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    # Tenta se conectar ao host na porta específica
    try:
        s.connect((host, port))
        return True
    except:
        return False

# Define o host a ser escaneado
host = 'localhost'

# Define as portas a serem escaneadas
portas = [80, 443, 8080, 3306]

# Loop através das portas e verifica se estão abertas
for port in portas:
    if scan_port(host, port):
        print(f"A porta {port} está aberta.")
    else:
        print(f"A porta {port} está fechada.")