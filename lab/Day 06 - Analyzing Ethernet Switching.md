---
title: "Day 06 Lab - Analyzing Ethernet Switching"
tags:
  - ccna
  - networking
  - lab
  - packet-tracer
  - cisco
type: lab-worksheet
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🧪 Day 06 Lab: Analyzing Ethernet Switching

Welcome to the **Day 06 Lab: Analyzing Ethernet Switching** guide! Is lab module mein hum dynamically verify karenge ki Cisco switches kaise network hosts ke MAC addresses learn karte hain, MAC address table (CAM Table) ko verify kaise karte hain, Address Resolution Protocol (ARP) ka dynamic request-reply broadcast flow kaise chalta hai, aur switch memory se entries ko manually flush kaise karte hain. Ye guide Hinglish language aur English/Latin script mein hai.

---

## 📝 1. Lab Overview & Topology

Is lab mein hum 1 switch aur 4 PCs ki simple star topology use karenge:

### Topology Components:
*   **Switch:** 1x Cisco Catalyst 2960 Switch (`Switch1`)
*   **PCs:** 4x PCs (`PC1`, `PC2`, `PC3`, `PC4`)
*   **Cabling:** 4x Copper Straight-Through Cables

### Logical Connections & IP Table:
*   `PC1 (Fa0)` ---> `Switch1 (Fa0/1)` | IP Address: `192.168.1.1/24`
*   `PC2 (Fa0)` ---> `Switch1 (Fa0/2)` | IP Address: `192.168.1.2/24`
*   `PC3 (Fa0)` ---> `Switch1 (Fa0/3)` | IP Address: `192.168.1.3/24`
*   `PC4 (Fa0)` ---> `Switch1 (Fa0/4)` | IP Address: `192.168.1.4/24`

---

## 🛠️ 2. Step-by-Step Lab Instructions

### Step 1: Verify Initial Switch MAC Table (Khali Table Check)
Switch boot up hone par iski MAC Address Table completely empty hoti hai (except control/multicast MACs).
1.  Packet Tracer mein `Switch1` par click karein -> **CLI** tab open karein.
2.  Enable mode mein enter karein:
    ```ios
    Switch> enable
    ```
3.  Active MAC table display karne ke liye command run karein:
    ```ios
    Switch# show mac address-table
    ```
*   **Expected Output:** Table mein koi dynamics host MAC addresses (`dynamic` type) show nahi hona chahiye kyunki kisi client ne abhi tak communicate nahi kiya hai.

---

### Step 2: Observe ARP & MAC Learning (PC1 to PC2 Ping)
Jab PC1 PC2 ko ping karega, toh Layer 2 MAC learning dynamically trigger hogi:
1.  `PC1` par double-click karein -> **Desktop** -> **Command Prompt** open karein.
2.  PC2 ko ping karein:
    ```cmd
    C:\> ping 192.168.1.2
    ```
3.  *What happens under-the-hood:*
    *   PC1 ko PC2 ka MAC nahi pata, isliye woh pehle ek **ARP Request (Broadcast)** bhejta hai.
    *   Switch `Fa0/1` interface par frame receive karte hi **PC1 ka MAC Address dynamic list mein save** kar leta hai.
    *   PC2 reply mein **ARP Reply (Unicast)** bhejta hai.
    *   Switch `Fa0/2` interface par **PC2 ka MAC Address dynamic list mein save** kar leta hai.

---

### Step 3: Verify Updated MAC Table (MAC addresses seekhna)
1.  `Switch1` ke CLI console par wapas jayein.
2.  Command run karein:
    ```ios
    Switch# show mac address-table
    ```
*   **Expected Output:** Ab aapko table mein do dynamic entries dikhai dengi:
    ```text
              Mac Address Table
    -------------------------------------------
    Vlan    Mac Address       Type        Ports
    ----    -----------       --------    -----
       1    0010.11aa.22bb    DYNAMIC     Fa0/1      ! PC1's MAC Address
       1    0060.5c33.44dd    DYNAMIC     Fa0/2      ! PC2's MAC Address
    ```

---

### Step 4: Check Host ARP Table
PCs bhi targets ke IP-to-MAC bindings apni internal cache database mein save karte hain:
1.  `PC1` ke Command Prompt par wapas jayein.
2.  Local ARP cache display command run karein:
    ```cmd
    C:\> arp -a
    ```
*   **Expected Output:** PC2 ka IP `192.168.1.2` aur uska corresponding MAC address mapping dynamically display hoga.

---

### Step 5: Clear MAC Address Table (Table flush karna)
Troubleshooting ke dauran hume switch memory clear karni padti hai:
1.  `Switch1` CLI par dynamic entries clear karne ki administrative command run karein:
    ```ios
    Switch# clear mac address-table dynamic
    ```
2.  Verify karne ke liye dobara check karein:
    ```ios
    Switch# show mac address-table
    ```
*   **Expected Output:** Table dobara completely empty ho jayegi. Dobara communicate karne par hi switch physical MACs learn karega.

---

## 💡 3. Key Concepts & Troubleshooting

*   ⚠️ **ARP Broadcast Storms:** Agar network loops ho, toh ARP broadcast frames circular links par continuously amplify hote hain, jisse switch CPU utilization 100% ho jata hai aur network collapse kar jata hai.
*   🕒 **MAC Aging Timeout:** Cisco switches par dynamic MAC entries by default **`300 seconds` (5 minutes)** tak inactive rehne par automatic delete ho jati hain, jisse switch memory refresh rehti hai.

---

## 📝 4. CCNA Day 06 Lab Practice Questions

1. **Q1: Cisco switch par dynamic learned MAC addresses and interface ports mapping database check karne ki command kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`show mac address-table`**.
   </details>

2. **Q2: Local hosts (like PC0) par cache stored IP-to-MAC mapping list verify karne ki Windows console utility command kya hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`arp -a`** (ya privilege modes par `show arp` in Cisco IOS).
   </details>

3. **Q3: Switch memory se dynamic configurations elements aur learned entries clear/flush karne ki command syntax kya hogi?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`clear mac address-table dynamic`**.
   </details>

4. **Q4: Target devices network par initialize hone par gateway IP target resolve check ke liye broadcast request frame forward perform karne wale helper protocol ko kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **ARP (Address Resolution Protocol)**.
   </details>

5. **Q5: Switch dynamic MAC table entries inactivity timer threshold rules ke dynamic limits (default aging time) kitna set rehta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **`300 seconds`** (5 minutes).
   </details>

6. **Q6: Switch ke physical switch interface frames forward and switch logic ko speed-up maintain records parameters ko target space mein kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **CAM Table (Content Addressable Memory)**, jise dynamic CLI mein MAC Address Table bolte hain.
   </details>

7. **Q7: Switch port link green hone par bhi ping start hone par absolute first reply packets missing kyu dekhne ko milta hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Kyunki dynamic path check par client absolute pehle target reach address verify resolve karne ke liye **ARP request handshake** run kar raha hota hai, jis se execution lag frame drop output display hota hai.
   </details>

8. **Q8: ARP Request frames switch segment boundary par physical interface forwarding logic ke according kis mode me push check hote hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Broadcast** format mein (MAC Destination: `FFFF.FFFF.FFFF`).
   </details>

9. **Q9: ARP Reply packets client response inputs dynamically switches frames mapping par kis mode par transit map entries confirm karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Unicast** (directly source target to requestor node).
   </details>

10. **Q10: Switches frames forward analyze karne ke liye dynamic simulation packet headers levels monitoring checks run Packet Tracer tabs kis pane modes par transition key use karta hai?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **Simulation Mode** (Widescreen window checks, visually tracing packet flows step-by-step).
    </details>
