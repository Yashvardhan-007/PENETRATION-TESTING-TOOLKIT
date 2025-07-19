import requests

def enumerate_subdomains(domain, wordlist):
    print(f"\n[*] Enumerating subdomains for: {domain}")
    for word in wordlist:
        subdomain = f"http://{word}.{domain}"
        try:
            response = requests.get(subdomain, timeout=2)
            if response.status_code < 400:
                print(f"[+] Discovered: {subdomain}")
        except:
            pass
