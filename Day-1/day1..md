- [Guide](#guide)
   1. [First Floor](#first-floor-ip)

## Task 1: Scan Your Local Network for Open Ports

## Objective:
Learn to discover open ports on devices in your local network to understand network exposure.

## Tools:
- **Nmap** (free)
- **Wireshark** (free)

### Guide

1.Install Nmap from official website.
2.Find your local IP range (e.g., 192.168.1.0/24).
3.Run: nmap -sS 192.168.1.0/24 to perform TCP SYN scan.
4.Note down IP addresses and open ports found.
5.Optionally analyze packet capture with Wireshark.
6.Research common services running on those ports.
7.Identify potential security risks from open ports.
8.Save scan results as a text or HTML file.

---
1. **Installing Nmap**
   - Visiting the [Nmap Download](https://nmap.org/download.html) and download the appropriate version for my operating system.
   - Following the installation instructions provided on the website for my platform (Windows, Linux, macOS).
   - verifing the nmap `version`
![nmap-version](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/nmap%20-v%20.png)

---

2. **Finding my local IP range** (e.g., 192.168.252.0/24).

![ifconfig](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/ifconfig.png)

---

3. **Using nmap perform TCP SYN scan**
   
- `-sS` is used for a **TCP SYN scan** (also known as a half-open scan).
- `/24` is the **CIDR notation** representing my subnet `192.168.232.1/24` means the first 24 bits are network bits — equivalent to subnet mask `255.255.255.0`

![nmap -sS](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-1/nmap%20-sS%20.png)

---

4. **IP addresses and open ports found**

### 🖥️ Target: `192.168.232.1`

**Open Ports:** `5`  
**Note:** Most other ports are filtered (no response).

| Port  | Protocol | State | Service       |
|-------|----------|-------|---------------|
| 135   | TCP      | Open  | MSRPC         |
| 139   | TCP      | Open  | NetBIOS-SSN   |
| 445   | TCP      | Open  | Microsoft-DS  |
| 2179  | TCP      | Open  | VMRDP         |
| 5357  | TCP      | Open  | WSDAPI        |


### 🖥️ Target: `192.168.232.128`

**Open Ports:** `2`  
**Note:** 998 ports are closed (replied with reset).

| Port | Protocol | State | Service |
|------|----------|-------|---------|
| 21   | TCP      | Open  | FTP     |
| 22   | TCP      | Open  | SSH     |

---
