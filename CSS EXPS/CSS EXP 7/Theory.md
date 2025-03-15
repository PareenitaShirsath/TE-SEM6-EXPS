# Jawahar Education Society’s

## A. C. Patil College of Engineering, Kharghar  
**Department of Artificial Intelligence & Data Science**  
**Academic Year 2024-25 (Even Sem.)**  

[www.acpce.org](www.acpce.org)  

# EXPERIMENT NO. 7

## Aim:
**Study of packet sniffer tools: Wireshark**  

1. Download and install Wireshark and capture ICMP, TCP, and HTTP packets in promiscuous mode.
2. Explore how the packets can be traced based on different filters.

## Objectives:

- Understand the need for traffic analysis.
- Understand how packet sniffing is done using Wireshark.
- Trace and understand various packets from dynamic traffic.

## Outcomes:
The learner will be able to:

- Sniff network packets and study insights of packets to get detailed network information.

## Hardware / Software Required:
- Unix/Linux/Windows
- Wireshark

---

## Theory:
Wireshark, a network analysis tool formerly known as Ethereal, captures packets in real-time and displays them in a human-readable format. Wireshark includes filters, color-coding, and other features that let you dig deep into network traffic and inspect individual packets.

### Features of Wireshark:

- Available for UNIX and Windows.
- Capture live packet data from a network interface.
- Open files containing packet data captured with tcpdump/WinDump, Wireshark, and other packet capture programs.
- Import packets from text files containing hex dumps of packet data.
- Display packets with very detailed protocol information.
- Export some or all packets in a number of capture file formats.
- Filter packets on many criteria.
- Search for packets on many criteria.
- Colorize packet display based on filters.
- Create various statistics.

---

## Capturing Packets:
After downloading and installing Wireshark, you can launch it and click the name of an interface under **Interface List** to start capturing packets on that interface. For example, if you want to capture traffic on the wireless network, click your wireless interface. You can configure advanced features by clicking **Capture Options**.

### Installation of Wireshark:
```bash
sudo apt-get install wireshark
```
After downloading and installing Wireshark, you can launch it and click the name of an interface under **Interface List** to start capturing packets on that interface. For example, if you want to capture traffic on the wireless network, click your wireless interface. You can configure advanced features by clicking **Capture Options**.

As soon as you click the interface’s name, you’ll see the packets start to appear in real-time. Wireshark captures each packet sent to or from your system. If you’re capturing on a wireless interface and have **promiscuous mode** enabled in your capture options, you’ll also see other packets on the network.

Click the **stop capture** button near the top left corner of the window when you want to stop capturing traffic.

Wireshark uses **colors** to help you identify the types of traffic at a glance:

- **Green** → TCP traffic
- **Dark Blue** → DNS traffic
- **Light Blue** → UDP traffic
- **Black** → TCP packets with problems (e.g., delivered out-of-order packets)

---

## Filtering Packets:
If you’re trying to inspect something specific, such as the traffic a program sends when phoning home, it helps to close down all other applications using the network so you can narrow down the traffic. Still, you’ll likely have a large number of packets to sift through. That’s where **Wireshark’s filters** come in.

The most basic way to apply a filter is by typing it into the filter box at the top of the window and clicking **Apply** (or pressing **Enter**). For example, type:
```plaintext
dns
```
and you’ll see only **DNS packets**. When you start typing, Wireshark will help you autocomplete your filter.

---

## Conclusion:
Wireshark installation and network traffic analysis using packet sniffing are completed. Detailed information about packets is explored by applying filters.


