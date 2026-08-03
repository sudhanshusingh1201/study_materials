---
title: "Topic 48 - TCP 3-Way Handshake (Connection Establishment Process)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🤝 48. TCP 3-Way Handshake (Connection Establishment Process)

### 📝 Introduction (Intro)
**TCP 3-Way Handshake** computer networking me client aur server ke beech ek reliable physical-like logical link connect/establish karne ka standard mechanism hai. Ye **Transport Layer (Layer 4)** par chalne wale TCP state transitions ka heart hai. Ye process ensure karta hai ki dono nodes mutually connect ho sakein aur transmission start karne ke liye Initial Sequence Numbers (ISNs) synchronize kar sakein.

#### ⚙️ Step-by-Step Handshake Procedure:
1. **Step 1: SYN (Synchronize - Active Open):**
   * Client server ko ek segment bhejta hai jisme **SYN flag** set hota hai (1).
   * Is segment me client apna Starting Sequence Number (ISN) bhejta hai, let's say **Seq = $x$**.
   * Client ki state `CLOSED` se switch hokar `SYN_SENT` ho jati hai.
2. **Step 2: SYN-ACK (Synchronize-Acknowledgement - Passive Open):**
   * Server client ka SYN receive karta hai aur space/resources allocate karta hai.
   * Server response segment bhejta hai jisme **SYN** aur **ACK** dono flags set hote hain.
   * Isme server apna serial sequence status (let's say **Seq = $y$**) bhejta hai aur client ke SYN packet ko ACK (Acknowledgement) karne ke liye **Ack = $x+1$** bhejta hai.
   * Server ki state `LISTEN` se switch hokar `SYN_RCVD` ho jati hai.
3. **Step 3: ACK (Acknowledgement):**
   * Client server ka SYN-ACK segment read karta hai.
   * Client server ke SYN packet ko final ACK response confirm karne ke liye ek packet bhejta hai jisme **ACK flag** set hota hai aur **Ack = $y+1$** hota hai.
   * Client ki state instantly `ESTABLISHED` ho jati hai. Jab server is packet ko receive karta hai, toh uski state bhi `ESTABLISHED` ho jati hai. Connection is open!

### ➕ Advantages (Fayde)
* **Establishes Initial Parameters Mutual Synchronization:** Dono sides parameters exchange matching locks synchronize kar lete hain (Sequence numbers, window scale sizes, Maximum Segment Size - MSS parameters).
* **Prevents Stale/Duplicate connection crashes:** Purane delayed packets internet routers se ghumi hokar achanak aayein toh sequence number check fail system ke jariye double active request block prevent ho jati hai.
* **Guarantees mutual duplex channel verification:** Confirm ho jata hai ki Client aur Server dono paths simultaneously send aur receive functions successfully run kar rahe hain.

### ➖ Disadvantages (Nuksan)
* **Round Trip Time (RTT) Connection Latency:** Actual data packet frame transition start hone se pehle 1 complete RTT cycle lagta hai connection setup ke liye (which slows down first byte load times).
* **Vulnerability to SYN Flood (DDoS Attack):** Hackers server ko high quantity fake SYN requests bhejte hain par Step 3 ka ACK response nahi bhejte. Isse server threads allocations `SYN_RCVD` slots (half-open connections) buffer limits load ho kar server exhaust system hang kar dete hain.

### 📊 Diagram
Ye layout sequence timeline sequence TCP 3-Way Handshake step numbers and parameters exchange mapping ko show karta hai:

```
[ Client Machine ]                                         [ Server Machine ]
     |                                                             |
     |---- 1. SYN Flag: 1, Seq: x (SYN_SENT) --------------------->| (Allocates resources)
     |                                                             | [SYN_RCVD]
     |<--- 2. SYN-ACK Flags: 1, Seq: y, Ack: x+1 ------------------|
     |                                                             |
     |---- 3. ACK Flag: 1, Ack: y+1 ------------------------------>| (Established!)
     |     [ESTABLISHED]                                           | [ESTABLISHED]
```

### 💡 Real-world Example (Udaharan)
* **Two Walkie-Talkie Users Conversation Metaphor:**
  - **Step 1 (SYN):** Amit button press karke bolta hai: "Sumit, kya tum mujhe sun sakte ho? Mera code name alpha hai." (SYN)
  - **Step 2 (SYN-ACK):** Sumit sun kar response karta hai: "Haan alpha, main tumhari aawaz sun sakta hun. Kya tum meri aawaz sun sakte ho? Mera code name beta hai." (SYN-ACK)
  - **Step 3 (ACK):** Amit bolta hai: "Haan beta, clear voice aa rahi hai. Over and out, main baat shuru kar raha hun." (ACK).
  - Ab dono ke beech standard communication channel open ho chuka hai.

### 🚀 Application (Kahan use hota hai?)
* **Web pages access handshakes:** Opening socket descriptors for HTTPS websites.
* **SSH remote shells validation:** Logging credentials checks parameters updates.
* **TCP APIs endpoints initialization:** Client-server microservices integration calls setup.

---