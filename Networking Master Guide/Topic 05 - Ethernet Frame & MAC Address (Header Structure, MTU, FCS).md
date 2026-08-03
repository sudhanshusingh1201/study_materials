---
title: "Topic 05 - Ethernet Frame & MAC Address (Header Structure, MTU, FCS)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 📦 5. Ethernet Frame & MAC Address (Header Structure, MTU, FCS)

OSI Layer 2 par data pack ko **Ethernet Frame** kehte hain.

### 📊 Ethernet II Frame Structure:
1. **Preamble & SFD (8 Bytes):** Synchronization bits taaki receiver ready ho jaye.
2. **Destination MAC (6 Bytes):** Target device physical address.
3. **Source MAC (6 Bytes):** Sender device physical address.
4. **EtherType (2 Bytes):** Layer 3 protocol identity (e.g. `0x0800` for IPv4).
5. **Payload/Data (46 - 1500 Bytes):** Actual data packet.
6. **FCS/CRC (4 Bytes):** Error-checking bits. Match na hone par switch frame drop kar deta hai.

### 📏 Size Limits:
* **Minimum Frame Size:** 64 Bytes (64 se chote frames ko **Runts** bolte hain, aur ye discard hote hain).
* **MTU (Maximum Transmission Unit):** Standard ethernet payload size is **1500 Bytes** (Frame size 1518 Bytes).
* **Jumbo Frames:** 9000 Bytes tak ka frame size, jo server communication me overheads kam karta hai.

---