---
title: "Topic 17 - SONET & Frame Relay (WAN Carrier Systems)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🌉 17. SONET & Frame Relay (WAN Carrier Systems)

### 📝 Introduction (Intro)
WAN core communication me high-speed data transmission pipelines aur private networks connectivity ke liye do major legacy standards develop kiye gaye the:

1. **SONET (Synchronous Optical Network):** SONET (jis ka European equivalent **SDH - Synchronous Digital Hierarchy** hai) optical fibers par extremely high-speed signals transfer karne ke liye ek standardization specification protocol hai. Ye Layer 1 (Physical Layer) standard hai. Ye multiple low-speed streams ko multiplex karke single optical path par sync clocks synchronization ke jariye bhejta hai.
2. **Frame Relay:** Frame Relay ek highly cost-effective Layer 2 (Data Link Layer) packet-switching network standard hai jise 1990s me customers ke geographical WAN offices ko aapas me connect karne ke liye design kiya gaya tha. Isme virtual circuits (PVCs) aur **DLCI (Data Link Connection Identifier)** addresses use hote the taaki shared carrier lines par multiple users ka data separation se travel kar sake.

### ➕ Advantages (Fayde)
#### SONET:
* **Self-Healing Rings Reliability:** SONET setups me dual counter-rotating fiber loops use hote hain. Agar main fiber wire physically break ho jaye, toh controller dynamic traffic reverse route par switch kar deta hai under **50 milliseconds** (Self-healing).
* **Massive Bandwidths:** Gigabits se lekar terabits per second speeds support karta hai (measured in OC - Optical Carrier levels, e.g. OC-192 = 9.95 Gbps).

#### Frame Relay:
* **Cost Efficiency:** Alag-alag branches ke liye dedicated point-to-point leased copper lines purchase karne ke mukable shared bandwidth structure me kafi sasta padta tha.
* **Committed Information Rate (CIR):** Customer requirements ke according speed allocation dynamic control kar sakte the, with capability to burst higher speeds under low traffic congestion.

### ➖ Disadvantages (Nuksan)
#### SONET:
* **Complex Synchronization:** Network me har node ka clock strictly time-synced hona zaroori hai. Hardware control installations and maintenance processes extreme level complex aur costly hote hain.
* **Overhead Sizes:** Continuous timing sync headers add karne ke karan packet payload data usage efficient nahi rehti thi.

#### Frame Relay:
* **No Error Recovery Protocols:** Ye raste me damaged frames check karke direct drop kar deta tha, but replacement frame re-send karne ka dynamic system upper layers (TCP) ko handle karna padta tha.
* **Obsolete Technology:** Modern broadband networks, fiber optics, MPLS, aur SD-WAN systems ke development ke baad Frame Relay industry se completely dead aur replace ho chuki hai.

### 📊 Diagram
Ye SONET ke dual-ring backup architecture aur Frame Relay shared virtual cloud connectivity layouts ko represent karta hai:

```mermaid
graph TD
    subgraph SONET Ring (Layer 1 Dual-Ring Loop)
        NodeA[Router Node A] <-->|Primary Ring - Clockwise| NodeB[Router Node B]
        NodeB <-->|Primary Ring| NodeC[Router Node C]
        NodeC <-->|Primary Ring| NodeA
        
        NodeA -.->|Backup Ring - Counter Clockwise| NodeC
        NodeC -.->|Backup Ring| NodeB
        NodeB -.->|Backup Ring| NodeA
    end

    subgraph Frame Relay WAN (Layer 2 Packet Switching)
        HQ[Corporate HQ Router] <-->|DLCI 100| FR_Cloud((Frame Relay WAN Cloud))
        FR_Cloud <-->|DLCI 200| Branch[Branch Office Router]
    end
```

### 💡 Real-world Example (Udaharan)
* **Bullet Train vs. Shared Cargo Van:**
  - **SONET = High-Speed Loop Train:** Ek high-tech bullet train jo closed loops me micro-second precision schedule (Synchronous) ke sath chalti hai. Agar main track block ho, toh systems turn-table se train backup parallel loop track par instantly run kar dete hain.
  - **Frame Relay = Shared Courier Service (DHL/FedEx):** Ek hi common delivery truck me alag-alag offices ke small packages (frames) unke box tags (DLCI IDs) ke jariye target branches tak route hote hain. Dedicated cargo hire karne se sasta hai, par parcel damaged hone par courier company direct return-refund process nahi karegi (no error correction).

### 🚀 Application (Kahan use hota hai?)
* **SONET/SDH Applications:**
  - **Telco Core Backbones:** Telecom cellular operators ke high density dynamic inter-city voice and data transit trunks.
  - **Undersea optical cables:** Continents links ko high bandwidth rings se redundant banana.
* **Frame Relay Applications (Historical):**
  - **1990s Corporate WANs:** Banking centers aur billing structures ko 90s me connect karne ka main tool (replaced by MPLS).

---