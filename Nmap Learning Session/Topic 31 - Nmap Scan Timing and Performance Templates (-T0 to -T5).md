---
title: "Topic 31 - Nmap Scan Timing and Performance Templates (-T0 to -T5)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 31: Nmap Scan Timing and Performance Templates (-T0 to -T5)

### 1. Explanation (Hinglish)
Nmap mein scans ki execute hone ki speed, probe intervals, packet timeouts, aur network bandwidth optimize karne ke liye **Timing Templates (flags: `-T0` se `-T5`)** use hote hain.

In timing templates ko dynamic networks aur security configurations ke tehat choose kiya jata hai:

---

### 📊 Timing Templates Comparison

| Template | Name | Speed / Behavior | Ideal Use-case |
| :--- | :--- | :--- | :--- |
| **`-T0`** | **Paranoid** | Extremely Slow (Waits 5 minutes between sending packets) | Intrusion Detection Systems (IDS) evasion checks. |
| **`-T1`** | **Sneaky** | Very Slow (Waits 15 seconds between sending packet probes) | Evasion checks for standard firewalls. |
| **`-T2`** | **Polite** | Slow (Waits 0.4 seconds, doesn't overload target system) | Industrial devices or critical servers tests. |
| **`-T3`** | **Normal** | Default Speed (No internal timeouts/performance changes) | Standard testing over standard networks. |
| **`-T4`** | **Aggressive** | Fast Speed (Reduces packet timeouts for faster execution) | Reliable, modern broadband connections. **(Most Popular Flag)** |
| **`-T5`** | **Insane** | Extremely Fast (Waits only milliseconds, high packet drop risk) | Fast local networks testing (can trigger firewalls instantly). |

---

### ⚖️ The Timing Trade-offs:
1. **Speed vs Detection:** Speed badhane (`-T4`/`-T5`) par scan fast khatam hota hai par firewalls/IDSs use **instantly block** kar dete hain. Speed kam karne (`-T0`/`-T1`) par scan silent ho jata hai par use complete hone mein ghante lag sakte hain.
2. **Speed vs Accuracy:** `-T5` use karne par network queue congestion hone ke karan probes drop ho sakte hain, jisse active open ports Nmap final screen par filtered/closed show ho sakte hain (False Negatives).

---

#### 🚪 Real-world Analogy: The Corridor Door Knocker
Socho aap ek hotel checking inspector ho:
- **`-T0` (Paranoid):** Aap ek room gate knock karte ho, fir corridor lounge mein jaakar **5 minutes rest karte ho**, fir aakar doosra gate knock karte ho. Security guard aapko normal guest samajh kar ignore kar deta hai (Stealth).
- **`-T3` (Normal):** Aap constant normal steps se chalkar har door check karte ho.
- **`-T4` (Aggressive):** Aap fast walking karte hue doors ko check karte ho.
- **`-T5` (Insane):** Aap corridor mein **full speed sprint (bhagte hue)** har gate par touch karke aage badhte ho. Kyunki aap bohot fast ho, security guard aapko instantly daudkar pakad leta hai (IDS Alert), aur speed ke karan aap 2-3 rooms check karna hi bhool jaate ho (Packet Drop/Accuracy loss).

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par speed differences test karne ke steps:

**Task 1: Aggressive speed scan run karna:**
```bash
nmap -T4 -p 22,80,443 scanme.nmap.org
```

**Task 2: Normal default scan run karna comparison ke liye:**
```bash
nmap -p 22,80,443 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap timing templates (`-T0` se `-T5`) mein se kaun sa template default speed control hota hai, jo scan command mein timing flag na set karne par automatic backend par apply ho jata hai?
- **A)** `-T2`
- **B)** `-T3`
- **C)** `-T4`

#### 🎯 Assignment
1. Kali Linux terminal par run karein: `nmap -T5 localhost` aur dynamic completion time note karein.
2. Phir run karein: `nmap localhost` (without timing flag).
3. Dono commands ke complete hone ke times compare karke quiz option aur results mujhe batayein!

---