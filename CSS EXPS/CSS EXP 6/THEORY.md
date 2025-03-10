# **Study of Network Reconnaissance Tools: WHOIS, dig, traceroute, nslookup**

## **AIM**  
To study the use of network reconnaissance tools like **WHOIS, dig, traceroute, and nslookup** to gather information about networks and domain registrars.

## **OBJECTIVES**  
- To understand **network information discovery**.  
- To study various **basic network commands** to gather network information.  
- To understand **passive attack techniques**.  

## **OUTCOMES**  
The learner will be able to:  
- Apply **basic network commands** to gather **network information**.  

## **Hardware / Software Required**  
- **Unix/Linux operating system**  

---

## **THEORY**  

### **1. WHOIS**  
- **WHOIS** is a **Linux utility** for searching an object in a **WHOIS database**.  
- The **WHOIS database** contains publicly displayed information about a domain's **ownership, billing, technical, administrative, and nameserver details**.  
- Running a **WHOIS query** on a domain retrieves information from the registrar.  

#### **WHOIS Database Information**  
The WHOIS database can provide the following details:  
- **Administrative contact details**, including names, email addresses, and telephone numbers.  
- **Mailing addresses** for office locations relating to the target organization.  
- **Details of authoritative name servers** for each given domain.  

#### **Example: Querying Facebook.com**  
# **Study of dig, traceroute, and nslookup Commands**

## **1. Dig (Domain Information Groper)**  

### **Introduction**  
- **dig** is a command-line tool used for **querying DNS servers**.  
- It helps **diagnose domain issues** and **verify DNS configurations**.  
- Commonly used to **retrieve information about domain name system (DNS) records**.  

### **Usage & Syntax**  
```sh
dig [options] [domain]

