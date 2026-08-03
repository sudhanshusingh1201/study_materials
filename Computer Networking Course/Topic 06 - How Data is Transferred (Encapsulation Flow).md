---
title: "Topic 06 - How Data is Transferred (Encapsulation Flow)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🔄 6. How Data is Transferred (Encapsulation Flow)

### 📝 Introduction (Intro)
Computer network par data transfer ek structured step-by-step process hai. Jab hum koi text message, image, ya video send karte hain, toh data top layers se lower physical layers tak travel karta hai jise **Encapsulation** kehte hain. Phir wo physical medium ke through transfer hota hai aur receiver par reverse order me **Decapsulation** hota hai.

Ye pura system main standard **OSI Model (7 Layers)** aur **TCP/IP Model (4 Layers)** ke through chalta hai:

#### 🛠️ Step-by-Step Data Transfer Journey:
1. **Application Layer (Data creation):** User app (jaise WhatsApp ya Browser) par data generate karta hai.
2. **Transport Layer (Segmentation):** Raw data ko small manageable chunks me toda jata hai jise **Segments** kehte hain. Yahan **TCP** ya **UDP** header lagaya jata hai (jo source/destination ports decide karte hain).
3. **Network Layer (Packetization):** Segments ke upar routing information (Source IP aur Destination IP) lagayi jati hai. Ab ise **Packets** kehte hain.
4. **Data Link Layer (Framing):** Packets ke aage aur peeche physical details (Source MAC Address, Destination MAC Address, aur Error Checking FCS) jod di jati hain. Ab ise **Frames** kehte hain.
5. **Physical Layer (Transmission):** Frames ko electrical pulses, light signals (fiber), ya radio frequencies (wireless) me convert kiya jata hai jise **Bits (0 aur 1)** bolte hain, aur medium par bhej diya jata hai.
6. **Decapsulation (Receiver Side):** Receiver computer in bits ko receive karta hai, physical signal se frame banata hai, MAC details check karke remove karta hai, IP details check karke packets kholta hai, port number dekhkar segment reassemble karta hai aur raw data display kar deta hai.

### ➕ Advantages (Fayde)
* **Standardized System:** OSI aur TCP/IP protocols global standard hain, jisse alag-alag companies ke OS (Windows, Android, iOS) ek dusre se aasaani se communicate kar sakte hain.
* **Fault Management:** Agar physical line me disturbance aaye aur bits lost ho jayein, toh Transport Layer (TCP) automatic recognize karke data fir se re-send kar deta hai.
* **Security & Encryption:** Encapsulation phase me data ko encrypt kiya ja sakta hai (e.g. HTTPS/SSL), jisse raste me koi hacker data chura nahi sakta.

### ➖ Disadvantages (Nuksan)
* **Encapsulation Overhead:** Har layer par extra headers (port, IP, MAC, FCS) lagte hain, jisse metadata badh jata hai aur real internet bandwidth thodi waste hoti hai.
* **Latency (Network Delay):** Har packet ko network switches, hubs aur routers par ruk kar processing (MAC table lookup aur IP routing table verification) karni hoti hai, jisse transmission speed thodi delay ho jati hai.
* **Data Collision:** Shared mediums (jaise Wi-Fi ya shared ethernet hubs) par agar do devices ek sath signals bhej dein, toh data collision ho jata hai aur unhe dubara re-send karna padta hai.

### 📊 Diagram
Ye Sender side par data ke wrap (Encapsulation) hone aur Receiver side par strip (Decapsulation) hone ke pure process ko darshata hai:

```mermaid
graph TD
    subgraph Sender Computer (Encapsulation)
        Data[Raw Data: e.g. 'Hello'] -->|Transport Layer Add Ports| Segment[Segments: TCP Header + Data]
        Segment -->|Network Layer Add IPs| Packet[Packets: IP Header + Segment]
        Packet -->|Data Link Add MACs| Frame[Frames: MAC Header + Packet + FCS]
        Frame -->|Physical Layer Convert| Bits[Bits: 01001000 01100101...]
    end

    subgraph Physical Network (Transit)
        Bits -->|Wired Cables / Wireless Waves| NetDevices[Switches & Routers]
        NetDevices -->|Route Packets & Forward Frames| R_Bits[Bits Received]
    end

    subgraph Receiver Computer (Decapsulation)
        R_Bits -->|Read Physical Signals| R_Frame[Read Frames]
        R_Frame -->|Strip MAC & Verify FCS| R_Packet[Read Packets]
        R_Packet -->|Strip IP & Route| R_Segment[Read Segments]
        R_Segment -->|Strip Port & Reassemble| R_Data[Raw Data Restored: 'Hello']
    end
```

### 💡 Real-world Example (Udaharan)
* **Courier Service Analogy:** 
  - **Data:** Ek important letter (Raw Data).
  - **Segment:** Letter ko security aur shape ke liye plastic cover me band kiya (Transport layer segment wrapper).
  - **Packet:** Us cover ko ek paper envelope me daala aur upar Sender & Receiver ke ghar ka Address (IP Address) likha (Network layer packet wrapper).
  - **Frame:** Envelope ko delivery truck ke security container/crate me store kiya, jis par driver ka source & target dispatch ID (MAC Address) aur weight checks hain (Data link layer frame).
  - **Physical:** Truck sadak par safar karta hai (Physical medium/cables).
  - **Decapsulation:** Receiver ke ghar pahunchne par container khulega, fir address check hoga, envelope phatega, aur letter hath me mil jayega.

### 🚀 Application (Kahan use hota hai?)
* **Every Network Interaction:** Jab bhi internet use hota hai (jaise WhatsApp, Instagram scroll, web browsing), background me yahi complete process chalta hai.
* **File Uploads/Downloads:** Badi files transfer protocol (FTP/SFTP) ke jariye encapsulation chunks ke form me safety se travel karti hain.
* **Real-time Video Calls:** Zoom ya Teams video streams packets ban kar milliseconds me capture, encapsulate aur display hoti hain.

---