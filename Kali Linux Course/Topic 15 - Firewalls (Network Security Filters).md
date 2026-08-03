---
title: "Topic 15 - Firewalls (Network Security Filters)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---



← [[Course on Kali Linux|Go Back to Course Hub]]

# 🧱 Topic 15: Firewalls (Network Security Filters)

Bhai, cyber security aur networking domain me **Firewall** protection ka sabse pehla aur primary gatekeeper hota hai. 

Firewall ek software or hardware device hai jo dynamic network traffic (incoming aur outgoing packets) ko continuously monitor aur filter karti hai, kuch predefined security rules ke basis par. Ye hamare local network (trusted) ko outer internet (untrusted) network se safe rakhti hai.

---

### 🔑 Real-World Analogy (Security Guard 👮‍♂️)
* Maan lo ek high-security VIP building hai. Gate par ek **Security Guard** khada hai jiske haath me ek access register list (Rules) hai.
* Jab koi car building me ghusne ki koshish karti hai, guard check karta hai:
  * *Car number kya hai? (Source IP)*
  * *Ye building me kis flat me ja rahi hai? (Destination Port)*
* Agar car ki entry list me allowed hai, toh guard gate khol deta hai. Agar rules me block hai, toh gate band rakhta hai. Ye guard hi **Firewall** hai.

---

### 📂 Major Types of Firewalls (Kaise Filter Karta Hai?)

Technology ke evaluation ke according firewalls ko in categories me divide kiya gaya hai:

1. **Packet Filtering Firewall (Simplest):**
   * Ye network layer par packets ko check karti hai. Ye packets ke dynamic variables (Source/Destination IP, Source/Destination Port, Protocol type) ko check karti hai par packet ke content payloads ko read nahi karti.
2. **Stateful Inspection Firewall (Smarter):**
   * Ye active network connection sessions ko track karti hai. 
   * *Example:* Agar aapne apne PC se google.com ko request bheji, toh Google se aane wale data reply packets ko firewall bina rules check kiye automatic aane degi kyunki connection setup internal system ne trigger kiya tha.
3. **Application Firewall / WAF (Deep Inspection) 🌐:**
   * **WAF (Web Application Firewall):** Ye specialized firewall hoti hai jo HTTP web traffic (ports 80/443) ko unpack karke scan karti hai. Ye web attacks jaise SQL Injection, Cross-Site Scripting (XSS) ko detect karke block karti hai.
4. **Next-Generation Firewall (NGFW):**
   * Modern enterprise grade protection systems. Inme standard rules checks ke alawa deep packet inspection (DPI), built-in Intrusion Prevention Systems (IPS), malware scanning engine aur automatic SSL decryption modules pre-load hote hain.

---

### 🛠️ Firewalls inside Linux (Kali Linux OS)

Linux operating systems me built-in firewall processing framework hota hai jise **netfilter** kehte hain. Local configuration rules manage karne ke liye tools standard parameters par use hote hain:

#### 1. ufw (Uncomplicated Firewall)
Ye standard `iptables` tool ka ek simple command-line interface wrapper hai:

**Basic Commands:**
* **Enable Firewall:**
  ```bash
  sudo ufw enable
  ```
* **Specific Port Allow karna (e.g., SSH port 22 allow status):**
  ```bash
  sudo ufw allow 22/tcp
  ```
* **Specific IP block karna:**
  ```bash
  sudo ufw deny from 192.168.1.50
  ```
* **Firewall Status Check:**
  ```bash
  sudo ufw status verbose
  ```

---

### 🕵️‍♂️ Hacker's View: How to Scan Firewalls?

Penetration testing scan ke time hacker ko pata hona chahiye ki target port direct closed hai ya kisi firewall filter ke wajah se blocked hai.

* **Nmap TCP ACK Scan (`-sA`):**
  * Ye scan target ports par ACK packets bhejta hai.
  * Agar database reply me **RST packet** milta hai, iska matlab hai port firewall protected nahi hai (unfiltered status).
  * Agar target reply **ICMP unreachable error** deta hai ya koi response nahi aata, iska matlab hai port ke aage firewall active hai (filtered status).
  ```bash
  nmap -sA <Target_IP>
  ```

---