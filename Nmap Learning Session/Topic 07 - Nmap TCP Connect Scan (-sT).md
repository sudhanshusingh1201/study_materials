---
title: "Topic 07 - Nmap TCP Connect Scan (-sT)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 7: Nmap TCP Connect Scan (-sT)

### 1. Explanation (Hinglish)
**`-sT`** Nmap ka **TCP Connect Scan** flag hai. Yeh TCP protocols ko scan karne ka sabse standard aur basic mechanism hai.

Jab aapke paas system par root/administrator (`sudo`) permissions **nahi** hoti hain, tab Nmap default roop se isi scan ka use karta hai.

#### 🔄 Technical Process: The 3-Way Handshake
TCP Connect Scan target system ke socket API ke sath poora TCP connection standard tarike se complete karta hai:
1. **SYN:** Nmap target machine ke port par Connection Request (SYN) bhejta hai.
2. **SYN-ACK:** Agar target port open hai, toh system connection accept karke response (SYN-ACK) bhejta hai.
3. **ACK:** Nmap response milte hi connection confirm karne ke liye ACK packet bhejta hai (**Handshake Complete!**).
4. **RST:** Connection establish hone ke turant baad, Nmap use close karne ke liye RST (Reset) packet bhej deta hai.

#### 🤝 Real-world Analogy: Formal Meeting & Handshake
Socho aap kisi client ke office gate par jate ho:
1. Aap haath milane ke liye badhate ho (SYN).
2. Client haath badhakar aapse handshake start karta hai (SYN-ACK).
3. Aap dono formally handshake complete karte ho (ACK) aur aapas mein connect ho jate ho.
4. Handshake karte hi aap turant haath chhudakar wahan se chale jate ho (RST).

#### 📊 Pros vs Cons
- **Pros (Fayde):**
  - **No Root Required:** Bina `sudo` ke as a normal user chala sakte hain.
- **Cons (Nuksan):**
  - **Not Stealthy (Noise):** Target web servers ya firewalls ke logs mein aapka IP address easily capture ho jata hai.

---

### 💻 Kali Linux Practice Task
TCP Connect Scan run karne ke liye commands:

**Task 1: TCP Connect scan specific ports par bina sudo ke run karna:**
```bash
nmap -sT -p 22,80,443 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
TCP Connect scan (`-sT`) run karne par target system ke logs mein scan detect hone ke chances kyun zyada hote hain?
- **A)** Kyunki yeh pure packets ko drop kar deta hai.
- **B)** Kyunki yeh standard TCP 3-Way Handshake connection ko poora complete karta hai.
- **C)** Kyunki isme Nmap target PC ko crash kar deta hai.

#### 🎯 Assignment
1. Kali Linux terminal par normal user privilege (bina sudo ke) se run karein: `nmap -sT -p 22,80 scanme.nmap.org`
2. Scan completion time note karein aur output check karein.
3. Quiz ka answer aur completed scan summary mujhe share karein!

---