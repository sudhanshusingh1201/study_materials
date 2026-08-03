---
title: "Topic 02 - What is a Port Scan"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 2: What is a Port Scan?

### 1. Explanation (Hinglish)
**Port Scan** ek aisi technique hai jiske zariye hum yeh check karte hain ki target machine par kaun-kaun se **logical communication channels (Ports)** open hain.

Computer networking mein total **65,536 ports (0 se 65535)** hote hain. Har port ek specific service ke liye door (darwaza) hota hai:
- **Port 80:** Web traffic (HTTP)
- **Port 443:** Secure web traffic (HTTPS)
- **Port 22:** Remote Login (SSH)

#### 🚪 Real-world Analogy: The Door Knocker
Socho aap ek hotel ke corridor mein ho jahan **65,536 rooms** hain. Aap har room ke gate par jaakar knock (khadkhadate) karte ho:
1. **Open:** Andar se response aaya "Aao bhaiya, welcome!" (Target app listen kar rahi hai).
2. **Closed:** Andar se standard reply mila "Room empty hai" (System active hai par port par koi app nahi hai).
3. **Filtered:** Raste mein security guard (Firewall) ne aapko room ke paas jaane hi nahi diya (Packet drop ho gaya).

---

### 💻 Kali Linux Practice Task
Nmap mein specific ports scan karne ke liye **`-p`** flag ka use kiya jata hai.

**Task 1: Selected ports scan karna (Faster):**
```bash
nmap -p 22,80,443 scanme.nmap.org
```

**Task 2: Saare 65,535 ports scan karna (Slower):**
```bash
nmap -p- scanme.nmap.org
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Networking mein total kitne ports hote hain?
- **A)** 1024
- **B)** 65,536
- **C)** 80,808

#### 🎯 Assignment
1. Apne Kali Linux terminal par specific check run karein: `nmap -p 80 localhost`
2. Output dekhein ki kya aapka local web port open hai.
3. Quiz answer aur assignment output mujhe chat mein send karein!

---