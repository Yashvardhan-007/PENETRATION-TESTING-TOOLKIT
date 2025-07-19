import requests
from utils import logger

def enumerate_subdomains(domain, wordlist):
    logger.info(f"Enumerating subdomains for: {domain}")
    for word in wordlist:
        subdomain = f"http://{word}.{domain}"
        try:
            response = requests.get(subdomain, timeout=2)
            if response.status_code < 400:
                logger.info(f"Discovered: {subdomain}")
        except:
            pass
