---
title: "Topic 18 - TCP Connect Scan vs TCP SYN Stealth Scan (-sT vs -sS)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 18: TCP Connect Scan vs TCP SYN Stealth Scan (-sT vs -sS)

### 1. Explanation (Hinglish)
Nmap mein TCP ports ko scan karne ke do sabse popular aur fundamental tarike hain: **TCP Connect Scan (`-sT`)** aur **TCP SYN Stealth Scan (`-sS`)**. Inke packet structure aur behavior ke difference ko samajhna target discovery mein sabse critical phase hai.

---

### 🔄 Technical Handshake comparison

| Feature | TCP Connect Scan (`-sT`) | TCP SYN Stealth Scan (`-sS`) |
| :--- | :--- | :--- |
| **Common Name** | Full-Open Scan | Half-Open / Stealth Scan |
| **TCP Handshake** | Complete 3-Way Handshake (`SYN -> SYN-ACK -> ACK`) | Incomplete Handshake (`SYN -> SYN-ACK -> RST`) |
| **Sudo Required?** | **No** (Normal user chalakar connect socket call use kar sakta hai) | **Yes** (Raw packets design karne ke liye superuser permission zaroori hai) |
| **Stealth Level** | **Low** (Target service logs mein connections fully visible hote hain) | **High** (Connection establish nahi hota, isliye application logs clean rehte hain) |
| **Scan Speed** | Slightly Slower | Faster (Connection completion overhead nahi hota) |

---

#### 🤝 Packet Flow in detail (Open Port):
1. **TCP Connect Scan (`-sT`):**
   - **SYN:** Scanner connection request bhejta hai.
   - **SYN-ACK:** Target connection accept karta hai.
   - **ACK:** Scanner handshake complete karta hai (**Connection Established!**).
   - **RST:** Scanner turant connection close karne ke liye reset packet bhejta hai.

2. **TCP SYN Stealth Scan (`-sS`):**
   - **SYN:** Scanner connection request bhejta hai.
   - **SYN-ACK:** Target connection accept karta hai (indicates port is open).
   - **RST:** Scanner handshake complete karne ke badle **direct RST (Reset) packet** bhej kar connection request break kar deta hai.

---

#### 🚪 Real-world Analogy: Greeting and Running Away
Socho aap kisi ke door (port) par check karne jate ho:
- **TCP Connect Scan (`-sT`):** Aap gate knock karte ho (SYN). Owner gate kholkar kehta hai—*"Aaiye andar baithiye"* (SYN-ACK). Aap andar jaakar formally handshake karte ho aur baithte ho (ACK). Phir aap turant bolte ho—*"Acha main chalta hoon"* (RST). Owner ke brain aur entry log mein aapka name-pata note ho chuka hai (Noisy).
- **TCP SYN Stealth Scan (`-sS`):** Aap gate knock karte ho (SYN). Owner gate khol kar haath badhata hai handshake ke liye (SYN-ACK). Aap gate khulte hi bina haath milaye aur bina ghar mein ghuse wahan se bhaag khade hote ho (RST). Kyunki aap formally ghar ke andar aaye hi nahi, isliye owner ke entry register mein aapki koi entry record nahi hoti (Stealthy).

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par in scans ka visual behavior test karein:

**Task 1: TCP SYN Stealth Scan run karna (Requires Root):**
```bash
sudo nmap -sS -p 22,80,443 scanme.nmap.org
```

**Task 2: TCP Connect Scan run karna (Sudo warning check):**
```bash
# normal account se run karein:
nmap -sT -p 22,80,443 scanme.nmap.org
```
*(Notice karein bina sudo ke default Connect mode chalta hai).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
TCP SYN Stealth scan (`-sS`) ko "Half-Open Scan" kyun kaha jata hai?
- **A)** Kyunki ye half ports ko open aur half ko filtered chhod deta hai.
- **B)** Kyunki ye standard TCP 3-Way Handshake connection process ko complete karne ke badle midway (SYN-ACK milte hi) RST packet bhejkar interrupt kar deta hai.
- **C)** Kyunki ye packet speed ko safe templates ke basis par half kar deta hai.

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `sudo nmap -sS -p 80 scanme.nmap.org`
2. Wireshark start karke active LAN interface par filter lagayein: `tcp.port == 80`
3. Check karein ki packet exchanges mein target system se SYN-ACK milte hi aapke Kali machine ne RST packet bheja ya ACK packet.
4. Quiz answer aur assignment parameters mujhe chat mein share karein!

---