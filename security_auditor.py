import socket

def check_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('your_public_ip', port))
    
    if result == 0:
        print(f"Warning: Port {port} is OPEN!")
    else:
        print(f"Port {port} is safe.")

check_port(22)
check_port(3389)