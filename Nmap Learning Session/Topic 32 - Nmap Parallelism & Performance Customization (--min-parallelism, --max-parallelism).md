---
title: "Topic 32 - Nmap Parallelism & Performance Customization (--min-parallelism, --max-parallelism)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 32: Nmap Parallelism & Performance Customization (--min-parallelism, --max-parallelism)

### 1. Explanation (Hinglish)
Nmap by-default ek **highly parallel scanning tool** hai. Iska matlab hai ki scan speed badhane ke liye yeh ek baar mein ek port scan karne ke badle, network par multiple hosts aur ports par ek sath packets (probes) bhejta hai.

Nmap network latency aur reliability ko dekhte hue automatic parallelism ko control karta hai. Par custom network environments ke liye hum ise in flags se manually adjust kar sakte hain:

---

### 1. `--min-parallelism <number>`
- **Kya karta hai?** Yeh Nmap ko force karta hai ki wo network par kam se kam `<number>` packets ko outstanding state (sent but unanswered) mein active rakhe.
- **Kab use karein?** Jab target machine ka firewall active ho aur wo scanning request packets ko silently drop kar raha ho. Nmap response timeouts ke liye wait karte hue extreme slow ho jata hai. `--min-parallelism` set karne se scan speed drop nahi hoti aur forced speed maintain rehti hai.

### 2. `--max-parallelism <number>`
- **Kya karta hai?** Yeh Nmap ko limit karta hai ki wo network par ek sath `<number>` se zyada active probes na rakhe (upper cap limit).
- **Kab use karein?** Jab scanner ya target network connection weak ho, ya target hardware fragile ho (jaise industrial systems, IoT networks). Zyada packets ek sath bhejne par devices packet queue overload ke karan network crash kar sakte hain.

---

#### 🚪 Real-world Analogy: The Inspection Team (Parallelism)
Socho aap ek hotel checking manager ho:
- **Serial Scanning (No Parallelism):** Ek single inspector pehle room 101 check karta hai, fir wapas aakar room 102 check karta hai (Very slow).
- **Parallel Scanning (Default):** Aap ek sath 10 inspectors ko corridor mein check karne ke liye bhej dete ho (Fast).
- **`--min-parallelism 20`:** Aap rule lagate ho ki corridor mein **hamesha minimum 20 inspectors** ek sath active rahenge. Agar kuch rooms se reply aane mein delay ho, toh bhi speed drop nahi honi chahiye, forced speed par kaam chalta rahega.
- **`--max-parallelism 5`:** Aap strict cap lagate ho ki corridor mein **maximum 5 inspectors** hi ja sakte hain, taaki corridor mein traffic crowd (congestion) na badhe aur corridor locking system crash na ho.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par parallelism settings check karne ke tasks:

**Task 1: Forced fast execution check (Min 30 parallel probes):**
```bash
sudo nmap --min-parallelism 30 -p 1-1000 scanme.nmap.org
```

**Task 2: Low-bandwidth protective scanning check (Max 5 parallel probes limit):**
```bash
sudo nmap --max-parallelism 5 -p 1-1000 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Target firewall silent packet drop ke karan Nmap scanning speed ko drop hone se bachane ke liye (Forced speed limit maintain karne ke liye), kis custom performance flag ka use kiya jata hai?
- **A)** `--max-parallelism`
- **B)** `--min-parallelism`
- **C)** `-sV`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `sudo nmap --min-parallelism 100 -p 1-1000 localhost` aur timing check karein.
2. Phir chalaein: `sudo nmap --max-parallelism 5 -p 1-1000 localhost`.
3. Dono commands ke completion times note karke quiz answers ke sath mujhe batayein!

---