---
title: "Topic 46 - TCP (Transmission Control Protocol - Connection-Oriented & Reliable)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🤝 46. TCP (Transmission Control Protocol - Connection-Oriented & Reliable)

### 📝 Introduction (Intro)
**TCP (Transmission Control Protocol)** internet ke core transport standards me se ek hai jo **Transport Layer (Layer 4)** par operate karta hai. UDP ke relative, TCP ek **Connection-Oriented** aur **Reliable** transmission protocol hai jo packets delivery ki 100% guarantee leta hai.

#### 🔑 Core Working Mechanisms of TCP:
* **Connection-Oriented (3-Way Handshake):** Actual data packet bhejne se pehle, Sender aur Receiver aapas me ek logical connection setup karte hain. Ye process **SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK** signals ke exchange se complete hota hai.
* **Byte-Stream Reliability:** Data bits sequence ko stream wise track kiya jata hai. Received data ko order matching check karne ke liye **Sequence Numbers** aur delivery state verify karne ke liye **Acknowledgement Numbers (ACK)** updates use hote hain.
* **Minimum Header Size (20 Bytes):** TCP segments header information space dynamic hota hai (minimum **20 Bytes** aur maximum **60 Bytes** options flags ke sath). Isme Source Port, Dest Port, Seq No, ACK No, Window size, Flags (SYN, ACK, FIN, RST, PSH, URG), Checksum, aur Urgent pointer fields hote hain.

### ➕ Advantages (Fayde)
* **Guaranteed Delivery (Zero Packet Loss):** Retransmission checks aur sequence orders monitoring ke chalte data lost hone par background retransmit triggers automatically work karte hain.
* **Ordered Data Reassembly:** Lagging networks routes ke karan random orders me aane wale segments sequence numbers read karke original structure array positions reassemble ho jate hain.
* **Congestion and Flow Control:** TCP sliding window mechanism ke through receiver buffer limits dynamically track karta hai. Agar networks buffer block full ho, toh TCP processing rate request control rate automatically decrease/slow down kar deta hai.

### ➖ Disadvantages (Nuksan)
* **High Connection latency Overhead:** Transmission start hone se pehle 3-way handshake setup, packet headers size (20-60 bytes), aur continuous ACK responses waiting validation process communication rate check ko slow down kar dete hain.
* **Resource Intensive:** Active connections tracks, buffer blocks allocations, and sequence tracking states maintains resources (Server RAM space memory) zyada consume karti hain.
* **No Broadcasting/Multicasting:** TCP strictly **1-to-1 (Unicast)** connections system par design hai, ye single stream data direct mass distribution modes me send nahi kar sakta.

### 📊 Diagram
Ye layout TCP 3-Way Handshake connection setup sequence aur basic TCP Header Structure components ko show karta hai:

```
[ Sender Host ]                                         [ Receiver Host ]
       |                                                        |
       |--- 1. Connection Request (SYN, Seq = x) -------------->| (Active open)
       |                                                        |
       |<-- 2. Connection Grant (SYN-ACK, Seq = y, Ack = x+1) --| (SYN Received)
       |                                                        |
       |--- 3. Setup Complete (ACK, Ack = y+1) ---------------->| (Established!)
       |                                                        |

=================================================================================
                       [ TCP HEADER FORMAT (Minimum 20 Bytes) ]
---------------------------------------------------------------------------------
|      Source Port (16-bits)         |       Destination Port (16-bits)         |
---------------------------------------------------------------------------------
|                           Sequence Number (32-bits)                           |
---------------------------------------------------------------------------------
|                        Acknowledgement Number (32-bits)                       |
---------------------------------------------------------------------------------
| Data Offset | Reserved |   Flags   |            Window Size (16-bits)         |
---------------------------------------------------------------------------------
|         Checksum (16-bits)         |         Urgent Pointer (16-bits)         |
---------------------------------------------------------------------------------
|                           Options (0 to 40 bytes)                             |
=================================================================================
```

### 💡 Real-world Example (Udaharan)
* **Landline Telephone Conversation Call:**
  - Aapne friend ko call lagane ke liye phone dial digits enter kiye (Initiation). Phone pick up hone par aap bolte hain "Hello?" (SYN). Aapka friend bolta hai "Haan bhai, bolo!" (SYN-ACK). Aap bolte hain "Haan suno..." (ACK). Is verification (Handshake) ke baad hi main data conversation shuru hota hai.
* **Sending Registered Book Parcel:**
  - Aap book parcels post custom center se cross handovers karte hain. Har register bundle order receipt update verification stamp checks, weight limits (Flow controls), aur customer destination signature registers tracking values contains karta hai.

### 🚀 Application (Kahan use hota hai?)
* **Secure Web Browsing (HTTP/HTTPS):** Safe banking transaction sites, Facebook, Google loading layers.
* **Direct File transfers (FTP/SFTP):** Downloading software files, uploads documentation records.
* **Electronic Mails (SMTP/IMAP/POP3):** Delivering email messages securely to targets mailboxes.
* **Remote Terminal Sessions (SSH):** Secure encrypted text connections controls on servers.

---