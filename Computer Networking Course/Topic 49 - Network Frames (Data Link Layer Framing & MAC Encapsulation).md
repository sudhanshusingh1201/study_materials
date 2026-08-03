---
title: "Topic 49 - Network Frames (Data Link Layer Framing & MAC Encapsulation)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 📦 49. Network Frames (Data Link Layer Framing & MAC Encapsulation)

### 📝 Introduction (Intro)
**Network Frame** computer networks ke **Data Link Layer (Layer 2)** par data transmission ki basic unit hai. Jab Layer 3 (Network Layer) se IP Packet niche Layer 2 par aata hai, toh hardware level par transport karne ke liye use extra boundaries aur hardware addresses ke sath wrap kiya jata hai. Is wrapping process ko **Framing** kehte hain aur resulting packet structure ko **Frame** kehte hain.

* **Packet vs Frame Difference:**
  - **IP Packet (Layer 3):** Isme logical addresses (Source IP and Destination IP) hote hain jo pure global internet routing me same rehte hain.
  - **Frame (Layer 2):** Isme physical hardware addresses (**Source MAC** and **Destination MAC**) hote hain. Har local network hop (router point) par purana frame envelope utar kar naya frame envelope lagaya jata hai, jisse MAC addresses change hote rehte hain.

#### 🗂️ Structure of a Standard Ethernet Frame (IEEE 802.3):
1. **Preamble & SFD (Start Frame Delimiter):** 8 bytes ki alternate bits series (101010...) jo receiver clock timing synchronize karti hai aur notify karti hai ki frame start ho raha hai.
2. **Destination MAC (6 bytes):** Target device ka physical MAC address.
3. **Source MAC (6 bytes):** Bhejne wali device ka physical MAC address.
4. **EtherType (2 bytes):** Ye batata hai ki frame ke andar kis Layer 3 protocol (jaise IPv4, IPv6, ARP) ka packet wrapped hai.
5. **Payload (46 to 1500 bytes):** Actual IP Packet jo travel kar raha hai.
6. **FCS/Trailer (4 bytes):** **Frame Check Sequence** jisme Cyclic Redundancy Check (CRC) error checking code hota hai.

### ➕ Advantages (Fayde)
* **Local Hop-to-Hop Delivery:** Frame boundaries network switches ko local devices ke physical interfaces (ports) par direct data delivery allow karti hain.
* **Physical Error Detection:** FCS/CRC trailer check ke through corrupt frames receiver level par hi drop ho jate hain, jisse upper layers (IP/TCP) ka processing load bach jata hai.
* **MTU Boundaries Enforcement:** Standard frame sizing limits (Maximum Transmission Unit - 1500 bytes payload) physical media lines crash overflow hone se rokati hain.

### ➖ Disadvantages (Nuksan)
* **Header & Trailer Overhead:** Har frame ke sath 18 to 26 bytes ka extra physical data (header+trailer) judta hai, jisse dynamic network throughput capacity ka chhota part bandwidth waste me chala jata hai.
* **Size Constraints (Runts & Giants):**
  - **Runt Frames:** Agar frame size 64 bytes se kam ho (collision noise ke chalte), toh devices use junk samajh kar discard kar deti hain.
  - **Giant Frames:** Agar frame size 1518 bytes se bada ho, toh switch use line jam protection ke chalte drop kar deta hai.
* **Hop-Local scope:** MAC address routing changes har router cross hone par frame recreation generation mandatory karti hain (increases processing latency).

### 📊 Diagram
Ye layout Data Link Layer framing structure encapsulation aur dynamic hop MAC modifications flow checks ko show karta hai:

```
========================================================================================
                      [ ETHERNET FRAME STRUCTURE (IEEE 802.3) ]
----------------------------------------------------------------------------------------
| Preamble |  SFD  | Dest MAC | Source MAC | EtherType |  Payload (IP Packet)  |  FCS  |
| (7 bytes)|(1 byte| (6 bytes)|  (6 bytes) | (2 bytes) |  (46 to 1500 bytes)   |(4 bytes
========================================================================================

                 [ Physical Hop MAC Address Modification Flow ]
[ Sender Client ]                   [ Router Point ]                 [ Target Server ]
  MAC: AA:AA:AA                       MAC: BB:BB:BB                    MAC: CC:CC:CC
        |                                   |                                |
        |== Frame 1 (Dest MAC: BB) ========>| (Opens Frame)                  |
        |                                   |  [IP Packet inside remains same]
        |                                   |== Frame 2 (Dest MAC: CC) =====>|
```

### 💡 Real-world Example (Udaharan)
* **Local Delivery Truck Container Metaphor:**
  - Maan lijiye aapne Amazon se ek gift order kiya. Gift box par sender-receiver ka final name-address (IP addresses) likha hai jo kabhi nahi badalta. Yahi humara **IP Packet** hai.
  - Lekin delivery company direct parcel ko fek nahi sakti. Wo use ek local logistics truck container me pack karti hai. Us truck container ke bahar local warehouse stop code (MAC address) likha hota hai. Yahi truck box humara **Frame** hai.
  - Delhi se Noida jaane me, Delhi warehouse par parcel ko Delhi-truck se utar kar (Frame stripping) Noida-truck me load kiya jata hai (New Frame generation with new MAC labels), par original gift box (IP packet) unchanged rehta hai.

### 🚀 Application (Kahan use hota hai?)
* **Local LAN Switching:** Switched ethernet networks delivering packages via MAC tables.
* **Wi-Fi Encapsulations:** Wireless frames formats transmission inside IEEE 802.11 environments.
* **WAN Link protocols:** Encapsulating point-to-point connections frames (PPP/HDLC) over leased lines.

---