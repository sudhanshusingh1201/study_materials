---
title: "Topic 51 - Routing (Path Selection Process & Its Types)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🛣️ 51. Routing (Path Selection Process & Its Types)

### 📝 Introduction (Intro)
**Routing** computer networks me data packets ko source se destination tak pahunchane ke liye sabse optimal aur best path select karne ka process hai. Ye operation **Network Layer (Layer 3)** par hota hai. Jab multiple interconnected routers ke beech se packet ko pass hona hota hai, toh routing logic best intermediate steps/nodes decide karta hai.

#### 🔑 Key Concepts of Routing:
* **Routing vs Forwarding:**
  - **Routing:** Ye poore network map ko dekh kar source se destination tak ki complete road planning (path selection) hai. (Control Plane task).
  - **Forwarding:** Kisi specific router par packet aane par use local exit port par aage push kar dena. (Data Plane task).
* **Primary Types of Routing:**
  1. **Static Routing:** Isme network administrator manually router ke andar fixed paths configuration code likhta hai. Paths static rehte hain aur dynamic failures adjust nahi hote (Best for small networks).
  2. **Dynamic Routing:** Routers dynamic protocols (jaise RIP, OSPF, EIGRP, BGP) run karte hain jo aapas me updates share karke active pathways calculations and link status adapt karte hain.
  3. **Default Routing:** Agar destination network address router table me explicitly mapped na ho, toh packet ko default outgoing path (Gateway of Last Resort) par redirect kar diya jata hai.

### ➕ Advantages (Fayde)
* **Automatic Fault Tolerance (Redundancy):** Dynamic routing protocols agar kisi active link crash/failure ko sense karte hain, toh automatic packets stream ko backup pathways par route kar dete hain.
* **Enables Global Internet Scalability:** Pure world ke different autonomous systems (AS) BGP protocol ke routes link updates share karke interconnected internet run kar pate hain.
* **Bandwidth Optimization:** Dynamic metrics calculations (hops count, bandwidth, link delay checks) data load balance aur lines congestion limit handle karte hain.

### ➖ Disadvantages (Nuksan)
* **Resource Consumption Overhead:** Dynamic routing algorithms routers ke CPU aur RAM par significant load generate karte hain.
* **Network Bandwidth Loss:** Routers periodically updates exchange karne ke liye metadata broadcast networks control streams use karte hain, jo useful bandwidth consume karti hain.
* **Security vulnerabilities:** Agar malicious router line update join karke fake route updates push kare, toh routing redirection (Traffic interception or Black-holing) attacks ho sakte hain.

### 📊 Diagram
Ye layout Sender se Receiver tak dynamic routing path selection algorithms mapping options ko show karta hai:

```
                  [ Path A (High Speed Fiber - 3 Hops) ]
                 /                                      \
[ Sender Host ] ---- [ Router 1 ] ---- [ Router 2 ] ---- [ Router 3 ] ---\
        |                                                                 v
  [ IP Packet ]                                                    [ Receiver Host ]
        |                                                                 ^
        \---- [ Router 4 ] -------------- [ Router 5 ] ------------------/
                  [ Path B (Slow copper line - 2 Hops) ]
  
  * Routing Decision: Router metrics OSPF chooses Path A (more hops but super fast).
```

### 💡 Real-world Example (Udaharan)
* **Google Maps GPS Navigation Metaphor:**
  - **Static Routing:** Aapne ghar se office jaane ka ek shortcut rasta sheet paper par fix write kar liya. Lekin agar raste me heavy road repair construction work (link fail) chal raha ho, aap wahi fas jayenge kyuki aapko manually doosra path choose karna nahi aata.
  - **Dynamic Routing (Google Maps):** GPS dynamic network data checks live update leta hai. Aage traffic jam ya block hone par app instantly bolta hai: "Rerouting... taking alternative path to save 10 minutes."
* **Postal Courier Transit Hubs:** Jab aap speed post bhejte hain, har center (Sorting hub/Router) envelope ka destination state checks filter run karke use target cargo transport flights or trains routes par load karta hai.

### 🚀 Application (Kahan use hota hai?)
* **Global Internet Routing Backbone:** BGP protocol routing path computations connecting countries ISP networks.
* **Internal Company LAN/WAN Grids:** OSPF/EIGRP protocols load balancing internal server requests.
* **Home Gateway connections:** Default routing of local home devices to ISP gateway points.

---