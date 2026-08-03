---
title: "Topic 14 - Nmap -Pn (No Ping) Scan with Real IP Address Example"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 14: Nmap -Pn (No Ping) Scan with Real IP Address Example

### 1. Case-Sensitivity Warning ⚠️
- `-pn` (lowercase) is invalid.
- `-Pn` (Capital P) is correct.

### 2. Explanation with Real IP Example
Maan lijiye target IP `192.168.1.45` ya `45.33.32.156` hai:
```bash
nmap -Pn 192.168.1.45
```
Yeh ping checks skip karke direct port scan force karta hai. Windows Defender ya firewalls jo standard ICMP Ping block karte hain, unhe scan karne ke liye ye zaroori hai.

---

### 💻 Kali Linux Practice Task
- **Task 1:** `nmap 192.168.1.45` (standard check).
- **Task 2:** `nmap -Pn 192.168.1.45` (bypass check).

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Target IP `192.168.1.100` par host discovery (ping check) bypass karke direct port scan force karne ke liye kaunsi command correct hai?
- **A)** `nmap -pn 192.168.1.100`
- **B)** `nmap -Pn 192.168.1.100`
- **C)** `nmap -sn 192.168.1.100`

#### 🎯 Assignment
1. Kali terminal par public target check karein: `nmap -Pn 45.33.32.156`
2. Quiz answer aur terminal output feedback mujhe chat mein share karein!

---