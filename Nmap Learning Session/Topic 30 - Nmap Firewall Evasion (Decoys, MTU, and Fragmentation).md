---
title: "Topic 30 - Nmap Firewall Evasion (Decoys, MTU, and Fragmentation)"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 30: Nmap Firewall Evasion (Decoys, MTU, and Fragmentation)

### 1. Explanation (Hinglish)
Jab target systems par robust firewalls ya Intrusion Detection Systems (IDS/IPS) active hote hain, toh wo standard Nmap scans ko detect karke drop/block kar dete hain. Unhe bypass karne ke liye Nmap mein key evasion methods use kiye jate hain:

---

### 1. Packet Fragmentation (`-f`) aur MTU (`--mtu`)
- **`-f` (Fragmentation):** Yeh flag Nmap ke standard 20-byte TCP headers ko 8-byte ke chote-chote fragments (tukdo) mein split kar deta hai. Do baar `-f` (`-ff`) likhne par fragments 16-byte segments mein split hote hain.
- **`--mtu <value>`:** Is option se hum custom transmission unit size specify kar sakte hain. **MTU value hamesha 8 ka multiple hona chahiye** (jaise 8, 16, 24, 32, etc.).
- **Bypass Logic:** Kuch firewalls aur IDSs chote packet fragments ko reassemble (wapas jodkar inspect) nahi karte. Wo sirf pehla fragment verify karte hain jisme incomplete header hone ke karan port information visible nahi hoti, aur access bypass ho jata hai.

---

### 2. Decoys (`-D`)
- **`-D <decoy1,decoy2,ME,...>`:** Target security monitors ko confuse aur logs mein heavy traffic noise fill karne ke liye decoy scan use hota hai.
- **Kaise kaam karta hai?** Nmap aapke scan ke sath-sath decoy spoofed IP addresses se bhi requests bhejta hai. Target firewall ko aisa dikhega ki 5-10 different servers use ek sath scan kar rahe hain.
- **ME Keyword:** Decoy IPs ki list ke beech mein **`ME`** keyword represent karta hai aapke system ke real/original IP address ko.

---

#### 🚪 Real-world Analogy: The Secret Agent Delivery
Socho aap ek VIP high-security building mein check-point pass karna chahte ho:
- **Fragmentation (`-f`):** Aap document ko ek bada envelope mein bhejne ke badle, use scissors se **10 chote pieces** mein cut karte ho aur alag-alag normal envelopes mein daal dete ho. Guards envelopes open karte hain par unhe akele pieces waste paper lagte hain aur wo bypass allow kar dete hain. Andar jaakar aap pieces assemble kar lete ho.
- **Decoys (`-D`):** Aap checkpoint par akele jaane ke badle, apne sath **10 look-alike fake agents (decoys)** ko khada karte ho jo aapki hi tarah dikhte hain. Guards confuse ho jate hain aur ye track nahi kar pate ki real document deliver kisne kiya.

---

### 💻 Kali Linux Practice Task
*Note: Packet spoofing aur customized fragmentation ke liye root (`sudo`) permissions lagti hain.*

**Task 1: Selected ports par fragmentation scan run karna:**
```bash
sudo nmap -f -p 22,80 scanme.nmap.org
```

**Task 2: Custom MTU segment (e.g., 16 bytes) set karke test run karna:**
```bash
sudo nmap --mtu 16 -p 22,80 scanme.nmap.org
```

**Task 3: Spoofed Decoy scan execute karna:**
```bash
sudo nmap -D 8.8.8.8,1.1.1.1,ME -p 22,80 scanme.nmap.org
```
*(Yahan target logs mein dikhega ki Google `8.8.8.8` aur Cloudflare `1.1.1.1` ke sath aapke real IP ne target scan kiya hai).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Nmap decoy scan (`-D`) command line parameters list mein, scanner ke real/original IP address ko fake decoy list ke beech hide/represent karne ke liye kis keyword ka use kiya jata hai?
- **A)** `REAL`
- **B)** `ME`
- **C)** `SELF`

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `sudo nmap -D 8.8.8.8,ME -p 80 scanme.nmap.org`
2. Monitor karein scan time. Kya decoy IPs setup scanning process noise increase hone ke karan completion time extend karta hai?
3. Quiz ka answer aur assignment output mujhe chat mein share karein!

---