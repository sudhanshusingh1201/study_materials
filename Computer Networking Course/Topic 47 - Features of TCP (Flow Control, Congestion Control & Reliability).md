---
title: "Topic 47 - Features of TCP (Flow Control, Congestion Control & Reliability)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# ⚙️ 47. Features of TCP (Flow Control, Congestion Control & Reliability)

### 📝 Introduction (Intro)
**Features of TCP** Transport Layer par uski functionality aur behavior ko define karte hain. TCP sirf data transfer nahi karta, balki pure session ko highly organized, optimal aur safe tarike se run karta hai. 

#### 🔑 Key Features of TCP:
1. **Connection-Oriented:** Data transfer se pehle sender aur receiver ka mutual sync validation (SYN, SYN-ACK, ACK 3-way handshake) setup compulsory hota hai.
2. **Reliability:** Custom algorithms (Checksum checks, Sequence Numbers, ACKs updates, aur Retransmissions) guarantee karte hain ki zero bits levels errors or loss ho.
3. **Full Duplex Service:** Ek hi time frame ke andar dono machines simultaneously data bhej aur receive kar sakti hain.
4. **Byte Stream Service:** TCP message formats ko individual structures me read karne ke bajay ek continuous sequence of bytes (byte stream) ki tarah transmit karta hai.
5. **Flow Control (Sliding Window):** Receiver sender ko bol sakta hai ki "slow down". TCP **Sliding Window Protocol** use karta hai jahan receiver updates send karta hai ki uske buffer zone me kitni space baaki hai (**Window Size**), aur sender sirf utna hi data bhejta hai.
6. **Congestion Control:** Agar network route congestion (traffic jam) ho, toh TCP algorithms (like Slow Start, Congestion Avoidance, Fast Retransmit) active window boundaries reduce karke data rate throttle kar dete hain taaki server crash se bacha ja sake.

### ➕ Advantages (Fayde)
* **High Flow Optimization:** Receiver capability (Flow Control) aur Network bottleneck limits (Congestion Control) dono ke base par delivery bandwidth tune ho jati hai.
* **Data Guarantee:** File structures headers safe format transitions complete rehte hain.
* **Anti-Collusion Protocols:** Dynamic traffic monitoring algorithm packet storm collision and network breakdown prevent karta hai.

### ➖ Disadvantages (Nuksan)
* **Complex State Machines Bookkeeping:** Flow values updates aur Congestion thresholds adjust karne me high computations locks algorithms call karni padti hain (delays data routing).
* **Memory Blocks reservation:** Sliding windows ranges buffer limits registers maintain karne me CPU context switching badh jati hai.
* **Not suitable for real-time video/gaming:** Flow rates drop limitations aur continuous checks updates ke chalte real-time dynamic streaming services run nahi ho patin.

### 📊 Diagram
Ye layout TCP **Sliding Window** flow control mechanism ke operations frame movement sequence check ko show karta hai:

```
                  [ SENDER BUFFER BYTE STREAM ]
[ Sent & ACKed ]     [ Sent, Not ACKed ]     [ Can Send Instantly ]     [ Cannot Send ]
  1   2   3   4     |  5   6   7   8   9  |    10   11   12   13     |   14   15   16
---------------------------------------------------------------------------------------
                    |<--- Window Size = 5 --->|
                     (Slides to right when bytes 5 & 6 are acknowledged by receiver)
```

### 💡 Real-world Example (Udaharan)
* **Factory Assembly Line Metaphor:**
  - **Flow Control (Sliding Window):** Maan lijiye conveyor belt (Medium) par ek workers machine boxes forward kar rahi hai. Aage packing lane worker (Receiver) maximum 5 boxes per minute pack kar sakta hai. Agar conveyor belt speed badhegi, toh packer aage button click karke belt speed slow (decreasing Window size) kar dega, jisse boxes assemble flow block na hon.
  - **Congestion Control:** Highway traffic monitoring police agar aage raste me jam (Network congestion) dekhti hai, toh local toll gates blocks limits par entry slow down kar deti hai taaki highway full choke or freeze na ho jaye.

### 🚀 Application (Kahan use hota hai?)
* **Enterprise Databases replication:** Syncing multiple distributed database clusters securely.
* **Large File transfers:** Reliable FTP sync of giant system images.
* **Web application protocols (HTTP/2 - HTTP/1.1):** Structured assets resource parsing.

---