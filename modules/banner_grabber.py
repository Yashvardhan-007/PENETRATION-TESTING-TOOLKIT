import socket
from utils import logger

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        s.settimeout(2)
        banner = s.recv(1024).decode().strip()
        logger.info(f"{ip}:{port} - {banner}")
    except Exception as e:
        logger.error(f"Could not grab banner for {ip}:{port} - {e}")
    finally:
        s.close()
