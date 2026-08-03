---
title: "Topic 24 - Inverse TCP Flag Scanning (-sN, -sF, -sX)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 24: Inverse TCP Flag Scanning (-sN, -sF, -sX)

### 1. Explanation (Hinglish)
**Inverse TCP Flag Scanning** ek advanced port scanning technique hai jisme standard TCP 3-Way Handshake (jaise SYN request) ka use nahi kiya jata. Iske badle Nmap target ports par **invalid ya unexpected TCP flags combinations** bhejta hai.

Is technique ke andar Nmap ke 3 main scanning flags aate hain:
1. **Null Scan (`-sN`):** Packet headers mein koi bhi TCP flag set nahi hota (bilkul blank request).
2. **FIN Scan (`-sF`):** Packet mein sirf **FIN (Finish)** flag set hota hai (jo normally connection close karne ke liye use hota hai).
3. **Xmas Scan (`-sX`):** **FIN, PSH, aur URG** teeno flags ek sath set hote hain. Ise Xmas (Christmas) scan isliye kehte hain kyunki packet header ke indicators ek Christmas tree ki lights ki tarah chamak uthte hain.

---

### 🔄 Technical Rules (RFC 793 Standards)
TCP standard RFC 793 rules ke mutabik unexpected packets ke liye targets ka response:
- **Closed Port:** Target port closed hone par target OS directly **RST (Reset)** packet return karega.
- **Open Port:** Target port open hone par target system unexpected packet ko **ignore (drop)** kar dega aur koi response nahi bhejega (Silence).

Is inverse logic se Nmap port state calculate karta hai:
- **RST packet mila** = Port **Closed** hai.
- **Kuch nahi mila (Silence)** = Port **Open|Filtered** hai (sure nahi ho sakta ki port open hai ya firewall block kar raha hai).

---

### 🚫 Windows Exception (The Loophole)
Microsoft Windows, print servers, aur network devices RFC 793 rule ko strictly follow nahi karte. Windows systems par chahe port open ho ya closed, unexpected packets milne par wo hamesha **RST** packet bhejte hain.
- **Isliye:** Null, FIN, aur Xmas scans Windows target computers par kaam nahi karte (wo sabhi ports ko Closed dikhayenge). Yeh scans sirf Unix/Linux/macOS systems par hi work karte hain.

#### 🚪 Real-world Analogy: The Silent Treatment
Socho aap ek hotel corridor checking par ho:
- **SYN Scan (Standard):** Aap main door knock karke clear check-up karte ho.
- **Inverse Scan (Ajeeb behaviour):** Aap door bell bajane ke badle door key handle ko click-toggle karte ho:
  - **Closed Room:** Agar room khali hai toh automatic door lock warning signal beep (RST) de dega.
  - **Open/Occupied Room:** Guest andar soya hai, wo aapki ajeeb activity par door lock warning sunkar bhi ignore karke shant baitha rehta hai (Silence).
  *Agar beep aayi toh room empty (Closed) hai, aur agar silence mila toh room occupied (Open|Filtered) hai.*

---

### 💻 Kali Linux Practice Task
*Note: Custom TCP raw packet building ke liye in scans ko run karne ke liye superuser (`sudo`) access lagta hai.*

**Task 1: Selected ports par Xmas Scan run karna:**
```bash
sudo nmap -sX -p 22,80 scanme.nmap.org
```

**Task 2: Null Scan execute karna target par:**
```bash
sudo nmap -sN -p 22,80 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Inverse TCP scans (`-sN`, `-sF`, `-sX`) chalane par, agar target port open hota hai aur target system standard RFC 793 rules follow karta hai, toh Nmap use kis port status mein mark karta hai?
- **A)** Open
- **B)** Closed
- **C)** Open|Filtered

#### 🎯 Assignment
1. Kali Linux terminal par local system target par run karein: `sudo nmap -sX -p 22 localhost`
2. Output verify karein ki kya SSH port 22 status `Open|Filtered` show hota hai.
3. Quiz ka answer aur assignment output mujhe chat mein batayein!

---