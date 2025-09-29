- [Task 5: Capture and Analyze Network Traffic Using Wireshark.](#task-5-capture-and-analyze-network-traffic-using-wireshark)
- [Objective:](#objective)
- [Tools:](#tools)
- [Deliverables:](#deliverables)
- [Guide](#guide)
    - [Installed Wireshark](#installed-wireshark)
    - [Started capturing on my main network interface](#started-capturing-on-my-main-network-interface)
    - [Visited a few websites and ran some pings](#visited-a-few-websites-and-ran-some-pings)
    - [Stopped the capture and checked the packets](#stopped-the-capture-and-checked-the-packets)
    - [Filter captured packets by protocol  HTTP, DNS, TCP.](#filter-captured-packets-by-protocol--http-dns-tcp)
    - [Identify at least 5 different protocols in the capture.](#identify-at-least-5-different-protocols-in-the-capture)
    - [Export the capture as a .pcap file.](#export-the-capture-as-a-pcap-file)
    - [Summarizing of Findings and Packet Details](#summarizing-of-findings-and-packet-details)
- [Outcome](#outcome)



## Task 5: Capture and Analyze Network Traffic Using Wireshark.


## Objective:
Capture live network packets and identify basic protocols and traffic types

## Tools:
- Wireshark (free)

## Deliverables:
A packet capture (.pcap) file and a short report of protocols identified

## Guide

1.Install Wireshark.

2.Start capturing on your active network interface.

3.Browse a website or ping a server to generate traffic.

4.Stop capture after a minute.

5.Filter captured packets by protocol (e.g., HTTP, DNS, TCP).

6.Identify at least 3 different protocols in the capture.

7.Export the capture as a .pcap file.

8.Summarize your findings and packet details.

---



###  Installed Wireshark

Just downloaded Wireshark from the [official site](https://www.wireshark.org/download.html)
 and installed it. Chose all default options during setup.
 ![Wireshark installation screenshot](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/wireshark%20installation.png)


> ✅ Good call — especially making sure Npcap was included. That’s needed for live captures.

### Started capturing on my main network interface

Opened Wireshark and started a capture on the interface showing activity (mine was Ethernet).

![Wireshark interface screenshot](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/interface-wireshark.png)




###  Visited a few websites and ran some pings

Went to a couple of websites and also pinged `testphp.vulnweb.com` from the terminal to generate traffic.

- i run test using ping 
![Ping success with website](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/ping%20sucess-with-websitte.png)

- 📌 Filtered ICMP Packets in Wireshark

After starting the packet capture, I used the display filter to isolate only ICMP traffic.

- icmp

This immediately showed all ping-related packets (Echo Request and Echo Reply). It helped me clearly see the traffic generated when I ran `ping google.com` from the terminal.

I could observe the round-trip communication between my system and the destination IP(44.228.249.3). Each request and reply pair was neatly listed, making it easy to analyze.

Captured ICMP packets included:
- Type 8: Echo (ping) request
- Type 0: Echo reply

This confirmed successful communication with the remote host.
![Wireshark traffic filter](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/wireshark-traffic-filter.png)


###  Stopped the capture and checked the packets

Clicked the red square to stop capturing after I had enough data.

> 🔍 i apply filters like `icmp`, `http`, `dns`, &`ssl` in the top bar to zoom in on specific types of traffic.



### Filter captured packets by protocol ( HTTP, DNS, TCP).

 - 📌 Filtering Captured Packets by Protocol

While capturing network traffic, I filtered packets by specific protocols to focus on the data I needed.

- To filter **HTTP** traffic, I used the display filter:
```
http
```
- For **DNS** packets, I applied:
```
dns
```
- To see only **TCP** packets, I applied:
```
tcp
```
- To see only **ssl** packets, I applied:
```
ssl
```
- To see only **udp** packets, I applied:
```
udp
```


### Identify at least 5 different protocols in the capture.
- **DNS**
![DNS capture](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/dns-wireshark%20capute.png)

- **HTTP**
![HTTP capture](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/http-wireshark-capute.png)

- **SSL**
![SSL capture](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/ssl-capture.png)

- **TCP**
![TCP capture](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/tcp-capture.png)

- **UDP**
![UDP capture](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/udp-capture.png)


### Export the capture as  file.
- 📌 Exporting Packet Data

- Once I finished capturing, I exported the packet summary to keep a record for later.  
- Wireshark lets you export either just selected packets or the whole capture in formats like `.pcap`  `.pcapng` `.txt`  `.csv`  
- This makes it easier to share the data or analyze it offline without needing Wireshark open.  
- You can find the export option under **File > Export Packet Dissections > As Plain Text**.

![Exporting packet](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-5/images/exporting-packet.png)



### Summarizing of Findings and Packet Details

- Captured network traffic using Wireshark on the active network interface during web browsing and ping tests.  
- Successfully filtered ICMP packets to analyze ping requests and replies, confirming reliable connectivity with the destination IP (44.228.249.3).  
- Observed round-trip times consistently around 261 ms, indicating stable response from the target server.  
- Applied protocol-specific filters such as HTTP, DNS, TCP, and UDP to isolate and study different types of network communications.  
- Noted successful DNS queries resolving domain names and HTTP traffic corresponding to web page requests.  
- Exported packet summaries in plain text format for documentation and offline analysis.  
- Overall, the captured data validates proper network function and provides clear insights into protocol-level interactions.

## Outcome
 -  Hands-on packet analysis skills and protocol awareness