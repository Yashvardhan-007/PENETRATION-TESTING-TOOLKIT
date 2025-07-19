from modules import port_scanner, ssh_bruteforcer, ftp_bruteforcer, subdomain_enum, banner_grabber

def menu():
    print("""
[1] Port Scanner
[2] SSH Brute Forcer
[3] FTP Brute Forcer
[4] Subdomain Enumerator
[5] Banner Grabber
[0] Exit
""")

    while True:
        menu()
        choice = input("Choose module: ")
        if choice == '1':
            target = input("Target IP: ")
            ports = list(map(int, input("Ports (comma-separated): ").split(',')))
            port_scanner.scan_ports(target, ports)
        elif choice == '2':
            host = input("SSH Host: ")
            user = input("Username: ")
            password_list = input("Passwords (comma-separated): ").split(',')
            ssh_bruteforcer.ssh_brute_force(host, user, password_list)
        elif choice == '3':
            host = input("FTP Host: ")
            user = input("Username: ")
            password_list = input("Passwords (comma-separated): ").split(',')
            ftp_bruteforcer.ftp_brute_force(host, user, password_list)
        elif choice == '4':
            domain = input("Domain: ")
            wordlist = input("Subdomain wordlist (comma-separated): ").split(',')
            subdomain_enum.enumerate_subdomains(domain, wordlist)
        elif choice == '5':
            ip = input("IP: ")
            port = int(input("Port: "))
            banner_grabber.grab_banner(ip, port)
        elif choice == '0':
            break

if __name__ == "__main__":
    menu()
