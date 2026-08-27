---
title: "Day 58 - Intro to Network Automation"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🤖 Day 58: Introduction to Network Automation

Welcome to the notes for **Day 58: Intro to Network Automation** of Jeremy's IT Lab CCNA Complete Course! Aaj hum **Module 7: Network Automation & Programmability** ko start karenge. Is lecture note mein hum seekhenge ki traditional network management (manual CLI) ke drawbacks kya hain, network ke teen primary plane systems—**Data Plane, Control Plane, aur Management Plane**—kya role play karte hain, Software-Defined Networking (SDN) centralized control model kya hota hai, aur SDN controller API architectures (**Northbound vs Southbound APIs**) ko details, comparisons, aur diagrams ke sath cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. Traditional Network Management vs. Automation

Traditional networks mein, network administrators routers aur switches ko manually configure karte hain:

*   **Traditional Drawbacks:**
    1.  *CLI Manual Entry:* Har device par manually SSH/Telnet karke commands execute karna (very slow aur repetitive process).
    2.  *Human Errors:* Manually configurations type karte waqt errors hone ke chances bohot high hote hain (e.g. writing wrong subnet mask).
    3.  *Configuration Drift:* Over time, identical switch configurations different ho jati hain (drift) because of random hot-fixes done by different admins.
    4.  *Lack of Global Visibility:* Network ka state check karne ke liye saare routers par alag-alag logins karke statistics aggregate karni padti hain.
*   **Automation:** Scripts (jaise Python) ya centralized controller software (jaise Cisco DNA Center / Catalyst Center) ke through poor networks ko aapas mein automatically, standard, aur programmatically update aur monitor kiya jata hai.

---

## 🏛️ 2. The Three Network Planes

Kise device ke functional layers aur architectures ko 3 planes mein divide kiya jata hai. CCNA examination point of view se ye definitions directly memory mein honi chahiye:

```text
  +-------------------------------------------------------------------+
  |   MANAGEMENT PLANE: SSH, Telnet, HTTP, SNMP, Syslog               |
  +-------------------------------------------------------------------+
                                   |
  +-------------------------------------------------------------------+
  |   CONTROL PLANE: OSPF, STP, ARP, BGP, Routing Engine, CPU         |
  |   (Decides WHERE to send packets - builds MAC/Routing Tables)     |
  +-------------------------------------------------------------------+
                                   |
  +-------------------------------------------------------------------+
  |   DATA PLANE: MAC Table Lookups, IP Route Lookups, ASICs          |
  |   (Actually forwards/switches frames - High-Speed Hardware)       |
  +-------------------------------------------------------------------+
```

### 1. Data Plane (Forwarding Plane):
*   **Role:** Wo process jo network par aane wale actual packets aur frames ko transit forward/switch karti hai.
*   **Characteristics:** Hardware speed par operate hoti hai using **ASICs (Application-Specific Integrated Circuits)**. Inme heavy calculations nahi hoti, bas matching algorithm chalte hain.
*   *Examples:* MAC Address table lookup, IP routing table packet check, Frame encapsulation/de-capsulation, ACL filters application.

### 2. Control Plane:
*   **Role:** Wo system jo network packets routing paths decide karta hai. Ye routing tables, MAC tables aur ARP caches build karne ke liye protocols run karta hai.
*   **Characteristics:** Router/Switch CPU memory par chalta hai. Ye direct forward nahi karta, bas forwarding plane ki table tayyar karta hai.
*   *Examples:* OSPF, EIGRP, BGP routing updates calculations, Spanning Tree Protocol (STP) convergence, ARP request/reply generation, ICMP processing.

### 3. Management Plane:
*   **Role:** Device ko administratively connect aur manage karne ke methods.
*   *Examples:* SSH, Telnet access, Web HTTPS browser access, SNMP polling, Syslog log generation, NTP time synchronization.

---

## 🧭 3. Software-Defined Networking (SDN)

Traditional networks mein, control plane aur data plane **har router/switch ke andar distributed (local)** hote hain. Har router apna control decision khud leta hai.

**Software-Defined Networking (SDN)** mein:
1.  Control Plane ko physical hardware devices se **decouple (separate)** kiya jata hai.
2.  Ek centralized central virtual controller software (**SDN Controller**) networks ka main Control brain ban jata hai.
3.  Physical switch/routers ke paas sirf unka local **Data Plane** bacha rehta hai, jo central controller ke specifications ke according blindly traffic forward karta hai.

---

## 🕸️ 4. SDN Controller API Architecture (Northbound vs. Southbound)

SDN controller poor system ke beech middle translation server ki tarah act karta hai:

```text
     +------------------------------------------+
     |   Applications / Admin Scripts (Python)   |
     +------------------------------------------+
                          |
                          |  NORTHBOUND APIs (REST APIs)
                          v
     +------------------------------------------+
     |             SDN CONTROLLER               |  <-- Central Control Plane
     +------------------------------------------+
                          |
                          |  SOUTHBOUND APIs (OpenFlow, NETCONF, RESTCONF)
                          v
     +------------------------------------------+
     |     PHYSICAL SWITCHES & ROUTERS          |  <-- Data Plane Only
     +------------------------------------------+
```

### A. Northbound APIs:
*   **Direction:** Controller se administrative applications / automation scripts (Python, Ansible, DNA center UI) ki taraf.
*   **Purpose:** Admin ko centralized control parameters aur variables modify or view karne ki flexibility deta hai.
*   **Protocol:** Standard **REST APIs** (HTTP formats return, typically JSON/XML data formats).

### B. Southbound APIs:
*   **Direction:** Controller se downward towards physical switches aur routers hardware.
*   **Purpose:** Controller switches par configurations push karta hai aur network forwarding state coordinate karta hai.
*   **Protocols:**
    *   **OpenFlow:** Original open-source SDN protocol.
    *   **NETCONF:** Modern management protocol (XML encoding, runs over secure SSH).
    *   **RESTCONF:** HTTP-based configuration protocol (HTTP commands GET, POST, PUT, DELETE with XML/JSON data).
    *   Cisco dynamic Southbound APIs (OnePK, CLI over SSH).

---

## 📝 5. CCNA Day 58 Practice Questions

1. **Q1: Traditional network device management mein 'Configuration Drift' kya error define karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Multiple similar network switches ke configurations over time alag-alag hot-fixes apply karne ke chalte different ho jana, jisse configurations standardized nahi rehti.
   </details>

2. **Q2: Packet transitions dynamically forward and switch karne ke liye switch/router ke kis plane layer ko assign kiya jata hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Data Plane** (Forwarding Plane).
   </details>

3. **Q3: OSPF route calculations aur Spanning Tree Protocol (STP) logic executions router ke kis network plane par process hote hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Control Plane** (Runs on device CPU).
   </details>

4. **Q4: Administrative remote CLI configuration commands (SSH/Telnet) terminal inputs kis system plane boundaries ke andruni parameters hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Management Plane**.
   </details>

5. **Q5: Software-Defined Networking (SDN) systems control plane aur data plane ko kaise modify karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Dynamic control plane ko physical devices se **separate (decouple)** karke central **SDN Controller** engine par locate kiya jata hai, jabki physical network devices par sirf L2/L3 data forwarding features local maintain rehte hain.
   </details>

6. **Q6: SDN controller architecture mein 'Northbound APIs' targets coordinates kis side communication direction specify karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Controller se **upward direction** mein, administrative software applications, configuration managers (Ansible, Chef) ya custom automation scripts (Python REST queries) ki taraf.
   </details>

7. **Q7: Controller downward network switches/routers configurations updates push karne ke liye use hone wale APIs systems ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Southbound APIs**.
   </details>

8. **Q8: Modern xml-based southbound management protocol jo secure SSH connection lines par dynamic config management operations execute karta hai, use kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **NETCONF** (Standardized under RFC 6241).
   </details>

9. **Q9: REST API HTTP operations protocols ko network controllers configurations par apply karne wale modern southbound protocol standard framework name kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **RESTCONF** (RFC 8040).
   </details>

10. **Q10: Switch data plane hardware packets switching high-speed boost perform karne ke liye typical kis computational module cards use karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **ASIC (Application-Specific Integrated Circuit)** cards.
    </details>
