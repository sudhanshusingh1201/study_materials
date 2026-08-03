---
title: "Topic 26 - Nmap Xmas Scan (-sX)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 26: Nmap Xmas Scan (-sX)

### 1. Explanation (Hinglish)
Nmap mein **`-sX`** flag ko **Xmas Scan** (ya Christmas Scan) kaha jata hai. Yeh inverse TCP flag scanning family ka sabse famous member hai.

#### ❓ Is scan ko "Xmas Scan" kyun bolte hain?
Is scan mein Nmap jo TCP packet bhejta hai, usme teen specific flags ko ek sath active (set) kiya jata hai:
- **FIN** (Finish)
- **PSH** (Push)
- **URG** (Urgent)

Jab hum in teeno flags ko packet header mein set karte hain, toh packet analyzer tools (jaise Wireshark) ke flags settings block mein ye teeno option yellow/bright highlight dikhte hain. Yeh dekhne mein aisa lagta hai jaise koi **Christmas Tree (Xmas Tree) lights se saja ho**.

---

### 🔄 Technical Mechanism (RFC 793 Standards)
Target system ka standard response rules:
- **Closed Port:** Target port closed hone par target system directly **RST (Reset)** packet return karega.
- **Open Port:** Target port open hone par system in unexpected flags wale packets ko **ignore/drop** kar dega (chup rahega).

Nmap is logic ke base par results output screen par show karta hai:
- **RST response mila** = Port **Closed** hai.
- **No response (Silence)** = Port **Open|Filtered** hai (matlab ya toh open hai ya firewall block kar raha hai).

---

### 🚫 Xmas Scan Limitations:
1. **Windows incompatibility:** Windows architecture systems RFC 793 rule follow nahi karte aur standard ports open hone par bhi RST bhejte hain, isliye Windows target par ye scan fail ho jata hai.
2. **Sudo Privileges Required:** Custom raw packets headers generate karne ke liye root access (`sudo`) lagta hai.

#### 🚪 Real-world Analogy: The blinking gift package
Socho aap ek hotel inspector ho:
- **Xmas Scan (`-sX`):** Aap room gate par formal checkup knock karne ke badle gate lock handle par ek decoration packet laga dete ho jisme red, green, aur blue blinkers (FIN, PSH, URG) ek sath jhal-mhal kar rahe hain:
  - **Closed Room:** Empty room ke security sensor light parameters warning signal beep (RST) de dete hain.
  - **Open/Occupied Room:** Guest andar se is ajeeb blinking tool ko dekhta hai, par safety reasons se chup baitha rehta hai aur door open nahi karta (Silence).

---

### 💻 Kali Linux Practice Task
Xmas scan test karne ke steps terminal par:

**Task 1: Selected ports par Xmas Scan fast parameters ke sath chalana:**
```bash
sudo nmap -sX -T4 -p 22,80,443 scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap Xmas Scan (`-sX`) packet headers mein kaun-kaun se TCP flags ek sath active/set hote hain?
- **A)** SYN, ACK, FIN
- **B)** FIN, PSH, URG
- **C)** RST, SYN, ACK

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `sudo nmap -sX -p 22,80,443 scanme.nmap.org`
2. Check karein ki output mein open ports ka status kya print hota hai.
3. Quiz ka answer aur assignment output status mujhe chat mein share karein!

---