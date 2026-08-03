---
title: "Topic 34 - Nmap Host Timeout (--host-timeout)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 34: Nmap Host Timeout (--host-timeout)

### 1. Explanation (Hinglish)
Bade systems aur networks ko scan karte waqt ek common problem aati hai: **Slow ya Unresponsive Targets**. 
Kai baar target systems bohot poor connectivity par hote hain, ya fir unke firewalls har scan request ko silently drop kar rahe hote hain. Aise systems par jab Nmap standard scan chalaata hai, toh timeouts ka wait karte-karte poora network scan **ghanto tak stuck (hang)** ho jata hai.

Is delay se bachne ke liye Nmap mein **`--host-timeout`** flag ka use kiya jata hai.

---

### ⚙️ `--host-timeout <time>` Flag
Yeh flag Nmap ko instruct karta hai ki agar koi computer system specified time range ke andar apna scan complete nahi karta, toh use scan list se **skip (drop)** kar diya jaye aur agle targets par focus kiya jaye.

#### ⏱️ Time formats structure:
- **`s`** (seconds): e.g., `30s` (30 seconds)
- **`m`** (minutes): e.g., `15m` (15 minutes)
- **`h`** (hours): e.g., `2h` (2 hours)
- Agar aap bina kisi unit ke value likhte hain, toh Nmap use **milliseconds** maanta hai (e.g., `60000` = 60 seconds).

---

#### 🚪 Real-world Analogy: The Interviewer's Stop Watch
Socho aap ek interviewer ho aur aapko ek din mein **100 candidates** ka interview lena hai:
- **Without Timeout:** Ek candidate aata hai jo har question ka reply dene mein 15-20 minutes sochta hai ya chup rehta hai (Slow/filtered host). Aap use tab tak room se nahi nikalte jab tak wo kuch na bole. Is akele candidate ke delay ki wajah se baki 90+ logo ka time waste ho jata hai aur audit scan stuck ho jata hai.
- **With Timeout (`--host-timeout 5m`):** Aap rule set karte ho ki har candidate ko **maximum 5 minutes** milenge. Agar candidate 5 minutes mein response nahi deta, toh aap interview interrupt karke use skip kar dete ho aur next candidate ko call karte ho. Isse interview speed constant bani rehti hai.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par timeout control verify karne ke steps:

**Task 1: Selected target par 1 minute limit set karke scan run karna:**
```bash
# Agar scan 1 minute mein complete nahi hua, toh Nmap use skip kar dega:
nmap --host-timeout 1m -p- scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap network scans ke dauran, slow ya filtered targets ki wajah se pura scan hang/stuck hone se bachane ke liye (maximum scan execution time limit control karne ke liye) kis flag ka use kiya jata hai?
- **A)** `--min-rtt-timeout`
- **B)** `--host-timeout`
- **C)** `-T0`

#### 🎯 Assignment
1. Kali Linux terminal par chalaein: `nmap --host-timeout 10s -p- scanme.nmap.org`
2. Dekhein ki kya target ports scan time 10 seconds cross hote hi skip/terminated message show karta hai.
3. Quiz ka answer aur assignment report updates mujhe chat mein share karein!

---