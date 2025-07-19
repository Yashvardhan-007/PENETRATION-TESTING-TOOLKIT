import socket
from utils import logger

def scan_ports(target, ports):
    logger.info(f"Scanning {target}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                logger.info(f"Port {port} is OPEN")
            sock.close()
        except Exception as e:
            logger.error(f"Error scanning port {port}: {e}")

