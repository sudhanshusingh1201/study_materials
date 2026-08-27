---
title: "Day 50 - Dynamic ARP Inspection"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🔒 Day 50: Dynamic ARP Inspection (DAI)

Welcome to the notes for **Day 50: Dynamic ARP Inspection (DAI)** of Jeremy's IT Lab CCNA Complete Course! Aaj hum switches par ARP-based spoofing aur poisoning attacks ko neutralize karne ke standard dynamic feature—**Dynamic ARP Inspection (DAI)**—ke baare mein seekhenge. Hum seekhenge ki ARP Poisoning (MitM) kaise kaam karti hai, DAI kaise **DHCP Snooping Binding Table** ka use karke entries ko validate karta hai, Trusted vs Untrusted ports setup kaise configure hota hai, rate-limiting lagane ke commands, aur optional check validations ko CLI commands ke sath detail mein cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. The Threat: ARP Poisoning (Spoofing)

Address Resolution Protocol (ARP) by default stateless aur unauthenticated hai. Devices bina verify kiye local ARP broadcasts aur replies ko accept karke apni temporary ARP Cache (RAM) local map table mein save kar leti hain:

*   **Gratuitous ARP (GARP):**
    *   Jab ek host up hota hai, toh woh segment par ek unsolicited (bina maange) ARP Reply broadcast bhejta hai: "Mera IP `192.168.1.10` hai aur mera MAC `MAC-A` hai." Devices is data se dynamic cache updates save kar leti hain.
*   **ARP Poisoning Attack (Man-in-the-Middle):**
    *   Attacker target client PC aur default gateway router ko fake (spoofed) unsolicited ARP replies bhejta hai:
        *   *To Client:* "IP `192.168.1.1` (Gateway) ab `MAC-Attacker` par hai."
        *   *To Router:* "IP `192.168.1.10` (Client) ab `MAC-Attacker` par hai."
    *   Dono targets apni local ARP cache overwrite kar lete hain. Ab client aur router ke beech hone wala saara traffic direct router par jaane ke bajaye **attacker ke laptop se bypass** hokar travel karta hai.

---

## 🏛️ 2. What is Dynamic ARP Inspection (DAI)?

**Dynamic ARP Inspection (DAI)** ek Layer 2 security feature hai jo switch ports par aane wale **saare ARP packets (Requests & Replies) ko intercept aur validate** karta hai.

### How DAI Validates Packets:
1.  **Database Lookup:** Jab switch ke untrusted port par koi ARP packet aata hai, toh switch us packet ke *Sender MAC* aur *Sender IP* parameters ko read karta hai.
2.  **DHCP Snooping Integration:** Switch in parameters ko **DHCP Snooping Binding Table** ke database entries se match (verify) karta hai.
    *   *If Match = Success:* ARP packet authentic hai, aur switch use normal forward kar deta hai.
    *   *If Match = Mismatch / No Entry:* packet fake hai, switch use **instantly drop** kar deta hai aur log error event trigger karta hai.
3.  **For Static IP Hosts:** Agar network par servers static IPs use kar rahe hain (jo DHCP database mein nahi honge), toh admin custom **ARP Access Control Lists (ACLs)** configure karke static mappings permit karwa sakta hai.

---

## 🧭 3. Trusted vs. Untrusted Ports in DAI

DHCP Snooping ki tarah, DAI ports ko do modes mein divide karta hai:

```text
                  +----------------------------------------------+
   LAN CLIENTS ---| [Untrusted Ports]  DAI  [Trusted interface] |--- GATEWAY ROUTER
  (Inspected by   | (ARP checked      (Switch) (Inspection     |   (No ARP check)
   Binding Table) |  against Snooping)          bypassed)        |
                  +----------------------------------------------+
```

*   **Trusted Ports:**
    *   Backbone links, router facing ports ya switches uplinks.
    *   *Rule:* DAI in ports par dynamic interface analysis run nahi karta (inspections are bypassed).
*   **Untrusted Ports:**
    *   Normal user end client terminals ports.
    *   *Rule:* Saare incoming ARP packets strictly inspect kiye jate hain.

---

## 💻 4. Cisco IOS CLI Configurations

Switch `Switch-Core` par VLAN 10 ke liye DAI active karna, router interface Gi0/1 ko trust parameters par map karna, aur rate limits configure karna:

### Step-by-Step Configuration:
```ios
! Prerequisite: DHCP Snooping must be globally active and populated
Switch-Core(config)# ip dhcp snooping
Switch-Core(config)# ip dhcp snooping vlan 10

! 1. Enable Dynamic ARP Inspection on VLAN 10 (Mandatory)
Switch-Core(config)# ip arp inspection vlan 10

! 2. Configure Router facing port Gi0/1 as TRUSTED (DAI bypasses it)
Switch-Core(config)# interface gigabitethernet 0/1
Switch-Core(config-if)# ip arp inspection trust

! 3. Configure client ports (Gi0/2 to 24) with Rate-Limiting
! (Default is 15 pps. Starvation and DoS tools block link ports if exceeded)
Switch-Core(config)# interface range gigabitethernet 0/2 - 24
Switch-Core(config-if-range)# ip arp inspection limit rate 20    ! Limit to 20 ARP packets per second
```

---

### B. Advanced Validation Checks:
Extra security layer apply karne ke liye switch packets headers ke structural checks perform kar sakta hai:

```ios
! Check 1: Ethernet Source MAC matches ARP Sender MAC in payload
Switch-Core(config)# ip arp inspection validate src-mac

! Check 2: Ethernet Destination MAC matches ARP Target MAC in payload
Switch-Core(config)# ip arp inspection validate dst-mac

! Check 3: Validates IP addresses in ARP body (Blocks invalid/multicast IPs)
Switch-Core(config)# ip arp inspection validate ip
```

---

## 🔍 5. Verification Commands

*   **VLAN configurations parameters check, statistics counters aur dropped packet status verify karne ki command:**
    ```ios
    Switch-Core# show ip arp inspection
    ```
    *Output snippet:*
    ```text
    Source Mac Validation      : Disabled
    Destination Mac Validation : Disabled
    IP Address Validation      : Disabled

     Vlan     Configuration    Operation
     ----     -------------    ---------
       10     Enabled          Active

     Vlan     Logged Packets   Dropped Packets
     ----     --------------   ---------------
       10                105               24                     ! 24 spoofed ARP packets dropped!
    ```
*   **Switches ports trust status aur configured rate limits settings parameters brief table check karne ki command:**
    ```ios
    Switch-Core# show ip arp inspection interfaces
    ```
    *Output snippet:*
    ```text
    Interface        Trust State     Rate (pps)    Burst Interval
    ---------------  -----------     ----------    --------------
    Gi0/1            Trusted                 None                1
    Gi0/2            Untrusted                 20                1
    ```

---

## 📝 6. CCNA Day 50 Practice Questions

1. **Q1: Dynamic ARP Inspection (DAI) spoofed ARP entries verify aur drop karne ke liye primary kis system database table lookup par rely karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **DHCP Snooping Binding Table** (Dynamic MAC to IP relationship mappings database).
   </details>

2. **Q2: DHCP Snooping switch port trust options ki tarah, DAI globally enabled hone par switches dynamic interface check par default state ports kya hold karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Saare switch interfaces by default **Untrusted** status hold karte hain (strict packet verification active on all ports).
   </details>

3. **Q3: Attacker dwara target systems (client and gateway) par unsolicited fake ARP updates bejh kar host caches pollute karne ke dynamic process attack ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **ARP Poisoning** (or ARP Spoofing).
   </details>

4. **Q4: Host device line network link up hote hi local segments updates aur dynamic duplicate IP checks run karne ke liye kis protocol packets use karti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Gratuitous ARP (GARP)**.
   </details>

5. **Q5: Cisco switches globally level par VLAN 15 scope ke andruni network ports par DAI service active karne ki commands configurations line kya hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global configuration command: **`ip arp inspection vlan 15`**.
   </details>

6. **Q6: Switch port security parameters set setup line interface GigabitEthernet 0/1 ko trusted define karne ki DAI config CLI configuration commands kya specify karegi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Interface mode command: **`ip arp inspection trust`**.
   </details>

7. **Q7: Client hosts untrusted interfaces par packet queries limits overflow (DoS/DDoS) prevent dynamic speed thresholds set limit rate set karne ki interface configuration command line syntax kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Interface mode command: **`ip arp inspection limit rate <packets-per-second>`** (e.g. `ip arp inspection limit rate 20`).
   </details>

8. **Q8: DAI extra validation checks ke configuration mein `src-mac` checking mode parameters verify target checks apply setup options syntax line command kya hold karti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global command: **`ip arp inspection validate src-mac`** (Checks if Ethernet source MAC matches Sender MAC inside ARP packet).
   </details>

9. **Q9: Connected interfaces levels trust state values (Trusted/Untrusted) aur active ARP packets rate settings display status check trace verify command name kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Privileged EXEC verification command: **`show ip arp inspection interfaces`**.
   </details>

10. **Q10: OSPF validation indicators checks statistics, active check options enabled status aur dynamic dropped frame counters tables verify command kya details return karegi?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** Privileged EXEC command: **`show ip arp inspection`**.
    </details>
