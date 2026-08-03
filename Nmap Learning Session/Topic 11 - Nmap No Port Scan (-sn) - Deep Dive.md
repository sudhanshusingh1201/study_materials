---
title: "Topic 11 - Nmap No Port Scan (-sn) - Deep Dive"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 11: Nmap No Port Scan (-sn) - Deep Dive

### 1. Explanation (Hinglish)
Root/Sudo vs Non-Root user flow:
- **Sudo Privilege (`sudo nmap -sn <target>`):** Local targets par ARP use karta hai aur external par ICMP + TCP ports 80/443 + Timestamp probes.
- **Bina Sudo (`nmap -sn <target>`):** Socket connections on port 80/443 (TCP Connect calls) bhejta hai.

---

### 💻 Kali Linux Practice Task
Active hosts save karne ka workflow:

**Task 1: Sweep scan karke Grepable text format (`-oG`) mein save karna:**
```bash
sudo nmap -sn -oG live_hosts.txt 192.168.1.0/24
```

**Task 2: Grep aur Cut command se IP list nikalna:**
```bash
grep "Up" live_hosts.txt | cut -d " " -f 2
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Jab Nmap ko bina Root/Sudo privileges ke chalaya jata hai, toh `-sn` check ke liye kis raw protocol ka request packet nahi bhej sakta?
- **A)** TCP connection on port 80/443.
- **B)** ARP raw request.
- **C)** Standard connection setup.

#### 🎯 Assignment
1. Kali Linux terminal par normal account aur sudo se `-sn scanme.nmap.org` chala kar difference note karein.
2. Quiz answer aur feedback mujhe batayein!

---