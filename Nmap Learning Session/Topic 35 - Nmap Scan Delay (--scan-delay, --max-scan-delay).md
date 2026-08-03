---
title: "Topic 35 - Nmap Scan Delay (--scan-delay, --max-scan-delay)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 35: Nmap Scan Delay (--scan-delay, --max-scan-delay)

### 1. Explanation (Hinglish)
Nmap mein scans ko custom intervals par pause ya delay dene ke liye **Scan Delay (flags: `--scan-delay` aur `--max-scan-delay`)** use hote hain.

Yeh options speed controls ko fine-tune karne ke liye custom timers set karne ki direct permissions dete hain:

---

### ⚙️ `--scan-delay <time>`
Yeh flag Nmap ko force karta hai ki wo target ko bheje jaane wale **har ek probe packet ke beech kam se kam `<time>` gap maintain kare**.

#### ⏱️ Timers Syntax:
- **`s`** (seconds): e.g., `2s` (2 seconds)
- **`ms`** (milliseconds): e.g., `500ms` (500 milliseconds)
- **`m`** (minutes): e.g., `1m` (1 minute)

#### ❓ Iska use kyun kiya jata hai?
1. **Rate-Limiting Bypass (Firewall Evasion):** Modern Intrusion Prevention Systems (IPS) aur firewalls network behavior monitor karte hain (jaise: *"Agar ek source IP 1 second mein 10 packets bhejta hai, toh use block karo"*). Har packet ke beech 2-3 seconds ka gap (`--scan-delay 3s`) rakhkar hum is threshold check ko **bypass** kar sakte hain.
2. **Target Protection:** System crashes aur excessive traffic load control karne ke liye.

---

### ⚙️ `--max-scan-delay <time>`
Jab network par connection loss ya high latency hoti hai, toh Nmap automatically packets spacing (delay) badhane lagta hai. Lekin extreme poor network conditions par ye timer badhte-badhte **minutes** tak pahunch jata hai, jisse scan stuck ho jata hai.
- `--max-scan-delay` Nmap ko batata hai ki dynamic delay chahe jitna badhe, par wo is maximum `<time>` limit (e.g., `5s`) se **zyada slow nahi ho sakta** (maximum delay cap).

---

#### 🚪 Real-world Analogy: The Delivery Boy's Gap
Socho aap ek courier delivery boy (Nmap) ho jo ek high-security building ke corridor rooms mein mail deliver kar raha hai:
- **Without Scan Delay:** Aap bhagte hue lines se saare doors ek sath knock karte ho. Main security guard (firewall) abnormal behavior detect karke aapko instantly room se nikal deta hai (IDS Alert).
- **With `--scan-delay 5s`:** Aap room 101 knock karte ho, envelope deliver karte ho, **5 seconds wait karte ho**, phir room 102 par jaate ho. Guard ko lagta hai aap standard customer check-up kar rahe ho aur aap bypass ho jaate ho.
- **With `--max-scan-delay`:** Agar lift kharab hone se delay badhne lage, toh bhi aap decide karte ho ki main **10 seconds se zyada wait nahi karunga** next floor door checking ke liye (Delay cap limit).

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par delay control verify karne ke steps:

**Task 1: Selected ports par 2 seconds constant delay set karke scan run karna:**
```bash
nmap --scan-delay 2s -p 22,80 scanme.nmap.org
```
*(Notice karein packets completion timings interval gaps status).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Target firewalls aur IPS ke threshold rate-limiting rules (packets-per-second filters) ko bypass karne ke liye, har probe packet ke beech manually custom interval delay gap set karne ke liye kis flag ka use kiya jata hai?
- **A)** `--host-timeout`
- **B)** `--scan-delay`
- **C)** `-T5`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `nmap --scan-delay 500ms -p 22,80 localhost`
2. Scan monitor karein (`Spacebar` daba kar check karein timings gaps).
3. Quiz ka answer aur task details mujhe batayein!

---