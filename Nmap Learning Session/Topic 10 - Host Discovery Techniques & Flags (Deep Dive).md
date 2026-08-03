---
title: "Topic 10 - Host Discovery Techniques & Flags (Deep Dive)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 10: Host Discovery Techniques & Flags (Deep Dive)

### 1. Explanation (Hinglish)
Nmap alag-alag techniques ka combination use karta hai hosts ko discover karne ke liye:
- **`-sn`** (No Port Scan)
- **`-Pn`** (Treat all hosts as online - Skip Host Discovery)
- **`-PS`** (TCP SYN Ping)
- **`-PA`** (TCP ACK Ping)
- **`-PE`** (ICMP Echo Ping)

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par alag-alag Host Discovery techniques test karein:

**Task 1: Firewall bypass check (Skip Host Discovery):**
```bash
nmap -Pn scanme.nmap.org
```

**Task 2: TCP SYN Ping use karke selected ports par host discovery karna (no port scan):**
```bash
sudo nmap -sn -PS22,80,443 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Agar target host ka firewall standard ICMP (Ping) packets block kar raha hai, toh host discovery process ko skip karke direct port scan force karne ke liye Nmap mein kaunsa flag use kiya jata hai?
- **A)** `-sn`
- **B)** `-Pn`
- **C)** `-sS`

#### 🎯 Assignment
1. Kali Linux terminal par scan run karein: `nmap -Pn scanme.nmap.org`
2. Quiz ka answer aur completed tasks summary mujhe chat mein batayein!

---