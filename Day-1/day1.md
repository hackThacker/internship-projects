- [Task 1: Scan Your Local Network for Open Ports](#task-1-scan-your-local-network-for-open-ports)
- [Objective:](#objective)
- [Tools:](#tools)
- [Guide](#guide)
    - [Installing Nmap](#installing-nmap)
    - [Finding my local IP range](#finding-my-local-ip-range)
    - [Using nmap perform TCP SYN scan](#using-nmap-perform-tcp-syn-scan)
    - [IP addresses and open ports found](#ip-addresses-and-open-ports-found)
    - [Analyzing capture packet](#analyzing-capture-packet)
    - [common services running on those ports](#common-services-running-on-those-ports)
    - [potential security risks](#potential-security-risks)
    - [scan results](#scan-results)
    - [Outcome](#outcome)





## Task 1: Scan Your Local Network for Open Ports

## Objective:
Learn to discover open ports on devices in your local network to understand network exposure.

## Tools:
- **Nmap** (free)
- **Wireshark** (free)

## Guide

1.Install Nmap from official website.
2.Find your local IP range (e.g., 192.168.1.0/24).
3.Run: nmap -sS 192.168.1.0/24 to perform TCP SYN scan.
4.Note down IP addresses and open ports found.
5.Optionally analyze packet capture with Wireshark.
6.Research common services running on those ports.
7.Identify potential security risks from open ports.
8.Save scan results as a text or HTML file.

---

### Installing Nmap
   - Visiting the [Nmap Download](https://nmap.org/download.html) and download the appropriate version for my operating system.
   - Following the installation instructions provided on the website for my platform (Windows, Linux, macOS).
   - verifing the nmap `version`
![nmap-version](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/nmap%20-v%20.png)

---

### Finding my local IP range

![ifconfig](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/ifconfig.png)

---

### Using nmap perform TCP SYN scan
   
- `-sS` is used for a **TCP SYN scan** (also known as a half-open scan).
- `/24` is the **CIDR notation** representing my subnet `192.168.232.1/24` means the first 24 bits are network bits — equivalent to subnet mask `255.255.255.0`

![nmap -sS](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/nmap%20-sS%20.png)

---

### IP addresses and open ports found

🌐 [TCP SYN Report](https://hackThacker.github.io/internship-projects/nmap_tcp_syn.html)


🖥️ Target: 192.168.232.11`

**Open Ports:** `5`  
**Note:** Most other ports are filtered (no response).

| Port  | Protocol | State | Service       |
|-------|----------|-------|---------------|
| 135   | TCP      | Open  | MSRPC         |
| 139   | TCP      | Open  | NetBIOS-SSN   |
| 445   | TCP      | Open  | Microsoft-DS  |
| 2179  | TCP      | Open  | VMRDP         |
| 5357  | TCP      | Open  | WSDAPI        |


 🖥️ Target: 192.168.232.1288`

**Open Ports:** `2`  
**Note:** 998 ports are closed (replied with reset).

| Port | Protocol | State | Service |
|------|----------|-------|---------|
| 21   | TCP      | Open  | FTP     |
| 22   | TCP      | Open  | SSH     |

---

### Analyzing capture packet

- opening `wireshark`
- choising the `eth0` capture the packet on  my interface
- then i used `map -sS 192.168.232.128/24`

![Wireshark Packet Captures](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/wireshark%20packet%20captures.png)

---

### common services running on those ports

🌐 [Common Service Report](https://hackThacker.github.io/internship-projects/common_service.html)

| Port | Protocol | Service       | Product                       | Version         | Description                                                              |
| ---- | -------- | ------------- | ----------------------------- | --------------- | ------------------------------------------------------------------------ |
| 21   | TCP      | FTP           | vsftpd                        | 3.0.5           | File Transfer Protocol — standard for transferring files over a network. |
| 22   | TCP      | SSH           | OpenSSH                       | 10.0p2 Debian 8 | Secure Shell — encrypted remote login and command execution.             |
| 135  | TCP      | MSRPC         | Microsoft Windows RPC         |                 | Remote Procedure Call — used for inter-process communication in Windows. |
| 139  | TCP      | NetBIOS-SSN   | Microsoft Windows NetBIOS-SSN |                 | Session service for Windows file/printer sharing over NetBIOS.           |
| 445  | TCP      | Microsoft-DS  |                               |                 | SMB over TCP/IP — file sharing, Active Directory services.               |
| 2179 | TCP      | VMRDP         |                               |                 | VMware Remote Desktop Protocol — remote access for VMware VMs.           |
| 5357 | TCP      | HTTP (WSDAPI) | Microsoft HTTPAPI httpd       | 2.0             | Web Services on Devices API — device discovery (SSDP/UPnP).              |

---

### potential security risks

| Port | Service       | Potential Risks                                                                                                                                                                                          |
| ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 21   | FTP           | • Transmits data, including credentials, in **plain text** (easy to intercept).<br>• Vulnerable to brute force attacks.<br>• Misconfigured FTP servers can allow unauthorized file access or upload.     |
| 22   | SSH           | • Weak passwords can lead to brute force attacks.<br>• Outdated SSH versions may have vulnerabilities.<br>• Misconfigurations may allow unauthorized access.                                             |
| 135  | MSRPC         | • Often targeted by worms and exploits (e.g., MS03-026).<br>• Can be used for remote code execution if vulnerabilities exist.<br>• Exposure can aid in network reconnaissance.                           |
| 139  | NetBIOS-SSN   | • Can leak sensitive information about network shares.<br>• Vulnerable to SMB relay and man-in-the-middle attacks.<br>• Can be used for unauthorized file sharing access.                                |
| 445  | Microsoft-DS  | • Common target for ransomware and malware (e.g., WannaCry).<br>• Vulnerable SMB implementations can allow remote code execution.<br>• Exposes critical services like file sharing and Active Directory. |
| 2179 | VMRDP         | • May expose VMware virtual machine consoles.<br>• Weak authentication could allow unauthorized VM access.<br>• Potential for lateral movement within virtualized environments.                          |
| 5357 | HTTP (WSDAPI) | • Exposure of device information via SSDP/UPnP can aid attackers.<br>• Can be exploited for network reconnaissance.<br>• Potential attack vector for denial of service or code execution if vulnerable.  |


### scan results

🌐 [TCP SYN Report](https://hackThacker.github.io/internship-projects/nmap_tcp_syn.html)
🌐 [Common Service Report](https://hackThacker.github.io/internship-projects/common_service.html)



### Outcome
 -  Basic network reconnaissance skills; understanding network service exposure