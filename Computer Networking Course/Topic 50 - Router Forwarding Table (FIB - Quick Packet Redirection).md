---
title: "Topic 50 - Router Forwarding Table (FIB - Quick Packet Redirection)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🧭 50. Router Forwarding Table (FIB - Quick Packet Redirection)

### 📝 Introduction (Intro)
**Router Forwarding Table** (jise **FIB - Forwarding Information Base** bhi kehte hain) router ke **Data Plane (Ya Forwarding Plane)** par chalne wali ek lightweight, highly-optimized look-up table hoti hai. Jab router ke pass koi IP packet aata hai, toh router is table ko check karke instantly decide karta hai ki packet ko kis exit interface (port) se bahar bhejna hai.

#### 🔑 Difference between Routing Table & Forwarding Table:
1. **Routing Table (RIB - Routing Information Base):** Ye router ke **Control Plane (Brain)** me hoti hai. Isme network ke saare possible paths aur dynamic routing protocols (OSPF, BGP, RIP) ki poori detail hoti hai. Ye static hoti hai aur complex calculation ke liye bani hoti hai.
2. **Forwarding Table (FIB):** RIB me se best path calculate karke jo simple aur fast lookup directory banti hai, use FIB kehte hain. Ye router ke hardware level (**ASIC chips/Data Plane**) par store hoti hai taaki packet processing me microsecond ka bhi lag na ho.

#### 🗂️ Typical Forwarding Table Columns:
* **Destination Network/Prefix:** Target IP address range (e.g. `192.168.2.0/24`).
* **Next Hop:** Agla router jahan packet bhejna hai (e.g. `10.0.0.2`).
* **Exit Interface (Port):** Router ka physical outgoing port (e.g. `GigabitEthernet0/1`).

### ➕ Advantages (Fayde)
* **Wire-Speed Packet Forwarding:** Hardware optimization ke jariye lookup fast hota hai, jisse millions of packets per second handle ho sakte hain.
* **Separation of Control & Data Planes:** Routing algorithms background me chalte hain, aur data planes directly independently packets forward karte hain. Ek plane me problem aane par doosra crash nahi hota.
* **LPM (Longest Prefix Match) Lookup:** Router table me checks matching layers chalata hai. Sabse matching specific IP mask subnet range select karke correct redirection guarantee karta hai.

### ➖ Disadvantages (Nuksan)
* **Hardware Memory Limits (TCAM):** Forwarding tables expensive hardware memory blocks (TCAM - Ternary Content-Addressable Memory) me save hoti hain. High routing tables size hone par memory full ho sakti hai.
* **Risk of Stale / Wrong Entries:** Agar routing database updates late milte hain, toh forwarding tables stale entries store rakhti hain, jisse **Routing Loops** ya data packet discard (Black Holes) ho jate hain.
* **CPU Overhead during Updates:** Jab dynamic updates RIB se FIB memory lines me push kiye jate hain, toh momentary interface CPU spikes aa sakte hain.

### 📊 Diagram
Ye layout Control Plane RIB se Data Plane FIB generation aur packet lookup logic steps ko show karta hai:

```
    [ CONTROL PLANE (RIB) ]
    Contains: OSPF, BGP database, static routes.
    Complex logic checks paths.
              |
              v (Generates best path cheatsheet)
    [ DATA PLANE (FIB / Forwarding Table) ]
    Stored in high-speed hardware memory (TCAM).
    
    --------------------------------------------------------
    | Destination Prefix | Next Hop IP  | Exit Interface   |
    |--------------------|--------------|------------------|
    | 192.168.1.0/24     | 10.0.0.2     | Gi0/1 (Port 1)   |
    | 172.16.0.0/16      | 20.0.0.5     | Gi0/2 (Port 2)   |
    --------------------------------------------------------
              ^
              | (Checks target IP: 192.168.1.50)
    [ Incoming Packet ] ===> [ Router Engine ] ===> [ Sends out of Gi0/1 (Port 1) ]
```

### 💡 Real-world Example (Udaharan)
* **Metro Station Departures Board vs Central Map:**
  - **Routing Table (RIB) = Metro System Map:** Isme poore shahar ke networks, saare lines, junction connections aur distance routes mapped hain. Ye kafi complex hai aur ise padhne me time lagta hai.
  - **Forwarding Table (FIB) = Exit Sign-Boards at Platform:** Jab aap platform par hote hain, aapko poora map dekhne ki zaroorat nahi hoti. Wahan simple sign-board likha hota hai: "Noida Sector-62 ke liye platform number 1 par jao". Aap instant sign dekhte hain aur platform 1 (Exit interface) ki taraf chale jate hain.
* **Post Office Sorting Bin Labels:** Sorting clerk ke table par ek quick sheet lagi hoti hai jisme likha hota hai: Pincode 110001 to 110050 goes to Box A. Clerk direct pin check karta hai aur direct Box A me packet drop kar deta hai, bina post office office hierarchy check kiye.

### 🚀 Application (Kahan use hota hai?)
* **Core Internet Routers:** Fast forwarding of global web traffic using massive FIB lookups.
* **Layer 3 Switches:** Forwarding IP packets inside enterprise corporate LANs at hardware bus speeds.
* **Software-Defined Networking (SDN):** Centralized controllers dynamically pushing FIB updates directly to dummy switch ports.

---