---
title: "Topic 01 - What is Nmap"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 1: What is Nmap?

### 1. Explanation (Hinglish)
**Nmap (Network Mapper)** ek powerful, free, aur open-source utility hai jo networks ko explore aur audit karne ke liye use hoti hai. Simple shabdon mein, yeh kisi system ya network ka **digital X-ray** nikalta hai.

#### 🛡️ Real-world Analogy: The Building Inspector
Socho aap ek building ke Security Inspector ho:
1. Aap pehle check karte ho ki building ka address sahi hai ya nahi (Host Discovery).
2. Fir aap check karte ho ki building ke kaun-kaun se **darwaze aur khidkiyan (Ports)** open hain ya locked (Port Scanning).
3. Jo darwaze open hain, unke andar kaun si activity ya kaun log kaam kar rahe hain, ye dekhte ho (Service Version Detection).
Nmap bilkul yahi inspector ka kaam networks ke liye karta hai.

---

### 💻 Kali Linux Practice Task
Apne Kali Linux terminal par jaakar ye basic scan command run karein:
```bash
nmap scanme.nmap.org
```
> [!IMPORTANT]
> `scanme.nmap.org` Nmap organization ka ek official, authorized test target hai. Bina authorization ke kisi bhi public website ko scan karna illegal hai.

**Expected Output:**
Nmap aapko batayega ki:
- Target machine up (online) hai.
- Uske kaun se common ports open hain (e.g., SSH port 22 ya HTTP port 80).
- Har port par kaun si service listen kar rahi hai.

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Agar Nmap ke output mein kisi port ka status **"Filtered"** likha aata hai, toh iska kya matlab hota hai?
- **A)** Port 100% closed hai.
- **B)** Target system band (offline) hai.
- **C)** Firewall ya security system Nmap ke probes ko target tak pahunchne se block kar raha hai.

#### 🎯 Assignment
1. Apne Kali Linux terminal par ye command run karein: `nmap localhost` (ya `nmap 127.0.0.1`).
2. Dekhein ki aapke local Kali machine par koi ports open hain ya nahi.
3. Output ko mere saath chat mein share karein!

---