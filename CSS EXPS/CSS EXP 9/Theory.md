# Experiment: Detecting ARP Spoofing Using Nmap, ARPWatch, and Wireshark

## Aim

The aim of this experiment is to detect ARP spoofing (also known as ARP poisoning) within a local network using open-source tools: *Nmap, **ARPWatch, and **Wireshark*. The experiment will demonstrate how these tools can be leveraged to identify and prevent potential network attacks that manipulate the Address Resolution Protocol (ARP) in a local area network (LAN).

## Theory

### 1. *ARP Spoofing Overview*
   
ARP spoofing is a type of cyber attack where a malicious actor sends false ARP (Address Resolution Protocol) messages over a local network. These messages associate the attacker's MAC address with the IP address of another device (usually the default gateway), causing the victim's machine to send traffic to the attacker instead of the legitimate gateway. The attacker can then intercept, modify, or drop the communication, leading to potential data theft, session hijacking, or network disruptions.

### 2. *ARP Protocol*

ARP is used in IPv4 networks to map a 32-bit IP address to a 48-bit MAC address. When a device wants to send data to another device within the same network, it uses ARP to resolve the recipient’s MAC address, as the MAC address is required for physical layer communication. ARP spoofing exploits this process by sending forged ARP messages, which can mislead devices in the network.

### 3. *Tools Used to Detect ARP Spoofing*

#### Nmap
- *Nmap* is a powerful open-source network scanning tool that can be used for discovering devices on a network, identifying open ports, and detecting anomalies. It can help in detecting ARP spoofing by scanning for inconsistencies or suspicious ARP replies that don't align with the expected topology of the network.
  
  *Example Nmap Commands for ARP Spoofing Detection:*
  - nmap -sn 192.168.1.0/24 - Performs a ping sweep on a subnet to discover devices.
  - nmap --script arping --script-args arping.timeout=500ms 192.168.1.0/24 - Performs an ARP scan to detect ARP inconsistencies.

#### ARPWatch
- *ARPWatch* is an open-source tool that monitors Ethernet/IP address pairings and logs changes. It can be used to detect suspicious or unexpected changes in the ARP table, which is a sign of ARP spoofing.
  
  ARPWatch listens for ARP traffic on the network and maintains a database of IP-MAC pairings. When it detects an unexpected change in a pair, it can send an alert to the network administrator.

  *Example ARPWatch Setup:*
  - Install ARPWatch using sudo apt install arpwatch
  - Start ARPWatch with sudo arpwatch -i eth0 to monitor the eth0 network interface for ARP anomalies.

#### Wireshark
- *Wireshark* is a widely-used network protocol analyzer that allows for real-time monitoring of network traffic. It can capture ARP packets and display them in detail, helping to identify ARP spoofing attempts by inspecting the ARP requests and replies.

  *Wireshark Filter for ARP:*
  - Use arp as a display filter to view all ARP packets. Malicious ARP replies can be identified by looking for duplicate IP-MAC associations or ARP replies without prior requests.

  *ARP Spoofing Detection in Wireshark:*
  - Look for ARP packets with suspicious or conflicting MAC addresses or multiple ARP responses with the same IP address.

### 4. *Preventing ARP Spoofing*
   
To mitigate ARP spoofing attacks:
- *Static ARP Entries:* Assign static ARP entries for critical devices like gateways to prevent attackers from altering the ARP cache.
- *ARPWatch Monitoring:* Regularly monitor the network using ARPWatch to detect and alert on suspicious changes.
- *Intrusion Detection Systems (IDS):* Use IDS solutions to monitor and alert on ARP spoofing attempts.
- *Encryption and VPNs:* Encrypt sensitive communication using SSL/TLS or VPNs to protect data even if ARP spoofing occurs.

## Conclusion

The experiment focuses on using Nmap, ARPWatch, and Wireshark to detect ARP spoofing in a local network. By understanding ARP spoofing techniques and utilizing these open-source tools, administrators can better secure their networks and detect potential ARP poisoning attacks. Detection and monitoring are essential for maintaining the integrity and security of local area networks.
