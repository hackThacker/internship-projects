- [Task 3: Perform a Basic Vulnerability Scan on Your PC.](#task-3-perform-a-basic-vulnerability-scan-on-your-pc)
- [Objective:](#objective)
- [Tools:](#tools)
- [Deliverables:](#deliverables)
- [Guide](#guide)
    - [Installed Nessus Essentials](#installed-nessus-essentials)
    - [Setuping local machine IP](#setuping-local-machine-ip)
    - [Start a full vulnerability scan](#start-a-full-vulnerability-scan)
    - [Wait for scan to complete](#wait-for-scan-to-complete)
    - [Review the report for vulnerabilities and severity](#review-the-report-for-vulnerabilities-and-severity)
    - [Research simple fixes or mitigations for found vulnerabilities](#research-simple-fixes-or-mitigations-for-found-vulnerabilities)
    - [Document the most critical vulnerabilities](#document-the-most-critical-vulnerabilities)
    - [scan Report](#scan-report)
    - [Outcome](#outcome)


## Task 3: Perform a Basic Vulnerability Scan on Your PC.


## Objective:
Use free tools to identify common vulnerabilities on your compute

## Tools:
- **Nessus** (free)

## Deliverables:
Vulnerability scan report with identified issues

## Guide

1.Install OpenVAS or Nessus Essentials.
2.Set up scan target as your local machine IP or localhost.
3.Start a full vulnerability scan.
4.Wait for scan to complete (may take 30-60 mins).
5.Review the report for vulnerabilities and severity.
6.Research simple fixes or mitigations for found vulnerabilities.
7.Document the most critical vulnerabilities.
8.Take screenshots of the scan results

---
### Installed Nessus Essentials

- I Download Nessus from the [official Tenable website](https://www.tenable.com/products/nessus/select-your-operating-system).
- Installing the package using your system's package manager ( `sudo dpkg -i Nessus-10.9.4.deb` on debain).
- Starting the Nessus service: `sudo systemctl start nessusd.service`.
- Accessing Nessus in my browser at `https://localhost:8834` and complete the setup wizard.

![Nessus Installation](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/nessues%20installtion.png)

### Setuping local machine IP

- Opening Nessus in my browser via `https://localhost:8834`.
- Log in and navigate to **New Scan** > **Basic Network Scan**.
- In the **Target** field, I enter MY local machine IP ( `192.168.1.x`).
- Save and launch the scan to analyze own system.

![Nessus Interface](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/nessus-interface.png)



### Start a full vulnerability scan

- There are many templated by default
- Clicking on **New Scan** and choosing **Advanced Scan** / **Basic Network Scan**.
- setting the my IP to **Target**  .
- Save the scan, then  i click **Launch** to start the full vulnerability scan.

![Nessus Scan Templates](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/Nessus-Scanner-SC-Scan-Templates.png)


![Nessus Network Scan](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/nessus-networ-scan.png)

![Nessus Advance Scan](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/nessus-advace-scan.png)


### Wait for scan to complete
- Initiated a network vulnerability scan using Nessus.  
- Scan duration: typically it takes 10–30 minutes depending on target size of network.  
- Please wait for the scan to complete before analyzing results.  
- Review findings once the scan status shows **"Completed"**.

### Review the report for vulnerabilities and severity

![Nessus Vulnerability Found 69](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-3/images/nessus-vulnerabilty-found-69.png)

### Research simple fixes or mitigations for found vulnerabilities

| IP Address     | Critical | High | Medium | Low | Info |
|----------------|----------|------|--------|-----|------|
| 192.168.1.70   | 0        | 0    | 5      | 0   | 32   |
| 192.168.1.72   | 0        | 0    | 1      | 0   | 10   |
| 192.168.1.74   | 14       | 82   | 95     | 16  | 75   |
| 192.168.1.75   | 0        | 0    | 0      | 0   | 5    |

| Plugin ID | Simple Fix / Mitigation |
|---|---|
| 207059 (Expat) | `sudo apt upgrade expat libexpat1` — upgrade to fixed versions.  |
| 201110 (Wget) | ` sudo apt upgrade wget` — update to patched version.  |
| 128475 (Linux kernel) | `s sudo apt upgrade -y` then reboot — install kernel updates.  |
| 206590 (Twisted) | `sudo apt upgrade python‑twisted python3‑twisted` — upgrade twisted packages.  |


### Document the most critical vulnerabilities

| Severity | CVSS v2.0 | VPR Score | EPSS Score | Plugin ID | Name |
|----------|-----------|-----------|-------------|-----------|------|
| Critical | 10.0      | -         | -           | 207059    | Ubuntu 14.04 LTS / 16.04 LTS / 18.04 LTS / 20.04 LTS / 24.04 LTS : Expat vulnerabilities (USN-7000-1) |
| High     | 9.4       | -         | -           | 201110    | Ubuntu 16.04 LTS / 18.04 LTS : Wget vulnerability (USN-6852-2) |
| Critical | 10.0      | -         | -           | 128475    | Ubuntu 16.04 LTS / 18.04 LTS : Linux kernel vulnerabilities (USN-4115-1) |
| High     | 9.0       | -         | -           | 206590    | Ubuntu 14.04 LTS / 16.04 LTS / 18.04 LTS / 20.04 LTS / 22.04 LTS / 24.04 LTS : Twisted vulnerabilities (USN-6988-1) |
| High     | 8.3       | -         | -           | 150155    | Ubuntu 16.04 ESM / 18.04 LTS : Linux kernel vulnerabilities (USN-4979-1) |


### scan Report

- **Network Vulnerabilities Report**: Identified multiple critical and high vulnerabilities across scanned hosts (`Ubuntu kernel`, `OpenSSH`, `Python`).
- **Nessus Remediations Report**: Suggested patches and configuration fixes for all detected vulnerabilities to reduce risk.
- **Next Steps**: Prioritize critical issues, apply vendor patches, and re-scan to verify remediation success.

[Nessus Vulnerabilities](https://hackthacker.github.io/internship-projects/Network_nessus.html)     |  [Nessus Remediations](https://hackthacker.github.io/internship-projects/Nessus_Remediations.html)


### Outcome
 -  Introductory vulnerability assessment experience and understanding of common PC risks.