---
title: "Day 39 - SNMP"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🌐 Day 39: Simple Network Management Protocol (SNMP)

Welcome to the notes for **Day 39: Simple Network Management Protocol (SNMP)** of Jeremy's IT Lab CCNA Complete Course! Aaj hum **Module 5: Security & Network Management** ko start kar rahe hain. Is lecture note mein hum seekhenge ki kaise SNMP centrally pure network devices ko monitor aur manage karta hai. Hum SNMP core components, message mechanisms (Get, Set, Trap, Inform), SNMP versions (v1, v2c, aur highly secure v3), Cisco CLI configurations (both v2c & v3), and verification commands ko step-by-step detailed explanations aur premium illustrations ke sath cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. What is SNMP? (Simple Network Management Protocol)

**Simple Network Management Protocol (SNMP)** ek Application Layer protocol hai jo network administrators ko centralized location se switches, routers, servers, printers, aur firewalls ko monitor aur configure karne ki capability provide karta hai.

### Core SNMP Components:
1.  **Network Management Station (NMS):**
    *   Central server ya computer jo monitoring application (e.g. Cisco Prime, PRTG, SolarWinds) run karta hai. Ye Agent devices se data query (pull) aur notifications receive karta hai.
2.  **Managed Device:**
    *   Network hardware (Router, Switch, Firewall) jo SNMP monitoring parameters execute karta hai.
3.  **SNMP Agent:**
    *   Managed device par run hone wala ek dynamic software daemon. Ye MIB variables ko track karta hai aur NMS queries ka response deta hai.
4.  **Management Information Base (MIB):**
    *   Managed device ke features aur parameters ki ek organized, hierarchical text database. Is database ke metrics ko **Object Identifiers (OIDs)** numbers range se locate kiya jata hai (e.g. CPU utilization, Interface status).

---

## 🏛️ 2. SNMP Messages & Ports

NTP aur DHCP ki tarah, SNMP operational communications ke liye specific **UDP Ports** use karta hai:

*   **UDP Port `161`:** NMS to Agent communications (Queries / Pull traffic) ke liye.
*   **UDP Port `162`:** Agent to NMS communications (Traps / Alerts push traffic) ke liye.

![SNMP Monitoring Concept](../images/snmp_monitoring_concept.jpg)

### SNMP Message Types:
1.  **GET Request (Pull):** NMS agent se specific OID value request karta hai (e.g., "Interface Gi0/1 ka status kya hai?").
2.  **GET NEXT Request:** MIB hierarchy mein current OID ke next entry ki value query karne ke liye.
3.  **SET Request (Push/Write):** NMS agent interface par configurations change karne ke liye command bhejta hai (e.g., shutdown an interface dynamically).
4.  **RESPONSE:** Agent NMS ko GET or SET query ke status ka answer send karta hai.
5.  **TRAP (Alert - Unsolicited):**
    *   Agent dynamically kisi emergency event (link down, high CPU) hone par NMS ko directly alert data push karta hai.
    *   *Note:* **TRAP messages unreliable hote hain** kyunki NMS receive hone par koi receipt confirmation (acknowledgment) send nahi karta.
6.  **INFORM (Alert - Acknowledged):**
    *   Agent to NMS notification message (similar to Trap) lekin **INFORM reliable hai**. Jab NMS INFORM receive karta hai, toh return ACK packet bhejta hai. Agar agent ko ACK na mile, toh woh alarm repeat send karta hai.

---

## 🛡️ 3. SNMP Versions Comparison (v1, v2c, v3)

Time ke sath security enhancements ke basis par SNMP ko teen versions mein release kiya gaya hai:

### A. SNMPv1:
*   **Security:** Very weak. System cleartext **Community Strings** (password) use karta hai jise protocol analyzer (Wireshark) se easily trace kiya ja sakta hai.
*   **Mechanism:** UDP base model. Inform messaging support nahi karta.

### B. SNMPv2c:
*   **Security:** V1 ki tarah cleartext Community Strings use karta hai.
*   **Enhancements:** Adds bulk get requests (multi-data query) and **INFORM** messages.

### C. SNMPv3 (Current Secure Standard):
SNMPv3 modern enterprises par strong security options add karta hai jiske liye teen primary levels define kiye gaye hain:

*   **noAuthNoPriv (No Authentication, No Privacy):** Username matching check hoti hai, par na packet hash authenticate kiya jata hai aur na encryption. (Equivalent to community string).
*   **authNoPriv (Authentication, No Privacy):** Authentication check parameters (using MD5/SHA hashes) configure hote hain, par data transmission plain text rehta hai.
*   **authPriv (Authentication, Privacy):** Authentication checks MD5/SHA se verified hote hain aur payload contents (Privacy) fully **AES / DES** algorithms se encrypted hoti hain.

---

## 💻 4. Cisco IOS CLI Configurations

### A. SNMPv2c Configuration (Community Strings):
Cisco switches par basic SNMPv2c service setup karne ke steps:

```ios
! 1. Read-Only community configure karein (NMS only data gather kar payega)
Router-A(config)# snmp-server community CISCO_RO RO

! 2. Read-Write community configure karein (NMS settings edit kar payega - Use carefully)
Router-A(config)# snmp-server community CISCO_RW RW

! 3. Configure NMS Target host IP for receiving Alerts (Traps/Informs)
Router-A(config)# snmp-server host 10.1.1.100 version 2c CISCO_RO

! 4. Enable Traps on Router
Router-A(config)# snmp-server enable traps
```

---

### B. SNMPv3 Secure Configuration (authPriv Level):
SNMPv3 security parameters define karne ke liye views, groups, aur users parameters map karne padte hain:

```ios
! 1. View create karein (MIB tree ka complete access permit karein)
Router-A(config)# snmp-server view ALL_ACCESS iso include

! 2. Group create karein (Security Model: v3, authPriv level, associate with View)
Router-A(config)# snmp-server group V3_SECURE_GRP v3 priv read ALL_ACCESS write ALL_ACCESS

! 3. User configure karein (Link User with Group, set SHA for Auth, AES 128 for Encryption)
Router-A(config)# snmp-server user ADMIN_USER V3_SECURE_GRP v3 auth sha AUTH_PASSWORD123 priv aes 128 ENCRYPT_PASS456
```

---

## 🔍 5. Verification Commands

*   **Router par active SNMP packets statistics, configuration details aur active community list check karne ke liye:**
    ```ios
    Router-A# show snmp
    ```
*   **Configured SNMP Users details check karne ke liye:**
    ```ios
    Router-A# show snmp user
    ```
*   **Active groups parameters verify karne ke liye:**
    ```ios
    Router-A# show snmp group
    ```

---

## 📝 6. CCNA Day 39 Practice Questions

1. **Q1: SNMP (Simple Network Management Protocol) database design structure hierarchy aur objects tracking system ko kya kehte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **MIB (Management Information Base)**, aur iske variables ko track karne wale paths code range numerical parameters ko **OIDs (Object Identifiers)** kehte hain.
   </details>

2. **Q2: SNMP communication ports details ke mutabik, NMS Queries (pull) aur Agent alerts/notifications (push) kin UDP port numbers par operate karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Pull queries on **UDP Port `161`** aur Push notifications/alerts on **UDP Port `162`**.
   </details>

3. **Q3: SNMP Agent to NMS send hone wale dynamic Alert messaging system mein 'Trap' aur 'Inform' messages ke beech core functional difference kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **TRAP** alerts completely unreliable hote hain (unacknowledged push), jabki **INFORM** alerts highly reliable hote hain kyunki unhe NMS se receipt confirmation (acknowledgment ACK) receive hona mandatory hota hai.
   </details>

4. **Q4: SNMP versions checks mein, bulk requests support add karne aur inform alarms feature introduce karne wala version kaun sa tha?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **SNMPv2c**.
   </details>

5. **Q5: SNMPv1 aur v2c versions corporate networks par highly vulnerable aur unsafe kyu mane jate hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Kyunki ye client authentication ke liye cleartext parameters **Community Strings** exchange karte hain, jisse Wireshark packet capture se passwords chori ho sakte hain.
   </details>

6. **Q6: SNMPv3 security levels range parameters checks ke dynamic framework mein 'authPriv' model kya attributes support karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Authentication** checks MD5/SHA protocols hashes verification ke sath hotey hain aur **Privacy (Payload Encryption)** secure AES or DES algorithms encryption setup support karti hai (Highly secure).
   </details>

7. **Q7: Router configurations check mein, read-only SNMP community strings create karne ki CLI configuration syntax kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global command: **`snmp-server community <string-name> RO`**.
   </details>

8. **Q8: Cisco device par local interfaces down parameters alerts automatic NMS host `10.10.10.5` ko redirect config set karne ki target hosts command kya setup hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Global command: **`snmp-server host 10.10.10.5 version 2c <community-string>`**.
   </details>

9. **Q9: SNMPv3 parameters setup lines par, MD5/SHA logins configuration credentials aur keys definitions verification profiles verify karne ke liye console commands indicators kya define hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Verification command: **`show snmp user`**.
   </details>

10. **Q10: OSPF parameters की tarah SNMP services enabled statistics parameters check karne ki primary verification control command kya output return karti hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **`show snmp`** command.
    </details>
