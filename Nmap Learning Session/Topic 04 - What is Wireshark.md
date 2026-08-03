---
title: "Topic 04 - What is Wireshark"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 4: What is Wireshark?

### 1. Explanation (Hinglish)
**Wireshark** ek free aur open-source graphical tool hai jo network traffic ko capture aur analyze karne ke liye use hota hai. Ise **"Packet Sniffer"** ya **"Protocol Analyzer"** bhi kehte hain.

Jab aap Wireshark start karte hain, toh yeh aapke network interface card (NIC) ke zariye aane aur jaane wale har ek raw data packet (traffic) ko read karke use aasan readable format mein display karta hai.

#### 📞 Real-world Analogy: The Wiretapper (Phone Tapping)
Socho do log phone call par baat kar rahe hain. 
Wireshark chalana bilkul **phone line tap** karne jaisa hai:
1. Aap call ke beech mein ek system install karte ho.
2. Dono side se jo bhi bola ja raha hai, aap use real-time mein record aur decode kar rahe ho.
3. Aap dekh sakte ho ki kis protocol (language) mein baat ho rahi hai, kaun bol raha hai (Source IP), aur kisko bola ja raha hai (Destination IP).

#### 🔑 Core Wireshark Terms
1. **Promiscuous Mode:** Network card ka ek special mode jo use apne subnet par travel karne wale har ek packet ko read karne ki permission deta hai (chahe packet aapke computer ke liye ho ya na ho).
2. **Display Filters:** Capture hone ke baad specific packets ko filter karna. Jaise, agar aapko sirf HTTP web traffic dekhna hai, toh filter lagayein: `http`.
3. **Capture Filters:** Capture shuru hone se pehle limit lagana ki hume kaun sa traffic capture karna hai (taaki unnecessary logs na banein).

---

### 💻 Kali Linux Practice Task
Kali Linux mein Wireshark pre-installed hota hai. Ise start karne ke liye:

**Task 1: Wireshark Open & Interface Select karna:**
1. Kali Linux application menu mein search karein "Wireshark" ya terminal par type karein:
   ```bash
   sudo wireshark
   ```
2. Welcome screen par apne active interface (e.g., `eth0` ya `wlan0` jiske aage continuous wave/graph ban raha hai) par double-click karke capture start karein.

**Task 2: Live Traffic Filter karna (Ping check):**
1. Capture start hone ke baad top bar mein **"Apply a display filter..."** box mein type karein: `icmp` (Internet Control Message Protocol).
2. Naya terminal open karke type karein:
   ```bash
   ping -c 4 scanme.nmap.org
   ```
3. Wireshark screen par wapas aayein, wahan aapko `Echo (ping) request` aur `Echo (ping) reply` ke packets blue/pink color mein highlight hote huye dikhenge!

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Wireshark network card ko kis special mode mein daalta hai taaki wo network ke saare packets (chahe wo dusre computer ke liye ho) read kar sake?
- **A)** Stealth Mode
- **B)** Promiscuous Mode
- **C)** Interceptor Mode

#### 🎯 Assignment
1. Kali Linux par `sudo wireshark` chalayein aur `icmp` filter lagayein.
2. Terminal par `ping -c 4 127.0.0.1` run karein.
3. Dekhein ki kya Wireshark packets capture kar raha hai. 
4. Quiz ka answer aur output/status mujhe chat mein share karein!

---