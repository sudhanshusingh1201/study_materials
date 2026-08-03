---
title: "Topic 25 - Layer 2 - Data Link Layer (Node-to-Node Delivery)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🔗 25. Layer 2 - Data Link Layer (Node-to-Node Delivery)

### 📝 Introduction (Intro)
**Data Link Layer (Layer 2)** OSI Model ki doosri layer (neeche se) hoti hai. Is layer ka main target same local physical network (LAN) ke andar directly connected do nodes ya network devices ke beech reliably aur error-free data chunks transmit karna hai (called **Node-to-Node** ya **Hop-to-Hop Delivery**).

* **Sublayers Split:** Data Link Layer internally do parts me split hoti hai:
  1. **LLC (Logical Link Control):** Upper layers (Layer 3 IP standard) ke interfaces aur formats identification protocols handle karti hai.
  2. **MAC (Media Access Control):** Hardware interface rules and physical link access control handle karti hai (preventing packet collisions).

#### 🔑 Core Functions of Layer 2:
1. **Framing:** Layer 3 se aane wale IP packets ko logical envelopes me pack karti hai jinhe **Frames** kehte hain. Frame me ek local Header (MAC addresses) aur local Trailer (Error Check flags) lagaya jata hai.
2. **Physical Addressing (MAC Addressing):** Frame par sender aur receiver ka **MAC Address** (48-bit unique factory number hardcoded on NIC) insert karti hai.
3. **Flow Control:** Fast sender aur slow receiver speed limitations balance karna, taaki receiver card memory buffers exhaust/overflow na ho.
4. **Error Control (CRC / FCS):** Frame trailer me **FCS (Frame Check Sequence)** or **CRC (Cyclic Redundancy Check)** checksum formulas add karke check karna ki transit me data bits corrupt toh nahi hue. Mismatch hone par frame direct drop/delete kar diya jata hai.
5. **Access Control:** Manage karna ki shared common physical cables/links standard collision detection rules (jaise CSMA/CD or CSMA/CA) ke under kab dynamic transmissions active karein.

### ➕ Advantages (Fayde)
* **Local Error Isolation:** Hardware level par corrupt frames drop ho jate hain, jisse useless garbage data dynamic network traffic increase nahi karti.
* **Collision Protection:** Standard media access control laws shared cables par traffic overwrites aur nodes collisions prevent karte hain.
* **Incredibly Fast Local Transfers:** Hardware switches aur NIC cards port level mappings use karte hain, jo Layer 2 transfers ko ultra-fast banate hain inside LANs.

### ➖ Disadvantages (Nuksan)
* **No Global Routing Capacity:** Ye layer direct internet routing nahi kar sakti. Ye local broadcast boundary (LAN) se bahar search nahi kar sakti; different network lines link karne ke liye L3 routers standard necessary hain.
* **Metadata Size Overhead:** Frame headers aur trailers (Preamble + Source MAC + Dest MAC + Type + FCS) local bandwidth capability me extra 18-26 bytes overhead weight add karte hain.
* **Switch buffer limitations:** Heavy traffic conditions me localized switches buffers overflow ho jate hain, jisse healthy frames drops hone lagte hain.

### 📊 Diagram
Ye flow mapping IP packet par MAC address wrapping (Framing) aur local L2 switch ke routing function loop ko show karti hai:

```mermaid
graph TD
    Layer3[Layer 3: Network Packet] --> Layer2[Layer 2: Data Link Layer]
    
    subgraph Operations inside Data Link Layer
        Layer2 --> Frame[1. Framing: Add MAC Header & FCS Trailer]
        Layer2 --> LLC[2. LLC: Identify Upper Layer protocol]
        Layer2 --> MACSub[3. MAC Sublayer: Physical Medium Access check]
    end

    Frame --> Layer1[Layer 1: Physical Layer - Bit Streams]
    
    subgraph LAN Switch Transit (MAC-to-MAC delivery)
        Switch[L2 Local Switch] -->|Inspects Dest MAC| DeviceA[Device A MAC: AA-BB-CC...]
        Switch -->|Inspects Dest MAC| DeviceB[Device B MAC: DD-EE-FF...]
    end
```

### 💡 Real-world Example (Udaharan)
* **Local Office Courier Dispatch Metaphor:**
  - **Global Planner (Layer 3):** Parcel check karke regional branch center floor drop kar gaya (Destination IP matching building).
  - **Local Floor Dispatcher (Layer 2 - Data Link Layer):**
    1. **Physical Address = Desk Nameplate (MAC):** Local dispatcher parcel par desk label chipkata hai (e.g. "Ramesh, Cabin 4"). Ramesh ka location address PIN system me constant hai aur wo wahi desk use karta hai (Factory Address).
    2. **FCS/CRC Check:** Delivery desk verify karegi ki parcel seal safely closed hai ya nahi. Seal damaged toh parcel throw away.
    - Dispatcher office gate ke bahar global highway path map nahi dekhta, wo bas office layout switchboard connections handles karta hai.

### 🚀 Application (Kahan use hota hai?)
* **Hardware switches and Hubs:** Layer 2 Switches, Local Bridges, Access Points, NIC (Network Interface Cards).
* **Protocols:** Ethernet (IEEE 802.3), Wi-Fi (IEEE 802.11), Point-to-Point Protocol (PPP).
* **Address Mapping:** Dynamic ARP protocols locating hardware MAC IDs in local networks.

---