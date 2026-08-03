---
title: "Topic 03 - What is ifconfig"
tags:
  - nmap
  - kali-linux
  - learning-session
  - cybersecurity
type: course-topic
---

← [[Nmap_Kali_Learning_Session|Go Back to Nmap Journal Hub]]

# 🌐 Topic 3: What is ifconfig?

### 1. Explanation (Hinglish)
**`ifconfig` (Interface Configuration)** ek aisi command-line utility hai jo Linux aur Unix operating systems (jaise Kali Linux) mein network interfaces (Ethernet, Wi-Fi cards, etc.) ko configure aur unki details view karne ke liye use hoti hai.

Is command se hume apne computer ke network adapters ke baare mein zaroori details milti hain:
1. **IP Address:** Device ka network address (e.g., `inet 192.168.1.15`).
2. **MAC Address:** Physical/Hardware Address (e.g., `ether 00:0c:29:3e:ab:cd`).
3. **Subnet Mask:** Netmask details (e.g., `netmask 255.255.255.0`).
4. **Interface Status:** Interface active (UP) hai ya band (DOWN).

> [!NOTE]
> **Modern Linux note:** Naye Linux systems mein `ifconfig` ke jagah `ip a` (ip address) command default standard ban gayi hai, par hacking/pentesting community mein `ifconfig` abhi bhi bohot common hai.

#### 📇 Real-world Analogy: The ID Card & Switchboard
Socho aap ka computer ek corporate office hai jahan multiple departments (network interfaces) hain:
- **`eth0` (Ethernet):** Wired connection line.
- **`wlan0` (Wi-Fi):** Wireless connection line.
- **`lo` (Loopback):** Office ka internal intercom system jo self-communication (127.0.0.1) ke liye use hota hai.
`ifconfig` run karna matlab office ke switchboard aur har line ki identity card check karne jaisa hai ki kaun si network line chalu hai, aur kis line ka number (IP) kya hai.

---

### 💻 Kali Linux Practice Task
Apne Kali Linux terminal par ye commands test karein:

**Task 1: Sabhi Active Interfaces ki list dekhna:**
```bash
ifconfig
```
*(Agar Kali mein error aaye, toh `sudo apt install net-tools` chala kar ise install kar sakte hain, ya fir **`ip a`** command use kar sakte hain).*

**Task 2: Kisi Interface ko temporary disable/enable karna (needs root privileges):**
```bash
# Interface band karne ke liye:
sudo ifconfig eth0 down

# Interface wapas chalu karne ke liye:
sudo ifconfig eth0 up
```

---

### 📝 Quiz & Assignment

#### ❓ Quiz Question
Self-testing ya internal network loops ke liye use hone wale default **Loopback IP (localhost)** address kya hota hai?
- **A)** 192.168.1.1
- **B)** 127.0.0.1
- **C)** 8.8.8.8

#### 🎯 Assignment
1. Apne Kali Linux terminal par `ifconfig` (ya `ip a`) run karein.
2. Apne computer ka active interface name, **IP address** aur **MAC address** find out karein.
3. Dono values aur quiz ka answer mujhe chat mein share karein!

---