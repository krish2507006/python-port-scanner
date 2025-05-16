import socket
import sys

def usage():
    print("Usage: python3 scanner.py HOST MIN_PORT MAX_PORT")
    sys.exit()

if len(sys.argv) != 4:
    usage()

host = sys.argv[1]

# Validate ports
try:
    min_port = int(sys.argv[2])
    max_port = int(sys.argv[3])
    if not (1 <= min_port <= 65535 and 1 <= max_port <= 65535):
        print("Error: Ports must be between 1 and 65535.")
        sys.exit()
    if min_port > max_port:
        print("Error: MIN_PORT cannot be greater than MAX_PORT.")
        sys.exit()
except ValueError:
    print("Error: Ports must be integers.")
    sys.exit()

try:
    ip_address = socket.gethostbyname(host)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
    sys.exit()

print(f"Starting scan on {ip_address} ports {min_port} to {max_port}")

for port_num in range(min_port, max_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    try:
        result = sock.connect_ex((ip_address, port_num))
        if result == 0:
            print(f"Port {port_num} is open")
    except Exception:
        pass
    finally:
        sock.close()

