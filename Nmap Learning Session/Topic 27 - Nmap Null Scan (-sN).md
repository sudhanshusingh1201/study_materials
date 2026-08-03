---
title: "Topic 27 - Nmap Null Scan (-sN)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 27: Nmap Null Scan (-sN)

### 1. Explanation (Hinglish)
Nmap mein **`-sN`** flag ko **Null Scan** kaha jata hai. Yeh inverse TCP flag scanning methods ka ek zaroori scanning structure hai.

#### ❓ Is scan ko "Null Scan" kyun bolte hain?
Is scan mein Nmap jo TCP packet target ko test karne ke liye bhejta hai, uske TCP header block mein **koi bhi flag set nahi hota (All flags = 0)**. Packet header bilkul "khaali" (Null) hota hai.

Standard TCP state machine protocol rules ke tehat, bina kisi flags (jaise SYN, ACK, or FIN) ke TCP packet send karna ek illegal aur invalid network activity hai. 

---

### 🔄 Technical Mechanism (RFC 793 Rules)
Unexpected empty packet milne par target system ka behaviour:
- **Closed Port:** Target port closed hone par target system directly **RST (Reset)** packet return karega.
- **Open Port:** Target port open hone par target system is blank packet ko silently **ignore (drop)** kar deta hai (chup rehta hai).

Nmap is protocol behaviour se port status analyze karta hai:
- **RST response mila** = Port **Closed** hai.
- **No response (Silence)** = Port **Open|Filtered** hai (ya toh port open hai ya fir firewall scan request block kar raha hai).

---

### 🚫 Null Scan Limitations:
1. **Windows incompatibility:** Windows systems RFC standards follow nahi karte aur Null packets milne par open ports par bhi RST return karte hain, isliye Windows target par ye scan fail ho jata hai.
2. **Sudo Privileges Required:** Custom raw packets headers generate karne ke liye root access (`sudo`) lagta hai.

#### 🚪 Real-world Analogy: The Silent Treatment (Blank Envelope)
Socho aap ek hotel inspector ho:
- **Null Scan (`-sN`):** Aap room gate par knock karne ya door bell bajane ke badle door par aakar bas chup-chaap blank cardboard sheet laga kar khade ho jaate ho (Empty flag header):
  - **Closed Room:** Empty room ke security control system alert beep (RST) warning return kar dete hain.
  - **Open/Occupied Room:** Guest gate slot se dekhta hai ki koi abnormal decoration blank sheet gate par lagi hai, par security reason se wo silently ignore karke shant baitha rehta hai (Silence).

---

### 💻 Kali Linux Practice Task
Null scan test karne ke steps terminal par:

**Task 1: Selected ports par Null Scan run karna:**
```bash
sudo nmap -sN -p 22,80 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap Null Scan (`-sN`) packet headers mein kaun-kaun se TCP flags active/set hote hain?
- **A)** SYN, ACK, FIN
- **B)** Koi bhi flag set nahi hota (Blank Header)
- **C)** FIN, PSH, URG

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `sudo nmap -sN -p 22,80 scanme.nmap.org`
2. Check karein ki output mein open ports ka status kya print hota hai.
3. Quiz ka answer aur assignment output status mujhe chat mein share karein!

---