---
title: "Day 43 - NAT - Part 1"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🌐 Day 43: Network Address Translation (NAT) - Part 1 (Static NAT)

Welcome to the notes for **Day 43: NAT - Part 1** of Jeremy's IT Lab CCNA Complete Course! Aaj hum CCNA routing and scaling ka ek sabse critical concept start kar rahe hain—**Network Address Translation (NAT)**. Is lecture note mein hum seekhenge ki NAT kya hota hai, private versus public IPv4 address spaces kya hain, NAT ke key terms (Inside Local, Inside Global, Outside Local, Outside Global) kya significance rakhte hain, aur Cisco IOS par **Static NAT (1-to-1 translation)** kaise configure aur verify kiya jata hai. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. Why do we need NAT?

IPv4 addresses 32-bit parameters (`4.29 Billion` total addresses) par limited hain. Internet ke early growth stage par hi clear ho gaya tha ki public IPs jaldi hi exhaust (khatam) ho jayenge.

Is issue ko temporarily solve karne ke liye **RFC 1918** rules banaye gaye:
*   **Private IP Addresses:** Har local network/home/office ke hosts ke liye reserve IPs jo public internet par direct route nahi ho sakte.
*   **Public IP Addresses:** Internet Service Providers (ISPs) ke through purchase hone wale unique addresses jo internet backbone par globally routable hote hain.

### RFC 1918 Private IPv4 Ranges (CCNA Core Memorization):
*   **Class A:** `10.0.0.0` to `10.255.255.255` (`10.0.0.0/8`)
*   **Class B:** `172.16.0.0` to `172.31.255.255` (`172.16.0.0/12`)
*   **Class C:** `192.168.0.0` to `192.168.255.255` (`192.168.0.0/16`)

> **The NAT Function:** Jab local client (e.g. `192.168.1.10`) public Internet par connect hona chahta hai, toh router boundaries par client ke private IP ko public IP address mein translate kar deta hai. Is system ko hum NAT kehte hain.

---

## 🏛️ 2. Critical NAT Terminology

Cisco examinations aur troubleshooting mein niche diye gaye 4 terminology definitions par command hona zaroori hai:

```text
               +-------------------------------------------------+
               |                    ROUTER                       |
   LAN HOST ---| [Inside Interface]  NAT  [Outside Interface] |--- PUBLIC TARGET
  192.168.1.10 |                                                 |   8.8.8.8
               +-------------------------------------------------+
               |<------- INSIDE ------->|<------- OUTSIDE ------>|
```

*   **Inside Local (IL):**
    *   Hamare internal local LAN segment ke host ka actual **Private IP Address** (e.g. `192.168.1.10`).
*   **Inside Global (IG):**
    *   Translation process ke baad, hamare inside host ka jo **Public IP Address** internet space par visible hota hai (e.g. `203.0.113.5`).
*   **Outside Local (OL):**
    *   Outside target device (internet server) ka IP address jaisa hamare inside LAN segment ko visible hota hai. (Almost hamesha outside global IP ke identical/same hota hai, e.g. `8.8.8.8`).
*   **Outside Global (OG):**
    *   Target internet device ka actual registered **Public IP Address** (e.g. `8.8.8.8`).

---

## 🧭 3. Static NAT (One-to-One Translation)

**Static NAT** mein ek single Inside Local (Private IP) ko permanently ek specific Inside Global (Public IP) se map kiya jata hai.

*   **One-to-One Mapping:** `1 Private IP` $\leftrightarrow$ `1 Public IP`.
*   **Use Case:** Iska use main servers (e.g. Internal Web Server ya Mail Server) ke liye kiya jata hai jisse internet par active outsiders directly access kar sakein.

![Static NAT Translation Flow](../images/static_nat_translation.jpg)

---

## 💻 4. Cisco IOS CLI Configurations

Static NAT configure karne ke liye aapko interfaces specify karne parte hain aur mapping line add karni parti hai:

### Step 1: Classify Interfaces (Inside vs Outside):
Router ko batana mandatory hai ki kaun sa interface LAN se connected hai aur kaun sa Internet (WAN) se:
```ios
Router-A(config)# interface gigabitethernet 0/0
Router-A(config-if)# ip nat inside                                ! LAN facing port

Router-A(config)# interface gigabitethernet 0/1
Router-A(config-if)# ip nat outside                               ! WAN/Internet facing port
```

### Step 2: Define Static NAT Mapping:
Hum Web server `192.168.1.10` ko public IP `203.0.113.5` par translate karenge:
```ios
! Command syntax: ip nat inside source static <local-IP> <global-IP>
Router-A(config)# ip nat inside source static 192.168.1.10 203.0.113.5
```

---

## 🔍 5. Verification & Troubleshooting Commands

### A. View Active Translation Table:
```ios
Router-A# show ip nat translations
```
*Output snippet:*
```text
Pro Inside local      Inside global       Outside local      Outside global
--- 192.168.1.10      203.0.113.5         ---                ---
tcp 192.168.1.10:80   203.0.113.5:80      8.8.8.8:53022      8.8.8.8:53022
```
*Note: First line baseline static entry show karti hai jiska koi timeout limits nahi hota (always persistent in RAM). Second line active port translation sessions flow details represent karti hai.*

---

### B. View NAT Statistics:
```ios
Router-A# show ip nat statistics
```
*Output snippet:*
```text
Total active translations: 1 (1 static, 0 dynamic; 0 extended)
Peak translations: 15, occurred 01:24:10 ago
Outside interfaces:
  GigabitEthernet0/1
Inside interfaces:
  GigabitEthernet0/0
Hits: 1245  Misses: 0
Expired translations: 12
Dynamic mappings:
```

---

### C. Clear dynamic table (Troubleshooting):
```ios
Router-A# clear ip nat translation *                              ! Removes dynamic NAT translations (Static mappings remain unchanged)
```

---

## 📝 6. CCNA Day 43 Practice Questions

1. **Q1: NAT (Network Address Translation) technology introduce karne ka primary core driver reason kya tha?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Public IPv4 address space ke rapid exhaustion (khatam hone) ko prevent karna aur address preservation scale ko maintain rakhna.
   </details>

2. **Q2: RFC 1918 Class B private address space ranges limits kya define ki gayi hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`172.16.0.0`** to **`172.31.255.255`** (`172.16.0.0/12`).
   </details>

3. **Q3: NAT terminology ke mutabik, inside host ke actual private IP address ko kya kehte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Inside Local (IL)**.
   </details>

4. **Q4: Packet router boundary cross karke WAN side jane ke baad, inside source IP address kis term se transform/represent hota hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Inside Global (IG)** (Inside host ka registered public IP).
   </details>

5. **Q5: External target destination (jaise public web server `8.8.8.8`) ke actual public address registration variables ko kya define kiya jata hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Outside Global (OG)**.
   </details>

6. **Q6: Static NAT configuration rules ke andruni parameters checks kis type of IP address mapping structures mapping perform karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **One-to-One mapping** (1 Private IP dynamically maps to exactly 1 Public IP).
   </details>

7. **Q7: Router LAN facing interface FastEthernet 0/1 ko NAT ingress point set karne ki configuration command kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Interface mode command: **`ip nat inside`**.
   </details>

8. **Q8: Local Server IP `10.1.1.5` ko public static IP `198.51.100.1` par map karne ki correct Cisco global command write kya hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global configuration command: **`ip nat inside source static 10.1.1.5 198.51.100.1`**.
   </details>

9. **Q9: Active NAT translation table entries check aur mappings database verify karne ki standard privileged EXEC verify command name kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Privileged EXEC command: **`show ip nat translations`**.
   </details>

10. **Q10: Dynamic NAT entries clear karne ke liye run hone wali standard administrative command kya verify statistics return karegi?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`clear ip nat translation *`** (Static mappings delete nahi honge, dynamic mapping clear statistics reset ho jayenge).
    </details>
