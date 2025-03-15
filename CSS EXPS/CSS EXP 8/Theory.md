# Jawahar Education Society’s

## A. C. Patil College of Engineering, Kharghar  
### Department of Artificial Intelligence & Data Science  
**Academic Year 2024-25 (Even Sem.)**  

**www.acpce.org**  

## EXPERIMENT NO. 8

### **Aim:**  
Download and install nmap. Use it with different options to scan open ports, perform OS fingerprinting, do a ping scan, TCP port scan, UDP port scan, Xmas scan, etc.

### **Objectives:**

- Understand port scanning.
- Understand how nmap helps to scan various ports.
- Explore various nmap options for OS fingerprinting and gathering detailed network and remote host information.

### **Outcomes:**  
The learner will be able to:

- Install and use nmap for gathering detailed network and remote host information.

### **Hardware / Software Required:**  
Unix/Linux, nmap  

---

## **Theory:**  
Nmap (Network Mapper) is a security scanner originally written by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich) used to discover hosts and services on a computer network, thus creating a "map" of the network. To accomplish its goal, Nmap sends specially crafted packets to the target host and then analyzes the responses. Unlike many simple port scanners that just send packets at some predefined constant rate, Nmap accounts for network conditions (latency fluctuations, network congestion, target interference with the scan) during the run.

Owing to the large and active user community providing feedback and contributing to its features, Nmap has been able to extend its discovery capabilities beyond simply figuring out whether a host is up or down and which ports are open and closed; it can determine the operating system of the target, names and versions of the listening services, estimated uptime, type of device, and presence of a firewall.

### **Nmap Features:**

- **Host Discovery** - Identifying hosts on a network (e.g., listing the hosts that respond to pings or have a particular port open).
- **Port Scanning** - Enumerating the open ports on one or more target hosts.
- **Version Detection** - Interrogating listening network services to determine the application name and version number.
- **OS Detection** - Remotely determining the operating system and some hardware characteristics of network devices.

---

### **Basic Commands in Nmap:**

- **For target specifications:**  
  ```bash
  nmap <target's URL or IP>
  ```

- **For OS detection:**  
  ```bash
  nmap -O <target-host's URL or IP>
  ```

- **For version detection:**  
  ```bash
  nmap -sV <target-host's URL or IP>
  ```

**SYN scan** is the default and most popular scan option. It can be performed quickly, scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It is also relatively unobtrusive and stealthy since it never completes TCP connections.

### **Installation of Nmap:**
  ```bash
  $ sudo apt-get install nmap
  ```

### **Common Nmap Scans:**

- **Ping Scan:**  
  ```bash
  nmap -sP 10.0.0.0/24
  ```
  Lists machines that respond to ping.

- **FIN scan (-sF):**  
  Sets just the TCP FIN bit.

- **Version Detection (-sV):**  
  Enables version detection. Alternatively, use `-A` to enable version detection along with other features.

- **IP Protocol Scan (-sO):**  
  Determines which IP protocols (TCP, ICMP, IGMP, etc.) are supported by target machines.

- **OS Detection (-O):**  
  Enables OS detection. Alternatively, use `-A` to enable OS detection along with other features.

- **Port Ranges (-p):**  
  Specifies which ports to scan, overriding the default.
  ```bash
  nmap -p 1-1023 <target>
  ```

- **Scan Top Ports:**  
  ```bash
  nmap --top-ports <number>
  ```
  Scans the N highest-ratio ports found in the `nmap-services` file.

- **List Host Interfaces and Routes:**  
  ```bash
  nmap --iflist
  ```
  Displays host interface and route information.

---

### **Conclusion:**  
Nmap is studied, and different types of Nmap scans are used to gather host and network-related information.  

---

**www.acpce.org**  
**Department of Artificial Intelligence & Data Science**  
**A. C. Patil College of Engineering, Kharghar**


