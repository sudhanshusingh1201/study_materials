---
title: "Topic 56 - Network Firewalls (Security Guard of Networks)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🧱 56. Network Firewalls (Security Guard of Networks)

### 📝 Introduction (Intro)
**Firewall** ek network security system hota hai jo predefined security rules ke basis par incoming aur outgoing network traffic ko continuously monitor aur control karta hai. Ye ek secure, trusted internal private network aur an untrusted external network (jaise public Internet) ke beech me ek barrier/wall ki tarah kaam karta hai.

#### 🔑 Classification/Types of Firewalls:
1. **Packet Filtering Firewall (L3/L4):**
   * *How it works:* Ye incoming packets ke headers checks run karta hai (Source IP, Destination IP, Protocol, Port number) aur decide karta hai ki use aage jaane dena hai (Allow/Pass) ya block karna hai (Drop/Deny).
   * *Nature:* Stateless, bahot fast, par application data inspect nahi kar sakta.
2. **Stateful Inspection Firewall (L3/L4/L5):**
   * *How it works:* Ye chal rahe active connections (established handshakes, TCP states tables) ki monitoring karta hai. Ye tabhi incoming packet allow karega jab wo kisi valid outgoing request ka active part ho.
3. **Application-Level Gateway / Proxy Firewall (L7):**
   * *How it works:* Ye Application layer level par data blocks ko dissect aur deep analyze karta hai (jaise HTTP packet content filtering). Ye client aur target server ke beech middleman (proxy) ki tarah act karta hai. Highly secure but slow.
4. **Next-Generation Firewall (NGFW):**
   * *How it works:* Modern enterprise firewalls jo packet filtering, stateful checks, Deep Packet Inspection (DPI), Intrusion Prevention Systems (IPS/IDS), aur real-time antivirus/anti-malware services ko combine karte hain.

### ➕ Advantages (Fayde)
* **Access Control & Traffic Monitoring:** Internal network assets blockages setup karke hackers aur external intruders se continuously system shield rakhta hai.
* **Malware & Attack Prevention:** SQL injections, cross-site scripting (XSS), aur unauthorized network scans data flows ko perimeter gate par block kar deta hai.
* **Custom Security Policies:** Business limits aur parameters control set kiya ja sakta hai (e.g., employee computer machines par torrent websites blocked).

### ➖ Disadvantages (Nuksan)
* **Performance Degradation (Bottlenecks):** Deep packet inspection aur state validations process traffic transmission link performance speed ko decrease (latency add) kar dete hain.
* **False Positives (Blocking Legitimate Traffic):** Configuration parameters restrictions extra tight hone par useful systems requests (legitimate traffic) block ho jate hain.
* **Complex Configuration & High Cost:** Premium enterprise firewalls and Next-Gen units deploy and maintain karne me strong administrative knowledge aur high costs require hoti hain.

### 📊 Diagram
Ye layout Internal network users, Firewall rules inspection gates, aur Internet external connection bridge ko show karta hai:

```
                                      [ FIREWALL SYSTEM ]
                                 (Checks Rules & Policies)
                                             |
[ Internal Private Network ]                 |                  [ External Public Network ]
 (Secure Devices / LAN)                      |                          (Internet)
        |                                    |                              |
  User Laptop (192.168.1.10) -- HTTP/Port 80 | === ALLOW ==> Web Server (Google.com)
                                             |
  Hacked System ------------ Bad Port 4444   | X X DROP X X <=== Malicious Intruder (Blocked!)
                                             |
```

### 💡 Real-world Example (Udaharan)
* **Private Society Security Guard Metaphor:**
  - Maan lijiye aap ek secure private building society me rehte hain. Society entrance gate par ek alert **Security Guard** (Firewall) baitha hai.
  - Us guard ke pass society office rules ki sheet (Policies) hai.
  - **Packet Filtering:** Guard visitor ka ID checks karta hai. Agar visitor guest register name book me allowed flat block se matched hai (Authorized IP/Port), use andar aane deta hai.
  - **Stateful Inspection:** Guard check karta hai ki kya society ke kisi member ne is guest ko call karke bulaya tha (outgoing session request check). Agar member validation matched hai, tabhi gate open hoga.
  - **Application Proxy:** Guard visitor ka box suitcase open karwakar check karta hai ki andar koi suspicious item (Deep Packet Inspection) toh nahi hai.

### 🚀 Application (Kahan use hota hai?)
* **Windows Defender Firewall:** Built-in OS software protection securing local laptop resources.
* **Corporate Network Edge:** Enterprise physical appliances (Fortinet, Cisco ASA, Palo Alto NGFW) wrapping corporate headquarters gateway points.
* **Cloud Infrastructure Security:** Cloud service providers configurations tools (like AWS Security Groups and Network ACLs protecting VPC instances).

---