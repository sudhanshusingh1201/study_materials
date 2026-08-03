---
title: "Topic 45 - UDP (User Datagram Protocol - Connectionless & Fast)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# ⚡ 45. UDP (User Datagram Protocol - Connectionless & Fast)

### 📝 Introduction (Intro)
**UDP (User Datagram Protocol)** computer networks ke **Transport Layer (Layer 4)** par kaam karne wala ek core protocol hai. TCP ke opposite, UDP ek **Connectionless** aur **Unreliable (Non-guaranteed)** protocol hai. Iska main focus bina kisi delay ya jhanjhat ke data ko fast deliver karna hota hai.

#### 🔑 Core Characteristics of UDP:
* **Connectionless:** Sender aur Receiver ke beech data send karne se pehle koi handshake (connection establishment) nahi hota. Direct data packets (jinhe **Datagrams** kehte hain) bhej diye jate hain.
* **Unreliable:** UDP is cheez ki guarantee nahi leta ki packet recipient tak pahuncha ya nahi, na hi ye packets ko correct order me reassemble karta hai. Koi Acknowledgement (ACK) mechanisms nahi hote.
* **Lightweight Header (Only 8 Bytes):** TCP ka header space minimum 20 bytes ka hota hai, jabki UDP ka header size fixed **8 Bytes** (Source Port, Destination Port, Length, Checksum - 2 bytes each) hota hai.

### ➕ Advantages (Fayde)
* **Ultra-Low Latency & High Speed:** Connection handshakes or acknowledgements check na hone ke karan data forwarding instant hoti hai.
* **Minimal Protocol Overhead:** 8-byte header ke chalte bandwidth consumption na ke barabar hota hai.
* **Support for Broadcasting & Multicasting:** UDP dynamic level par single source stream ko simultaneously thousands of destinations nodes par distribute kar sakta hai (TCP cannot do this as it is strictly 1-to-1).

### ➖ Disadvantages (Nuksan)
* **No Packet Delivery Guarantee:** Network loop congestion hone par packets easily drop ho jate hain aur data corruption alerts user apps ko handles karne padte hain.
* **No Flow or Congestion Control:** UDP blind-rate speed par packets dispatch karta hai. Agar receiver machine crash or buffer overflow ho jaye, toh UDP transmission slow down nahi hota (can overwhelm networks).
* **Out-of-Order Delivery:** Packets path changes ke chalte aage-piche deliver ho sakte hain, sequence track records missing rehne se reconstruction app codes level par karni padti hai.

### 📊 Diagram
Ye layout UDP un-acknowledged datagram streams forwarding structure aur fixed 8-byte header fields formats ko show karta hai:

```
[ Sender Client ]                                   [ Receiver Host ]
        |                                                   |
        |--- Datagram 1 (Seq: None, No Handshake) --------->| (Received)
        |                                                   |
        |--- Datagram 2 ----------------------------------->| (Packet Dropped/Lost!)
        |                                                   |  [No Retransmit, No ACK]
        |--- Datagram 3 ----------------------------------->| (Received out-of-order)

=====================================================================
                    [ UDP HEADER FORMAT (8 Bytes) ]
---------------------------------------------------------------------
|   Source Port (16-bit)      |     Destination Port (16-bit)       |
---------------------------------------------------------------------
|   Length (16-bit)           |     Checksum (16-bit)               |
=====================================================================
```

### 💡 Real-world Example (Udaharan)
* **Ordinary Mail Postcard vs Registered Post:**
  - **TCP = Registered Post:** Courier handler aapke door aakar signature leta hai, delivery receipt update karta hai aur confirmation check back bhejta hai.
  - **UDP = Ordinary Postcard:** Aapne postcard par details likhi aur post box me drop kar di (No Handshake). Ab card post handler se drop ho jaye ya barish me kharab ho jaye, koi tracking ya re-delivery guarantee nahi hai.
* **Live Sports Television Stream:** Match broadcast hotey waqt agar internet signal 1 second ke liye weak ho jaye, toh screen thodi pixelate ya freeze (frame drops) ho jati hai. Par network stream pause hokar past frames re-download nahi karti, balki match live screen se coordinate chalta rehta hai.

### 🚀 Application (Kahan use hota hai?)
* **Real-time Video/Audio Streaming:** YouTube Live, Zoom meetings, Discord voice channels, aur VoIP calls.
* **Online Multiplayer Gaming:** Real-time movement vectors coordinate sync (games like Counter-Strike/PUBG).
* **Quick Queries services:** DNS lookup queries (Port 53) and DHCP network configurations requests.

---