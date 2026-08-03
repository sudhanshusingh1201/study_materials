---
title: "Topic 19 - OSI Model Overview (Open Systems Interconnection)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🗼 19. OSI Model Overview (Open Systems Interconnection)

### 📝 Introduction (Intro)
**OSI Model (Open Systems Interconnection Model)** ek conceptual/theoretical framework hai jise 1984 me **ISO (International Organization for Standardization)** ne networking processes ko standardize aur categorize karne ke liye publish kiya tha.

Iska main purpose alag-alag companies (jaise Apple, Microsoft, Cisco, Intel) ke hardware aur software platforms ko aapas me bina kisi communication boundaries ke bridge (connect) karna tha.

* **Layered Architecture:** OSI Model total **7 vertical layers** me design kiya gaya hai. Har layer ka networking me ek specific discrete job hota hai. Data jab sender device se nikalta hai, toh wo Layer 7 se Layer 1 ki taraf neeche travel karta hai (Encapsulation), aur receiver end par pahunchkar Layer 1 se Layer 7 ki taraf upar travel karta hai (Decapsulation).

#### 🗼 The 7 Layers of OSI Model (Names Only):
1. **Layer 7: Application Layer**
2. **Layer 6: Presentation Layer**
3. **Layer 5: Session Layer**
4. **Layer 4: Transport Layer**
5. **Layer 3: Network Layer**
6. **Layer 2: Data Link Layer**
7. **Layer 1: Physical Layer**
*(Note: Aapne kaha hai ki layers ek-ek karke puchenge, toh hum inki andruni details aage padhenge!)*

### ➕ Advantages (Fayde)
* **Interoperability (Universal Standard):** Ye standard kisi bhi vendor ke computer hardware aur operating system (jaise Windows client talking to Linux server) ko standard guidelines ke under direct connectivity deta hai.
* **Granular Troubleshooting:** Network faults debug karna aasaan ho jata hai. Agar connectivity drop ho, toh engineers layers check karte hain (jaise: L1 issue = Cable damage, L3 issue = Bad IP address routing, L7 issue = App crash).
* **Modular Development:** Software aur hardware developer kisi bhi individual layer me dynamic modifications kar sakte hain bina baaki 6 layers ko impact kiye.
* **Pedagogical/Educational Value:** Networking ke extremely complex structures ko step-by-step modular units me padhna aur samajhna highly simplified banata hai.

### ➖ Disadvantages (Nuksan)
* **Purely Theoretical Reference:** OSI Model real-world networks me direct implement nahi hota. Aaj hamara poora internet **TCP/IP Model (4/5 Layers)** standard par chalta hai, aur OSI model sirf padhne/reference ke liye use hota hai.
* **Redundancy (Service Duplication):** Kuch operations alag-alag layers par repeat hote hain. Jaise error-checking aur flow-control mechanisms Layer 2 (Data Link) aur Layer 4 (Transport) dono jagah check hote hain.
* **Header Overhead:** Har layer ke pass data packets ke aage apna unique metadata header wrapping lagana padta hai, jisse total bandwidth utilization efficiency drop ho jati hai.

### 📊 Diagram
Ye data transition flow (Encapsulation from sender and Decapsulation at receiver) ko 7 layers me represent karta hai:

```mermaid
graph TD
    subgraph SENDER (Encapsulation - Downwards)
        S7[Layer 7: Application] --> S6[Layer 6: Presentation]
        S6 --> S5[Layer 5: Session]
        S5 --> S4[Layer 4: Transport]
        S4 --> S3[Layer 3: Network]
        S3 --> S2[Layer 2: Data Link]
        S2 --> S1[Layer 1: Physical]
    end

    S1 ===|Physical Medium: Cables/Waves| R1

    subgraph RECEIVER (Decapsulation - Upwards)
        R1[Layer 1: Physical] --> R2[Layer 2: Data Link]
        R2 --> R3[Layer 3: Network]
        R3 --> R4[Layer 4: Transport]
        R4 --> R5[Layer 5: Session]
        R5 --> R6[Layer 6: Presentation]
        R6 --> R7[Layer 7: Application]
    end
```

### 💡 Real-world Example (Udaharan)
* **Global Post Metaphor:**
  - **Layer 7 (Application - Letter):** Aapne message likha (Aapka dynamic content).
  - **Layer 6 (Presentation - Language):** Aapne use English me convert kiya aur formatting lock kari.
  - **Layer 5 (Session - Booking):** Post office counter par booking session start hua.
  - **Layer 4 (Transport - Envelope Wrapper):** Letter envelope me pack hua aur tracking code lagaya.
  - **Layer 3 (Network - IP Addresses):** Envelopes ke upar sender aur receiver ka permanent home address/PIN code chipkaya.
  - **Layer 2 (Data Link - Dispatch Container):** Envelopes local truck container boxes me transfer hue (using dispatch station IDs/MAC addresses).
  - **Layer 1 (Physical - Highways):** Truck road network (physical cables) ke jariye nikal gayi.
  - Receiver side par iska perfect reverse sequence run hoga.

### 🚀 Application (Kahan use hota hai?)
* **Standard Network Troubleshooting:** CCNA, CCNP, aur CompTIA certifications me networking faults segmenting ke liye default reference framework.
* **Network Design Architecture:** Protocols standard design criteria check karne ke liye base model specifications matching.

---