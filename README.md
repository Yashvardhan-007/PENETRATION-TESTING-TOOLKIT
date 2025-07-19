#PENETRATION TESTING TOOLKIT

**COMPANY - CODETECH IT SOLUTIONS

**NAME - YASHVARDHAN SINGH

**INTERN ID - CT06DH2788

**DOMAIN - CYBER SECURITY AND ETHICAL HACKING

**DURATION - 6 WEEKS

**MENTOR - NEELA SANTHOSH KUMAR

DESCRIPTION OF THE TASK

# 🛠️ Penetration Testing Toolkit

A modular, Python-based toolkit for penetration testing and ethical hacking. This toolkit includes essential tools for information gathering and brute-force testing, all bundled into a CLI-based interface.

> ✅ For **educational and authorized testing** only.

---

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules Description](#modules-description)
- [Project Structure](#project-structure)
- [Sample Output](#sample-output)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features

✅ **Port Scanner**  
🔑 **SSH Brute Forcer**  
📁 **FTP Brute Forcer**  
🌐 **Subdomain Enumerator**  
🛡️ **Banner Grabber**

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/pentest_toolkit.git
cd pentest_toolkit
```

 Install Dependencies

pip install -r requirements.txt

▶️ Usage
Run the toolkit using:
python main.py


pentest_toolkit/
├── main.py
├── requirements.txt
├── README.md
├── modules/
│   ├── port_scanner.py
│   ├── ssh_bruteforcer.py
│   ├── ftp_bruteforcer.py
│   ├── subdomain_enum.py
│   └── banner_grabber.py



⚠️ Disclaimer
This tool is intended strictly for educational purposes and authorized security assessments only.

Do NOT use this toolkit on networks, servers, or services without explicit permission.

The author is not responsible for any misuse or damage caused.


🤝 Contributing
Pull requests are welcome! If you’d like to add new modules or enhance existing ones:

1.Fork the repository

2.Create your feature branch (git checkout -b feature-name)

3.Commit your changes (git commit -am 'Add new feature')

4.Push to the branch (git push origin feature-name)

5.Create a new Pull Request


🧪 Sample Output (Main Menu)

[1] Port Scanner
[2] SSH Brute Forcer
[3] FTP Brute Forcer
[4] Subdomain Enumerator
[5] Banner Grabber
[0] Exit
Choose module: 1
Target IP: 192.168.0.1
Ports (comma-separated): 22,80,443
[*] Scanning 192.168.0.1
[+] Port 22 is OPEN
[+] Port 80 is OPEN




