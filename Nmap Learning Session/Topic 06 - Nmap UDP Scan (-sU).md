---
title: "Topic 06 - Nmap UDP Scan (-sU)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 6: Nmap UDP Scan (-sU)

### 1. Explanation (Hinglish)
**`-sU`** Nmap ka **UDP Scan** flag hai. Jab hume network par chalne wali UDP (User Datagram Protocol) services ko scan karna hota hai, tab hum is flag ka use karte hain.

TCP connection-oriented hota hai (jisne handshake confirm hota hai), par **UDP connectionless protocol** hai (bina confirmation ke data bhej diya jata hai). Common UDP services:
- **Port 53:** DNS (Domain Name System)
- **Port 67/68:** DHCP (IP assign karne ke liye)
- **Port 123:** NTP (Network Time Protocol)

#### 📨 Real-world Analogy: Letter Box Without Delivery Receipt
Socho aap kisi ko bina acknowledgement/receipt ke ek post-card (UDP packet) bhej rahe ho:
1. **Closed:** Agar target system active hai par port par koi app nahi hai, toh system ek ICMP error message wapas bhejega: *"Port Unreachable"* (Nmap samajh jata hai ki port **Closed** hai).
2. **Open|Filtered:** Agar target port open hai aur app ko packet mila, toh UDP ke rules ke mutabik wo target app koi response wapas nahi bhejegi (silence). Nmap is silence ko dekh kar sure nahi hota aur use mark karta hai: **`Open|Filtered`** (yani ya toh open hai ya fir raste mein firewall ne packet drop kar diya).

---

### 💻 Kali Linux Practice Task
UDP scanning ke liye root (`sudo`) permissions ki zaroorat hoti hai.

**Task 1: Selected UDP ports ko scan karna (Faster):**
```bash
sudo nmap -sU -p 53,123,161 scanme.nmap.org
```

**Task 2: UDP scan ke sath Service Version detect karna (Slightly slower but more accurate for Open ports):**
```bash
sudo nmap -sU -sV -p 53 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
UDP scan (`-sU`) karte waqt, agar target port se koi response (no reply) nahi milta, toh Nmap use kis status mein show karta hai?
- **A)** Open
- **B)** Closed
- **C)** Open|Filtered

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `sudo nmap -sU -p 53,123 scanme.nmap.org`
2. Dekhein ki DNS (53) aur NTP (123) ports ka status output mein kya dikh raha hai.
3. Quiz ka answer aur scanning output ka short summary mujhe chat mein send karein!

---