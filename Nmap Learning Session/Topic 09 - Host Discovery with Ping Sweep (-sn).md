---
title: "Topic 09 - Host Discovery with Ping Sweep (-sn)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 9: Host Discovery with Ping Sweep (-sn)

### 1. Explanation (Hinglish)
**Host Discovery** ka simple matlab hai: Network par active aur online devices (hosts) ka pata lagana. Aur **Ping Sweep** (Nmap mein **`-sn`** flag) iska sabse popular aur fast tareeqa hai.

Yeh target ports ko **bilkul scan nahi karta**. Yeh sirf check karta hai ki target device network par active hai ya nahi.

---

### 💻 Kali Linux Practice Task
Apne local network par ping sweep run karne ke liye:

**Task 1: Apne local subnet range ka pata lagana:**
```bash
ifconfig
```

**Task 2: Apne pure network range par Ping Sweep chalana:**
```bash
sudo nmap -sn 192.168.1.0/24
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap mein Host Discovery (Ping Sweep) scan chalane ke liye kis flag ka use kiya jata hai jisse port scanning completely skip ho jati hai?
- **A)** `-sS`
- **B)** `-sn`
- **C)** `-Pn`

#### 🎯 Assignment
1. Kali Linux terminal par check karein apna network IP.
2. Apne router subnet range par `sudo nmap -sn <subnet>` run karein.
3. Quiz ka answer aur host counts mujhe chat mein batayein!

---