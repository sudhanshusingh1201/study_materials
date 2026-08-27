---
title: "Day 44 - NAT - Part 2"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🌐 Day 44: Network Address Translation (NAT) - Part 2 (Dynamic NAT & PAT)

Welcome to the notes for **Day 44: NAT - Part 2** of Jeremy's IT Lab CCNA Complete Course! Aaj hum Network Address Translation (NAT) ke advanced mechanisms—**Dynamic NAT** aur **PAT (Port Address Translation / NAT Overload)**—ke baare mein seekhenge. Hum seekhenge ki kaise PAT ek single public IP address par hazaron local users ko internet access allow karta hai using Layer 4 port numbers. Iske sath hi hum dynamic pool definitions, interface overload configurations, and verification tables ko step-by-step detailed explanations aur premium illustrations ke sath cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. Dynamic NAT (Concepts & Limitations)

Static NAT (Day 43) manual 1-to-1 mappings use karta tha, jo flexible nahi hai.

**Dynamic NAT** automatically Inside Local IPs ko public IPs ke ek pre-defined pool se maps karta hai (first-come, first-served basis par):
*   **Mechanism:** Jab koi internal client internet access attempt karta hai, router pool se ek free public IP dynamically use karta hai aur transition entry save karta hai.
*   **Limitation:** Dynamic NAT bhi **1-to-1 mapping** par hi kaam karta hai (1 client active session = 1 public IP from pool). Agar pool mein total 5 public IPs hain, toh sirf pehle 5 clients hi internet access kar payenge. 6th user ko access block ho jayega (`translation miss`). Isliye Dynamic NAT actual public IP addresses ko conserve (save) nahi karta.

---

## 🏛️ 2. PAT (Port Address Translation / NAT Overload)

**Port Address Translation (PAT)**, jise Cisco IOS mein **NAT Overload** bhi kehte hain, actual address conservation standard hai jo aaj pure world ke home networks aur corporate enterprises mein use kiya jata hai.

*   **Many-to-One / Many-to-Few Mapping:** Dynamic local network hosts (e.g. `192.168.1.0/24`) aapas mein **ek hi public IP address** share karte hain.
*   **How PAT Works (Port Tracking):**
    *   Router translation ke waqt sirf IP address change nahi karta, balki client ke outgoing packet ka **Layer 4 Source Port Number** check aur modify karta hai.
    *   Router har user session ke liye unique source port block bind kar leta hai. Jab internet target response bhejta hai, toh destination port ko analyze karke router identify karta hai ki packet kis local PC ka hai.

![PAT NAT Overload Port Mapping](../images/pat_nat_overload.jpg)

*   **Capacity:** Ek single IPv6/IPv4 address theoretically $2^{16} = 65,536$ concurrent sessions support kar sakta hai (using ports range `1024 - 65535`).

---

## 💻 3. Cisco IOS CLI Configurations

### A. Dynamic NAT Configuration:

```ios
! Step 1: LAN/WAN interfaces classify karein (Jaise Static NAT mein kiya tha)
Router-A(config)# interface gigabitethernet 0/0
Router-A(config-if)# ip nat inside
Router-A(config)# interface gigabitethernet 0/1
Router-A(config-if)# ip nat outside
Router-A(config)# exit

! Step 2: Access List (ACL) create karein to match allowed LAN IP ranges
Router-A(config)# access-list 1 permit 192.168.1.0 0.0.0.255

! Step 3: Define Public IP Pool
! Syntax: ip nat pool <name> <start-public-IP> <end-public-IP> netmask <subnet-mask>
Router-A(config)# ip nat pool PUBLIC_POOL 203.0.113.10 203.0.113.15 netmask 255.255.255.248

! Step 4: Link ACL and Pool
! Syntax: ip nat inside source list <acl> pool <pool-name>
Router-A(config)# ip nat inside source list 1 pool PUBLIC_POOL
```

---

### B. PAT / NAT Overload Configurations:

Real-world deployments par PAT ko do tarike se configure kiya ja sakta hai:

#### Option A: Overload using an IP Pool (Multi-IP sharing):
Agar aapke paas small range of public IPs hai aur aap un sabhi par overloading lagana chahte hain:
```ios
! Pool configuration ke same commands chalayein, aur linking ke end mein 'overload' keyword add karein:
Router-A(config)# ip nat inside source list 1 pool PUBLIC_POOL overload
```

#### Option B: Overload using exit Interface (Single IP sharing - Most Common):
Home routers ya small branches par jahan hume router ke WAN port interface dynamic IP address (assigned by ISP) par hi saara LAN traffic overload karna ho:
```ios
! Syntax: ip nat inside source list <acl> interface <WAN-port> overload
Router-A(config)# ip nat inside source list 1 interface gigabitethernet 0/1 overload
```

---

## 🔍 4. Verification & Troubleshooting Commands

### A. View PAT Session details:
```ios
Router-A# show ip nat translations
```
*Output snippet:*
```text
Pro Inside local       Inside global        Outside local      Outside global
tcp 192.168.1.10:1024  203.0.113.5:50001    8.8.8.8:80         8.8.8.8:80
tcp 192.168.1.20:2150  203.0.113.5:50002    8.8.8.8:443        8.8.8.8:443
```
> [!NOTE]
> Output parameters confirm karte hain ki dono clients (`192.168.1.10` aur `192.168.1.20`) ko **exact same public Inside Global IP `203.0.113.5`** mila hai. Router local ports `:1024` aur `:2150` ko unique global ports `:50001` aur `:50002` ke dynamic values par differentiate kar raha hai.

---

### B. View NAT Statistics:
```ios
Router-A# show ip nat statistics
```
*Output checks details like misses, dynamic pool allocations, interfaces, and overload parameters status.*

---

## 📝 5. CCNA Day 44 Practice Questions

1. **Q1: Dynamic NAT systems aur PAT (NAT Overload) ke beech main database mapping differences kya hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Dynamic NAT temporary first-come-first-serve basis par **1-to-1 IP mapping** (1 private IP to 1 public IP) karta hai, jabki PAT/NAT Overload **Many-to-One IP mapping** (multiple private IPs to 1 single public IP using Layer 4 ports) karta hai.
   </details>

2. **Q2: PAT (Port Address Translation) dynamic translations differentiate karne ke liye header ke kis criteria ko map/modify karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Layer 4 Source Port Numbers** (TCP/UDP source ports) ko.
   </details>

3. **Q3: Dynamic NAT pool configurations run karte waqt, agar pool ke saare public IP addresses active hosts ko assign ho chuke hon, toh 6th user access check par kya output parameter generate hoga?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Router par **NAT Translation Miss** count alert setup hoga aur us user ka internet traffic block (drop) ho jayega.
   </details>

4. **Q4: Theory parameters ke according, ek single public IP address par concurrently maximum kitne dynamic ports sessions support kiye ja sakte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Up to **`65,536`** sessions (typically range `1024 - 65535` usable ports).
   </details>

5. **Q5: Dynamic NAT pool configure karne ki router CLI parameters command options kya scale specify karegi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global command: **`ip nat pool <pool-name> <start-IP> <end-IP> netmask <subnet-mask>`**.
   </details>

6. **Q6: Access List 10 target match local LAN devices ko interface GigabitEthernet 0/1 public address par overload dynamic configure karne ki exact command syntax kya hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global configuration command: **`ip nat inside source list 10 interface gigabitethernet 0/1 overload`**.
   </details>

7. **Q7: Dynamic NAT configs links par access list aur IP pool mapping process execute karne ke liye command configure variables order structure kya hoga?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global command: **`ip nat inside source list <ACL-num> pool <pool-name>`**.
   </details>

8. **Q8: Active PAT session dynamic ports mappings table, inside local target ports aur mapped inside global translation entries verify karne ki verification command kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Privileged EXEC command: **`show ip nat translations`**.
   </details>

9. **Q9: NAT parameters checks par translation counters parameters, dynamic mapping statistics aur active inside/outside interface status verification target options query command kya use hoti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Privileged EXEC command: **`show ip nat statistics`**.
   </details>

10. **Q10: Dynamic NAT/PAT tables troubleshooting run ke dauran, dynamic translation session buffers reset/flush karne ki privilege command kya hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`clear ip nat translation *`** command.
    </details>
