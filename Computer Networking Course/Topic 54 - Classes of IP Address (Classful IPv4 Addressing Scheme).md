---
title: "Topic 54 - Classes of IP Address (Classful IPv4 Addressing Scheme)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🏷️ 54. Classes of IP Address (Classful IPv4 Addressing Scheme)

### 📝 Introduction (Intro)
IPv4 addresses ko early internet days (1980s) me simplify aur organize karne ke liye ek system design kiya gaya tha jise **Classful Addressing** kehte hain. Is addressing schema me pure IPv4 range ($0.0.0.0$ to $255.255.255.255$) ko total **5 Classes (Class A, B, C, D, E)** me divide kiya gaya tha. Iska main indicator IP ke pehle group (First Octet) ka decimal value hota hai.

#### 🔑 The 5 IPv4 Classes Breakdown:
1. **Class A (Very Large Networks):**
   * *Range:* `1.0.0.0` to `126.255.255.255`. (First Octet high bit is always `0`).
   * *Structure:* 1 octet Network ID, 3 octets Host ID (`N.H.H.H`). Default Mask: `255.0.0.0` (`/8`).
   * *Capacity:* $126$ networks, aur har network me $16.7$ million hosts.
   * *Note:* `127.x.x.x` ranges loopback testing diagnostics ke liye reserve hain.
2. **Class B (Medium to Large Networks):**
   * *Range:* `128.0.0.0` to `191.255.255.255`. (First bits are always `10`).
   * *Structure:* 2 octets Network ID, 2 octets Host ID (`N.N.H.H`). Default Mask: `255.255.0.0` (`/16`).
   * *Capacity:* $16,384$ networks, aur har network me $65,534$ hosts.
3. **Class C (Small Networks):**
   * *Range:* `192.0.0.0` to `223.255.255.255`. (First bits are always `110`).
   * *Structure:* 3 octets Network ID, 1 octet Host ID (`N.N.N.H`). Default Mask: `255.255.255.0` (`/24`).
   * *Capacity:* $2$ million networks, aur har network me $254$ hosts.
4. **Class D (Multicasting):**
   * *Range:* `224.0.0.0` to `239.255.255.255`. (First bits are always `1110`).
   * *Structure:* Koi Subnet mask nahi hota. Ye target devices groups ko ek sath packets forward karne (**Multicasting**) ke liye reserved hai.
5. **Class E (Experimental / Research):**
   * *Range:* `240.0.0.0` to `254.255.255.255`. (First bits are always `1111`).
   * *Structure:* No Subnet mask. Ye futuristic research and military R&D projects ke liye reserved hai.

### ➕ Advantages (Fayde)
* **Simple Routing Decisions:** Purane basic routers ke pass processing power kam thi. Wo sirf first octet ki class value read karke path optimization decisions fast le lete the.
* **Easy IP Planning:** Starting scale me companies ko sizes sets ke clear choices milte the (S, M, L levels).

### ➖ Disadvantages (Nuksan)
* **Massive IP Address Wastage:** Sabse badi failure. Agar kisi agency ko 300 hosts connect karne hon, toh Class C ($254$ hosts) thoda padega, isliye unhe Class B ($65,534$ hosts allocation) diya jata tha, jisse baki $65,200$ addresses seedhe waste ho jati thin.
* **Inflexible Structure:** Default mask structures strict hone ke karan address boundaries modify karna impossible tha, jise theek karne ke liye baad me classless routing (**CIDR**) aur **Subnetting** introduced ki gayi.

### 📊 Diagram
Ye layout Class A, B, aur C addresses ke Network ID vs Host ID bytes division mapping pattern ko show karta hai:

```
[ CLASS A ]  | Network ID (8 bits) |              Host ID (24 bits)               |
             |---------------------|----------------------------------------------|
             | First octet: 1-126  | Default Mask: 255.0.0.0 (/8)                 |

[ CLASS B ]  |      Network ID (16 bits)     |             Host ID (16 bits)        |
             |-------------------------------|--------------------------------------|
             | First octet: 128-191          | Default Mask: 255.255.0.0 (/16)      |

[ CLASS C ]  |             Network ID (24 bits)               |  Host ID (8 bits) |
             |------------------------------------------------|-------------------|
             | First octet: 192-223                           | Def Mask: /24     |
```

### 💡 Real-world Example (Udaharan)
* **Garment Size Chart Metaphor:**
  - Maan lijiye market me standard clothes options sirf standard sizes me milte hain: **Class A = XXL** (bina loose option ke), **Class B = L**, aur **Class C = S**.
  - Agar aapke family member ka size S se thoda bada hai, toh aapko force karke L size (Class B) buy karna padega. Jisse cloth kafi loose (IP wastage) rahega. Custom stitching (Subnetting/CIDR) ka option tab tak available nahi tha.
* **Country Postal Codes:** Class A is like a massive metropolis (Delhi) where millions of houses (Hosts) exist under one main code region. Class B is like a district area, and Class C is like a small street segment where only 250 houses are active.

### 🚀 Application (Kahan use hota hai?)
* **Loopback Diagnosis:** Class A range `127.0.0.1` checking local software processes.
* **IP Multicasting Streams:** Class D ranges (like `224.0.0.1` routing multimedia packets in routers clusters).
* **Private IP blocks reservation:** Class A (`10.0.0.0/8`), Class B (`172.16.0.0/12`), and Class C (`192.168.0.0/16`) reserved for internal local setups.

---