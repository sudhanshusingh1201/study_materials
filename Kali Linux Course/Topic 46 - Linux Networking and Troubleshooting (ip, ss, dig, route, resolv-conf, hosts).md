---
title: "Topic 46 - Linux Networking & Troubleshooting (ip, ss, dig, route, /etc/hosts)"
tags:
  - kali-linux
  - cybersecurity
  - learning-session
type: course-topic
---

← [[Course on Kali Linux|Go Back to Course Hub]]

# 🌐 Topic 46: Linux Networking & Troubleshooting (ip, ss, dig, route, /etc/hosts)

Bhai, cyber security aur hacking me networking fundamental backbone hai. Kali Linux me target systems ko scan karne, connected devices ki details dekhne, local open ports audit karne aur DNS configurations modify karne ke liye Linux Networking utilities ka deep knowledge hona mandatory hai.

---

### 🏛️ Core Linux Networking Commands

#### 1. `ip` / `ifconfig` (Interface configuration checkers)
System ke network card interfaces, IP addresses aur MAC addresses ko check karne ke liye:
* **`ip a`** (IP Address details):
  ```bash
  ip a
  ```
  *(Isse network card adapters like `eth0`, `wlan0` ya `lo` ke configurations aur assigned IP addresses show hote hain).*
* **`ip link`** (MAC address details show karne ke liye):
  ```bash
  ip link show eth0
  ```

---

#### 2. `ss` / `netstat` (Socket Statistics & Listening Ports) 🚨
Hacking forensics aur system audit me sabse important command! Ye check karti hai ki aapke system par kaun-kaun se doors (ports) open hain aur kaunse connections active hain:
* **`-t`**: TCP connections.
* **`-u`**: UDP connections.
* **`-l`**: Listening sockets (jo connections accept karne ke liye ready hain).
* **`-p`**: Process name aur PID dikhana.
* **`-n`**: Numeric port numbers dikhana (jaise port 80, na ki http).
* **`ss -tulpn`** (Standard listening audit utility):
  ```bash
  sudo ss -tulpn
  ```
  *(Ye check karne ke liye bohot useful hai ki system me koi hidden backdoor port toh open nahi hai).*

---

#### 3. `route` / `ip route` (Gateway & Routing Tables)
Data packets network ke bahar jane ke liye kaunse router (gateway) ka route use kar rahe hain, use check karne ke liye:
```bash
ip route show
```
*(Isme `default via 192.168.1.1` likha hai toh 192.168.1.1 aapka router/gateway gateway IP hai).*

---

#### 4. `dig` & `nslookup` (DNS Query lookup)
Kisi domain name (jaise google.com) ka DNS record (A record, MX record) extract karne ke liye:
```bash
dig google.com
```

---

### 📁 Crucial Network Configuration Files

#### 1. `/etc/resolv.conf` (DNS Nameservers config)
Is file me bataya jata hai ki system ko DNS resolution (Name to IP conversion) karne ke liye kis DNS server ke paas jana hai:
```text
nameserver 8.8.8.8
```
*(Yahan Google DNS list configured hai).*

#### 2. `/etc/hosts` (Local Name resolver - IP Spoofing Vector ⚡)
Linux system real-world DNS server ke paas jaane se pehle is file me check karta hai. Agar isme koi matching listed hai, toh system wahi network IP load kar lega.
* *Cybersecurity Spoofing Trick:* Agar hacker target computer ki hosts file me line add kar de:
  ```text
  10.10.10.5  facebook.com
  ```
  Toh wo user jab bhi `facebook.com` open karega, browser real server ke bajaye hacker ke dummy IP `10.10.10.5` par redirect ho jayega!

---

### 🔑 Real-World Analogy (The Post Office & Sockets 🏢✉️)
* **`ip a` (Your Physical Address):** Jaise aapki building ka address aur main gate identity verify karna.
* **`ss -tulpn` (The Apartment Windows):** Check karna ki aapke apartment me kaun-kaun si windows/doors open hain aur unke pass kaunse security guards (services) baithe hain.
* **`ip route` (The Street Signs):** Wo directions signs jo packets ko batate hain ki highway (internet) par jaane ke liye pehle kis mod (router gateway) par mudna hai.
* **`/etc/hosts` (Your Personal Address Book):** Agar aapne apni address book me likh diya ki "Pharmacy = Rahul's House", toh aap pharmacy jaane ke liye direct Rahul ke ghar chale jayenge, poore town se nahi poochenge.

---

### 📝 10 Practice Questions/Tasks for You!

Bhai, networking parameters verify karne ke liye in tasks ko terminal par execute karein:

1. **Task 1:** Apne current system interface list check karne aur active IP address identify karne ke liye **`ip a`** run karein.
2. **Task 2:** System me connected ethernet cards ke dynamic traffic link status check karne ke liye `ip -s link` test run karein.
3. **Task 3:** Sudo permissions ke sath open listening ports check karein: **`sudo ss -tulpn`** aur verify karein kaunse service port active hain.
4. **Task 4:** default gateway IP check karne ke liye routing command verify karein: `ip route show` aur default route IP status identify karein.
5. **Task 5:** Ek basic network connectivity check latency ping test google DNS check verify karein: `ping -c 3 8.8.8.8`.
6. **Task 6:** Domain name `kali.org` ke detailed DNS records query run karne ke liye appropriate **`dig kali.org`** chala kar output check karein.
7. **Task 7:** DNS resolution nameservers check karne ke liye resolv configuration file parameters read karein: `cat /etc/resolv.conf`.
8. **Task 8:** `/etc/hosts` file inspect karein aur observe karein ki local loopback address `127.0.0.1` kis-kis domain name par mapped hai: `cat /etc/hosts`.
9. **Task 9:** DNS troubleshooting test check ke liye `nslookup kali.org` run karein aur address lists check karein.
10. **Task 10:** Hacking local redirects simulations me target computers `/etc/hosts` entry manipulations karne ke standard scope significance kya hain? 2 lines me explain karein.

---
