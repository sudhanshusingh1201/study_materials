---
title: "Topic 25 - Nmap FIN Scan & TCP FIN Flag (-sF)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 25: Nmap FIN Scan & TCP FIN Flag (-sF)

### 1. Explanation (Hinglish)
Aapne jo keyword select kiya hai: **`FIN`**, yeh TCP protocol ka ek basic flag hai jo Nmap ke **FIN Scan (`-sF`)** ke control system ko represent karta hai.

---

### 1. TCP FIN Flag ka Base Kaam: Connection Teardown
TCP transmission protocol mein, **FIN (Finish)** flag ka primary kaam chal rahe dynamic connection ko **gracefully close (terminate)** karna hota hai. 
- Jab do systems (jaise aapka computer aur ek server) data transmission complete kar lete hain, toh scanner target ko FIN packet bhejta hai (indicating: *"Mera data complete hai, ab connection close karo"*), aur target system reply mein FIN-ACK bhejkar connection terminate kar deta hai.

---

### 2. Nmap FIN Scan (`-sF`) kya hai?
Nmap is flag ka misuse karke ek inverse/stealth scan technique perform karta hai. Nmap target ports par direct ek raw TCP packet bhejta hai jisme **sirf FIN flag set** hota hai (bina standard SYN handshake start kiye):

- **Closed Port Response:** Target system standard RFC 793 rules ke tehat directly **RST (Reset)** packet return karega (indicating: *"Humare beech koi connection chalu hi nahi tha, ye request terminate karo"*).
- **Open Port Response:** Target system open port par is invalid/unexpected FIN packet ko **silently ignore (drop)** kar dega (chup rahega). Nmap is silence ko dekh kar use **`Open|Filtered`** mark karta hai.

#### 🚪 Real-world Analogy: The "Polite Goodbye" Out of Nowhere
Socho aap kisi client office building checking par ho:
- **SYN Scan (Standard):** Aap reception counter par jaakar entry register fill karte ho.
- **FIN Scan (`-sF`):** Aap bina register entry kiye ya bina andar gaye, direct corridor window se chillakar bolte ho—*"Accha main jaa raha hoon, bye!"* (FIN packet):
  - **Closed Office (Closed Port):** Security guard turant check karta hai registry book aur bolta hai—*"Aap aaye kab the jo bye bol rahe ho? Chalo bahar nikalye!"* (RST).
  - **Open/Occupied Office (Open Port):** Client office room ke andar se aawaz sunta hai par ajeeb behviour samajh kar ignore kar deta hai aur shant baitha rehta hai (Silence).

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par FIN scan test karne ke steps:

**Task 1: Selected ports par FIN scan run karna:**
```bash
sudo nmap -sF -p 22,80 scanme.nmap.org
```
*(Notice karein open ports status in Linux targets).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Standard TCP protocol suite parameters ke tehat, **FIN flag** ka primary/original connection network purpose kya hota hai?
- **A)** Connection connection link ko secure link mein convert karna.
- **B)** Active connection sequence ko gracefully close/terminate karna.
- **C)** Handshake connection start karna.

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `sudo nmap -sF -p 22,80 localhost`
2. Dekhein ki kya localhost Linux OS par ports status open/closed response return karte hain.
3. Quiz ka answer aur assignment output mujhe chat mein share karein!

---