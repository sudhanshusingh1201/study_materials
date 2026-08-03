---
title: "Topic 43 - TCP Timers (Retransmission, Keep-Alive, Time-Wait, Persistent)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# ⏱️ 43. TCP Timers (Retransmission, Keep-Alive, Time-Wait, Persistent)

### 📝 Introduction (Intro)
**TCP Timers** computer networks ke **Transport Layer (Layer 4)** par chalne wale TCP connection state machines ka sabse critical segment hain. Inka main objective data transmission flow control ensure karna, network deadlocks (phasna) se bachana, aur connections states ko strictly regulate karna hota hai.

#### 🔑 The 4 Essential TCP Timers:
1. **Retransmission Timer (RTO - Retransmission Timeout):**
   * *Purpose:* Jab sender segment bhejta hai, toh is timer ko start karta hai. Agar timer expire hone se pehle ACK (Acknowledgement) na mile, toh sender segment ko automatically **retransmit** (dobara send) kar deta hai. Iska duration RTT (Round Trip Time) algorithm ke base par dynamically change hota rehta hai.
2. **Keep-Alive Timer:**
   * *Purpose:* Agar dono devices ke beech connection active hai par lambe samay (normally 2 hours) se koi data transfer nahi hua, toh keep-alive timer expire ho jata hai. TCP server automatically probes packets (validation queries) bhejta hai. Agar receiver response nahi deta, toh connection close kar diya jata hai.
3. **Time-Wait Timer (2MSL - Maximum Segment Lifetime):**
   * *Purpose:* Connection close (FIN-ACK flow) hone ke baad, initiator node socket ko direct close nahi karta. Wo connection ko **2MSL** (usually 2 to 4 minutes) ke liye TIME_WAIT state me rakhta hai. Isse ensure hota hai ki:
     - Final ACK data package target computer tak secure pahunch gaya ho.
     - Network pipelines me bache-khuche duplicate packets automatic discard (die out) ho sakein.
4. **Persistent Timer:**
   * *Purpose:* Jab receiver apna buffer space bharne par dynamic window size `0` bhejta hai (sender ko rokta hai), aur baad me buffer khali hone par window size update bhejta hai jo network me **lost** ho jata hai. Bada deadlock prevent karne ke liye, Persistent Timer expire hone par sender periodic probe segments send karta hai receiver ka true buffer status fetch karne ke liye.

### ➕ Advantages (Fayde)
* **Zero Deadlocks (Continuous Flow):** Loss conditions updates handles hone se network me deadlocks freeze prevent ho jate hain.
* **Guaranteed Reliability:** Retransmission timeout (RTO) checks protect packets from random network drop losses.
* **Clean State Transitions:** Time-wait states guarantee that trailing legacy packet segments do not mix-up with new socket connections.

### ➖ Disadvantages (Nuksan)
* **High System resource Consumption:** Har active TCP session (lakhon active sockets servers par) ke liye simultaneously 4 timers calculations active servers CPU/RAM memory states exhaust kar sakti hain.
* **Complex Tuning Calculations:** Timer timeouts default duration sets karna extreme complex hai. Agar duration bahut short ho, toh duplicate fuzul packet transmission badhenge; agar bahut long ho, toh loss detection delay badh jayega.

### 📊 Diagram
Ye layout TCP Retransmission (RTO) aur Time-Wait (2MSL) state duration flows ko show karta hai:

```
[ Sender Machine ]                                        [ Receiver Machine ]
        |                                                          |
        |--- Segment 1 (Start Retransmit Timer) ------------------>| (Packet Lost!)
        |                                                          |
        X  <-- (Timer Expired! Timeout reached)                    |
        |                                                          |
        |=== Retransmit Segment 1 (Restart Timer) ================>| (Received)
        |                                                          |
        |<-- ACK Segment 1 ----------------------------------------| (Stop Timer)
```

### 💡 Real-world Example (Udaharan)
* **Restaurant Seat Waiting Metaphor:**
  - **Retransmission Timer (RTO):** Aapne cafe me waiter se sandwich order kiya aur watch me **10 minutes** timer lagaya. Agar 10 minutes tak sandwich nahi aaya (No ACK), aap counter par dobara order place karte hain (Retransmit).
  - **Keep-Alive Timer:** Aap ek seat par baithe hain par 1 ghante se kuch order nahi kiya. Waiter aakar puchta hai: "Sir, aage aur order karna hai ya table khali karein?" (Keep-alive probe).
  - **Time-Wait (2MSL):** Guest ke table se uthne ke baad manager 5 minutes table empty rakhta hai taaki clean/sanitize (discard residual items) ho sake aur next customer bina legacy garbage ke fresh baith sake.

### 🚀 Application (Kahan use hota hai?)
* **Reliable TCP Handshakes:** Maintaining integrity in HTTP/HTTPS internet browsings.
* **Database Keep-Alives:** Keeping database server ports persistent and active for remote operations.
* **Mobile networks cell switching:** Reconnection parameters when users move across cellular towers.

---