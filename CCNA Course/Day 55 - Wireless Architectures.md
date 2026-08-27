---
title: "Day 55 - Wireless Architectures"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 📶 Day 55: Wireless Architectures (AP Modes and WLC Deployments)

Welcome to the notes for **Day 55: Wireless Architectures** of Jeremy's IT Lab CCNA Complete Course! Aaj hum seekhenge ki enterprise wireless networks ko design aur manage karne ke liye kaun se physical aur logical architectures use kiye jate hain. Hum Autonomous APs, Lightweight APs (LAPs), **Wireless LAN Controller (WLC)**, **CAPWAP Tunnels** (Control vs Data ports), aur WLC deployments (Centralized, Embedded, Cloud-Based) ko detailed steps, structural comparisons, aur diagrams ke sath cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. Standalone vs. Centralized AP Architectures

WLAN networks ko design aur scale karne ke teen primary methods hain:

### A. Autonomous AP Architecture (Standalone):
*   **Concept:** Har Access Point (AP) ek completely standalone intelligent unit hota hai.
*   **Operations:** AP khud wireless authentication, encryption, channel tuning, aur VLAN mappings ko independent parameters par manage karta hai.
*   **Scale Problem:** Agar office mein 50 APs hain, aur hume SSID password change karna hai, toh admin ko manually **saare 50 APs par alag-alag login karke configuration write** karni padegi. Isliye ye model dynamic enterprise growth par scale nahi ho sakta.

---

### B. Cloud-Managed AP Architecture (Cisco Meraki):
*   **Concept:** APs physically office branches mein deployed hote hain par unki configurations aur management **centralized Cloud Dashboard** se hoti hai.
*   **Split Plane:**
    *   *Control Plane (Management):* Cloud platform se AP firmware update aur config templates push hoti hain.
    *   *Data Plane (User Traffic):* User data traffic local branch switch se directly route hota hai (wo cloud par nahi jata).

---

### C. WLC (Wireless LAN Controller) / Split-MAC Architecture:
*   **Concept:** Enterprise network ke saare Access Points ko hum dumb (lightweight) device bana dete hain aur unka central brain ek hardware server box (**WLC**) ko bana dete hain.
*   **Split-MAC Division:**
    *   **Lightweight AP (LAP):** Sirf basic Layer 1/2 real-time processes handle karta hai (jaise beacon frames generate karna, wireless encryption handshakes, aur frame transmit/receive).
    *   **WLC (Controller):** Management features handle karta hai (jaise dynamic channel assignment, AP transmit power tuning via RRM, client authentication, security policy checks, and roam coordination).

---

## 🏛️ 2. CAPWAP Tunneling Protocol

Split-MAC design mein, LAPs aur WLC aapas mein communicate karne ke liye **CAPWAP (Control and Provisioning of Wireless Access Points)** protocol tunneling use karte hain. 

```text
  +----------------------+                           +-------------------+
  | Lightweight AP (LAP) | ======== CAPWAP ========= | Wireless LAN (WLC)|
  | (L2 radio actions)   |                           | (Management Brain)|
  +----------------------+                           +-------------------+
                               Tunnels:
                               1. CAPWAP Control (UDP 5246) -> Encrypted
                               2. CAPWAP Data    (UDP 5247) -> Encapsulated
```

CAPWAP standard do logical tunnels build karta hai between LAP and WLC:
1.  **CAPWAP Control Tunnel (UDP Port 5246):**
    *   *Traffic:* Management traffic (configuration updates, power adjustments, firmware pushes).
    *   *Security:* DTLS (Datagram Transport Layer Security) protocol se **fully encrypted** hoti hai.
2.  **CAPWAP Data Tunnel (UDP Port 5247):**
    *   *Traffic:* Clients ka standard user data traffic (web request, email frames).
    *   *Encryption:* By default **unencrypted** hoti hai (unless manual IPsec setup is done).
    *   *How it Works:* Client ka traffic AP par aate hi CAPWAP header se encapsulate hokar dynamic tunnel se direct WLC tak bypass route hota hai. WLC use de-capsulate karke local switch switchport trunk par inject kar deta hai.

---

## 🧭 3. WLC Deployment Models (CCNA Core)

Cisco networks par WLC deployment ke key models are:

1.  **Unified / Centralized Deployment:**
    *   *Setup:* WLC is placed in a central data center. Saare campus LAPs tunnel banakar central datacenter WLC tak aate hain.
    *   *Scale:* Highly scalable, easy centralized management. Heavy backbone overhead.
2.  **Embedded Deployment:**
    *   *Setup:* WLC software functions directly standard Layer 3 switch (jaise Cisco Catalyst 9300 series switches) ke internal processors par run hote hain.
    *   *Usage:* Small branch offices jahan alag se controller lagane ki cost nahi chahiye.
3.  **Mobility Express Deployment:**
    *   *Setup:* WLC software local lightweight APs mein se hi ek selective AP ke processor memory par dynamically host ho jata hai. Woh AP AP-and-Controller dono roles serve karta hai.
4.  **Cloud-Based Deployment:**
    *   *Setup:* Virtual machine (VM) target private ya public cloud cloud infrastructure par host hoti hai jo switches and APs remote locations se manage karti hai.

---

## 📝 4. CCNA Day 55 Practice Questions

1. **Q1: Autonomous Standalone APs aur Lightweight APs (LAPs) ke config management scaling mein primary difference kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Autonomous APs individually and manually configure karne padte hain (poor scaling), jabki Lightweight APs central brain **WLC (Wireless LAN Controller)** se automatically dynamic parameters aur updates receive karte hain (high scaling).
   </details>

2. **Q2: Cisco Meraki cloud architecture ke control plane aur data plane operations flow kahan locate hote hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Control plane (management/configs) Meraki Cloud Dashboard par aur Data plane (actual user data packets) local branch switches/routers network switches par local run hota hai.
   </details>

3. **Q3: Split-MAC design rules ke andruni parameters checks me, Lightweight Access Point (LAP) kis structural layers check responsibilities ko serve karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Real-time **Layer 1 and Layer 2 functions** (beacons, frame transmission, encryption keys application).
   </details>

4. **Q4: LAP aur WLC ke andruni communication channels create karne ke liye standard RFC network tunnel protocol name kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **CAPWAP (Control and Provisioning of Wireless Access Points)**.
   </details>

5. **Q5: CAPWAP Control messages transmission aur WLC parameter updates execute karne ke liye kis network port type aur standard protocol features ka use hota hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **UDP Port `5246`** (encrypted using **DTLS**).
   </details>

6. **Q6: Clients user data transport traffic tunnel route pass forward karne ke liye CAPWAP kis default port parameters values ko check map karta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **UDP Port `5247`** (unencrypted by default).
   </details>

7. **Q7: WLC central hardware deployment segment jahan saare branch LAPs tunnels converge datacenters switches par aggregate hote hain, use kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Unified / Centralized WLC Deployment**.
   </details>

8. **Q8: Cisco Catalyst core switches processors (Catalyst 9300 series) par active virtual controller features configurations model ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Embedded WLC Deployment**.
   </details>

9. **Q9: Standalone Lightweight APs blocks par WLC logic dynamically local active AP hardware par virtual control node set chalane ko kya kehte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Cisco Mobility Express** (Virtual WLC on AP).
   </details>

10. **Q10: LAP switches segments par dynamic radio frequency (RF) bands parameter channel tunings and transmit power scale check configure control automation standard tool ko kya bolte hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **RRM (Radio Resource Management)** jo WLC internally auto-calculate and adjust karta hai.
    </details>
