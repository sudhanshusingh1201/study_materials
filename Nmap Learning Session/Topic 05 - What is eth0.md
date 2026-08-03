---
title: "Topic 05 - What is eth0"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 5: What is eth0?

### 1. Explanation (Hinglish)
**`eth0` (Ethernet 0)** Linux operating systems (jaise Kali Linux) mein use hone wala standard network interface name hai jo aapke computer ke **pehle wired Network Interface Card (NIC)** ko represent karta hai.

- **`eth`**: Ethernet (Wired Connection - LAN cable wala network).
- **`0`**: Zero-based index (matlab pehla physical wired port). Agar computer mein do LAN card honge, toh doosre ko `eth1` kaha jayega.

> [!NOTE]
> **Modern Linux note:** OS naming policies ke tehat `eth0` ke badle **`ens33`**, **`enp0s3`**, ya **`enp3s0`** jaise names bhi ho sakte hain, par virtual machines mein default name `eth0` hi rehta hai.

#### 🔌 Real-world Analogy: The Main LAN Port
Socho aapke laptop mein ek physical LAN (RJ45) port hai jahan aap ethernet cable lagate ho.
`eth0` us physical plug point ka **logical digital name** hai.
- Jab aap cable connect karenge, toh `eth0` active hoga aur router se use IP address milega.
- Jab cable nikal denge, toh `eth0` status disconnected show karega.

---

### 💻 Kali Linux Practice Task
Kali Linux terminal par `eth0` interface ko specific tareeqe se monitor aur manage karne ki commands:

**Task 1: Sirf `eth0` interface ki details dekhna:**
```bash
ifconfig eth0
```

**Task 2: `eth0` par hone wale live data transfers (packets) ko terminal par dekhna:**
```bash
sudo tcpdump -i eth0
```
*(tcpdump ek command-line packet sniffer hai jo eth0 ka traffic live terminal par print karega. Ise stop karne ke liye **Ctrl + C** press karein).*

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Linux system mein `eth` prefix kis type ke connection network ko represent karta hai?
- **A)** Wireless (Wi-Fi) connection.
- **B)** Wired Ethernet (LAN Cable) connection.
- **C)** Virtual Host connection.

#### 🎯 Assignment
1. Kali Linux terminal par check karein: `ifconfig eth0` (ya `ip a show eth0`).
2. Check karein ki kya aapke `eth0` interface ke paas abhi koi active IP address hai ya nahi.
3. RX (Received) aur TX (Transmitted) packets ka count check karein ki data send/receive hua hai ya nahi.
4. Quiz ka correct option aur local ethernet card status mujhe share karein!

---