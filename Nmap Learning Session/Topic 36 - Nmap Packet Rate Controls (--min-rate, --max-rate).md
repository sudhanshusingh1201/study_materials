---
title: "Topic 36 - Nmap Packet Rate Controls (--min-rate, --max-rate)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 36: Nmap Packet Rate Controls (--min-rate, --max-rate)

### 1. Explanation (Hinglish)
Nmap scan speed aur target load control karne ka ek aur bohot direct aur powerful tareeqa hai: **Packet Rate Limits (flags: `--min-rate` aur `--max-rate`)**.

Yeh flags Nmap ko instruct karte hain ki use **ek second mein minimum ya maximum kitne packets (probes)** target par send karne hain. Ise network security language mein **PPS (Packets Per Second)** kehte hain.

---

### ⚙️ `--min-rate <number>`
- **Kya karta hai?** Yeh Nmap ko force karta hai ki wo scan ke dauran **kam se kam** `<number>` packets per second ki speed se packets send kare. E.g., `--min-rate 1000` set karne se Nmap kam se kam 1000 packets per second bhejega.
- **Ideal use-case:** Jab hume bohot bade IP ranges (jaise pure `/16` network jisme 65,536 targets hote hain) scan karne hon aur hum chahte hain ki network timeouts ke delay ko ignore karke scan super-fast complete ho.

### ⚙️ `--max-rate <number>`
- **Kya karta hai?** Yeh strict upper ceiling limit lagata hai ki Nmap kisi bhi haal mein **`<number>` packets per second se zyada speed** se scan na kare. E.g., `--max-rate 50` set karne se Nmap 1 second mein maximum 50 packets hi bhejega.
- **Hume iski zarurat kyun hoti hai?**
  1. **Device Safety:** Fragile networking devices (IoT hardware, old router, printing machines) par high-rate traffic packets crash block trigger kar sakta hai.
  2. **Bandwidth Protection:** Apne scanner systems ki network bandwidth choke hone se bachane ke liye.
  3. **Stealth:** Low packet rate target firewall rule triggers ko avoid karne mein help karta hai.

---

#### 🚪 Real-world Analogy: The Water Pump Controller (Packet Rates)
Socho aap ek garden hose pipes system handle kar rahe ho:
- **`--min-rate 1000` (High Pressure Pump):** Aap pump ki speed set karte ho ki **1 second mein 1000 drops (packets)** water flow continuously pipe se nikalna chahiye. Garden jaldi irrigate (scan) ho jayega par high pressure se patle plant leaves (weak target systems) damage/crash ho sakte hain.
- **`--max-rate 50` (Drip Irrigation):** Aap strictly restrict kar dete ho ki controller device **1 second mein 50 drops** se zyada water flow allow na kare. Isse scanning process thoda slow chalega par local network pipes aur systems burst (congestion/crash) nahi honge aur safe checking flow chalta rahega.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par packet rate limits test karne ke tasks:

**Task 1: Selected ports par 50 packets per second ki maximum limit set karke scan chalaein:**
```bash
sudo nmap --max-rate 50 -p 1-500 scanme.nmap.org
```

**Task 2: Fast speed testing check (Min 500 packets per second rate):**
```bash
sudo nmap --min-rate 500 -p 1-500 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap scanning performance custom settings ke tehat, 1 second mein maximum kitne packets (PPS) targets par bheje ja sakte hain uski upper safety ceiling limit set karne ke liye kis flag ka use kiya jata hai?
- **A)** `--min-rate`
- **B)** `--max-rate`
- **C)** `--host-timeout`

#### 🎯 Assignment
1. Apne terminal par scan chalaein: `sudo nmap --max-rate 10 -p 1-200 localhost` aur monitor karein scan latency.
2. Phir chalaein: `sudo nmap --min-rate 200 -p 1-200 localhost`.
3. Dono commands ke execution speeds compare karke quiz answers ke sath mujhe batayein!