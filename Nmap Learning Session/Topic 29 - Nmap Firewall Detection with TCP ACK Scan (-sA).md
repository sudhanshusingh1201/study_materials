---
title: "Topic 29 - Nmap Firewall Detection with TCP ACK Scan (-sA)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 29: Nmap Firewall Detection with TCP ACK Scan (-sA)

### 1. Explanation (Hinglish)
Nmap mein target system ke security rules, router policies, aur firewalls ko detect/map karne ke liye sabse primary method **TCP ACK Scan (flag: `-sA`)** hai.

Yeh scan doosre scans (SYN or Connect scan) se bilkul alag hai kyunki **yeh open ports identify nahi karta**. Iska primary task yeh batana hai ki kaun-kaun se ports firewall ke peeche filtered/blocked hain aur kaun se unfiltered hain.

---

### 🔄 Technical Mechanism (ACK packet test)
Nmap target par ek raw TCP packet bhejta hai jisme sirf **ACK (Acknowledge)** flag active hota hai. Standard rules ke mutabik unexpected ACK packet milne par target response behavior:

1. **Unfiltered State (No Firewall Block):**
   - Target port open ho ya closed, target machine ka TCP stack is unsolicited request ko cancel karne ke liye **RST (Reset)** packet return karega.
   - RST reply milte hi Nmap use **`unfiltered`** mark kar deta hai (matlab raste mein koi firewall rules block nahi kar rahe).
2. **Filtered State (Firewall Active):**
   - Stateful firewall ya packet filter in packets ko block kar deta hai, jisse ya toh koi reply nahi aata (silence) ya fir router direct ICMP destination unreachable errors return karta hai.
   - Nmap in ports ko **`filtered`** mark karta hai (indicating firewall presence).

---

#### 🚪 Real-world Analogy: The Fake Conversation Check
Socho aap ek complex building security analyze kar rahe ho:
- **ACK Scan (`-sA`):** Aap building ke kisi room ke samne jaakar direct bolte ho—*"Haan sir, humari phone call par deal confirm ho gayi thi, ye lo receipt!"* (ACK packet - although no call ever happened):
  - **No Security Guard (Unfiltered):** Room door open ho ya closed, owner direct gate par aakar gusse mein chilata hai—*"Kaun si call? Wapas jao!"* (RST). Aapko pata chal jata hai ki beech mein koi guard nahi hai jo packet block kar sake.
  - **Security Guard present (Filtered):** Gate par khada guard (firewall) aapko door tak jaane hi nahi deta aur beech raste se hi wapas bhagata hai (Silence/ICMP block). Aap samajh jate ho ki is room tak pahunchne ke liye guard rules active hain.

---

### 💻 Kali Linux Practice Task
*Note: Custom TCP ACK headers build karne ke liye is scan ko run karne ke liye superuser (`sudo`) access lagta hai.*

**Task 1: Selected ports par ACK Scan rules map karna:**
```bash
sudo nmap -sA -p 22,80,443 scanme.nmap.org
```
*(Notice karein open/closed status ke badle **unfiltered** response output tables).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap TCP ACK Scan (`-sA`) ka primary design network function kya hota hai?
- **A)** Active services ke versions find out karna.
- **B)** Firewall filtering rules active hain ya nahi (Filtered vs Unfiltered ports map karna) ye check karna.
- **C)** Targets ka OS fingerprint scan karna.

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `sudo nmap -sA localhost`
2. Check karein ki localhost loopback ports ka status table layout mein kya print hota hai.
3. Quiz ka answer aur assignment output mujhe chat mein share karein!

---