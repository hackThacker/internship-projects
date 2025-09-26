
- [Task 4: Setup and Use a Firewall on Windows/Linux](#task-4-setup-and-use-a-firewall-on-windowslinux)
- [Objective:](#objective)
- [Tools:](#tools)
- [Deliverables:](#deliverables)
- [Guide](#guide)
    - [Open Firewall Configuration Tool](#open-firewall-configuration-tool)
    - [List Current Firewall Rules](#list-current-firewall-rules)
    - [Block Inbound Traffic on Port 23 Telnet](#block-inbound-traffic-on-port-23-telnet)
    - [Test the Block Rule](#test-the-block-rule)
    - [Allow SSH on Port 22 Linux Only](#allow-ssh-on-port-22-linux-only)
    - [Remove the Test Block Rule](#remove-the-test-block-rule)
    - [Commands & GUI Steps Summary](#commands--gui-steps-summary)
    - [How Firewall Filters Traffic](#how-firewall-filters-traffic)
- [Outcome](#outcome)


## Task 4: Setup and Use a Firewall on Windows/Linux


## Objective:
Configure and test basic firewall rules to allow or block traffic

## Tools:
- Windows Firewall / UFW (Uncomplicated Firewall) on Linux

## Deliverables:
Screenshot/configuration file showing firewall rules applied

## Guide

1.Open firewall configuration tool (Windows Firewall or terminal for UFW).

2.List current firewall rules.

3.Add a rule to block inbound traffic on a specific port (e.g., 23 for Telnet).

4.Test the rule by attempting to connect to that port locally or remotely.

5.Add rule to allow SSH (port 22) if on Linux.

6.Remove the test block rule to restore original state

7.Document commands or GUI steps used.

8.Summarize how firewall filters traffic

---

###  Open Firewall Configuration Tool

* **Windows**: Go to *Control Panel > System and Security > Windows Defender Firewall > Advanced Settings*.

![Windows Defender Firewall](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/windows-defender-firewall.png)


* **Linux (UFW)**: Open terminal and type:

  ```bash
  sudo ufw status
  ```
![UFW Status](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/ufw-status.png)



###  List Current Firewall Rules

* **Windows**: In Advanced Settings, click *Inbound Rules* and *Outbound Rules*.

![Inbound](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/inbound.png)

* **Linux (UFW)**:

  ```bash
  sudo ufw status numbered
  ```
  ![UFW Status Numbered](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/ufw-status-numbered.png)


###  Block Inbound Traffic on Port 23 (Telnet)

* **Windows**: Create a new *Inbound Rule*, set port to `23`, block the connection.


* **Linux (UFW)**:

  ```bash
  sudo ufw deny 23
  ```

###  Test the Block Rule

* Try connecting via Telnet from the same or remote machine:

  ```bash
  telnet localhost 23
  ```
  ![Telnet Refused](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/telnet-refused.png)

* Connection should fail if the rule is active.

###  Allow SSH on Port 22 (Linux Only)

* Ensures remote admin access is not blocked:

  ```bash
  sudo ufw allow 22
  ```

### Remove the Test Block Rule

* **Windows**: Delete the rule from *Inbound Rules*.
* **Linux (UFW)**:

  ```bash
  sudo ufw delete deny 23
  ```

###  Commands & GUI Steps Summary

- Commands for Windows Firewall:
  - `netsh advfirewall firewall add rule name="Block Telnet" protocol=TCP dir=in localport=23 action=block`
  - `netsh advfirewall firewall delete rule name="Block Telnet"`

  ![Creating Inbound Rules](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/creating-inbound-rules.png)

  ![Inbound Rules with Port](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/inbound-rules-with-port.png)

![Blocking the connection](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/blocking%20the%20connection.png)


![Inbound Rules Name](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/inboun-rules-name.png)

- Commands for UFW: 
  - `sudo ufw allow 22/tcp`
  - `sudo ufw deny 23/tcp`

###  How Firewall Filters Traffic
![Firewall Operation](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-4/images/3%20Firewall%20Operation.png)


* Firewalls monitor and control incoming/outgoing traffic.
* Rules determine which ports/services are allowed or blocked.
* Helps prevent unauthorized access to system resources.
* Acts as a barrier between trusted and untrusted networks.

## Outcome
 -  Basic firewall management skills and understanding of network traffic filtering