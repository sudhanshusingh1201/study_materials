---
title: "Topic 15 - OS and Service Version Scanning (-O, -sV, -A)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 15: OS and Service Version Scanning (-O, -sV, -A)

### 1. Explanation (Hinglish)
- **Service Version Detection (`-sV`):** Open ports par chalne wali standard application software package aur uska version details dhoondhna (e.g., Apache 2.4.41). Known vulnerability search karne ke liye zaroori hai.
- **OS Detection (`-O`):** target ke TCP/IP stack behavior (fingerprinting) se uske Operating System (Windows, Linux, macOS) ka guess karna.
- **Aggressive Scan (`-A`):** Version scanning (`-sV`), OS detection (`-O`), Default scripts (`-sC`), aur Traceroute ko ek sath chalane wala combo flag.

---

### 💻 Kali Linux Practice Task
*Note: OS Detection (`-O`) ke liye superuser root/sudo privileges lagti hain.*

**Task 1: Selected ports par Service Version check karna (Faster):**
```bash
nmap -sV -p 22,80,443 scanme.nmap.org
```

**Task 2: Target system ka Operating System (OS) detect karna:**
```bash
sudo nmap -O scanme.nmap.org
```

**Task 3: Aggressive Scan (`-A`) chalakar detail analysis karna:**
```bash
sudo nmap -A -p 80,22 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap mein target system ke open ports par chalne wale exact application software version details pata karne ke liye kis flag ka use kiya jata hai?
- **A)** `-O`
- **B)** `-sV`
- **C)** `-Pn`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `sudo nmap -sV -O scanme.nmap.org`
2. Scan output check karke batayein:
   - Port 80 ya Port 22 par kaun si service aur uska exact version chal raha hai?
   - Target machine par kaun sa OS guess kiya gaya?
3. Quiz ka answer aur assignment answers mujhe batayein!

---