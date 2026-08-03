---
title: "Topic 52 - Types of Routing (Static, Dynamic and Default Routing Detailed)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🛤️ 52. Types of Routing (Static, Dynamic and Default Routing Detailed)

### 📝 Introduction (Intro)
Networking me devices ke beech packets exchange path setup methods ke basis par **Routing** ko 3 primary types me divide kiya jata hai. Har type ka apna specific setup mechanism, control behavior aur adaptation parameters hote hain.

#### 🔑 The 3 Primary Types of Routing:
1. **Static Routing (Manual Configuration):**
   * *What is it:* Isme Network Administrator manually commands run karke har path ki entry routing table me write karta hai.
   * *Nature:* Non-adaptive (agar link down ho jaye, toh router automatic alternative path nahi dhoondh sakta).
2. **Dynamic Routing (Automatic & Adaptive):**
   * *What is it:* Routers dynamic routing protocols run karte hain jo neighboring devices ke sath coordinate hokar dynamic network status matrices (metric calculations) share karte hain.
   * *Subcategories:*
     - **Distance Vector Protocols:** Destination distance and direction check (e.g. RIP - Routing Information Protocol, uses hop count metric).
     - **Link State Protocols:** Complete topology map check (e.g. OSPF - Open Shortest Path First, uses cost metric based on bandwidth).
     - **Path Vector Protocols:** Path attributes analysis (e.g. BGP - Border Gateway Protocol, connecting different Autonomous Systems).
3. **Default Routing (Wildcard redirection):**
   * *What is it:* Jab router forwarding database table me specific IP network interface map entries missing hon, toh router packet drop karne ke bajay ek generic destination gateway address (**0.0.0.0/0**) par forward kar deta hai use **Default Route** kehte hain.

### ➕ Advantages (Fayde)
* **Static Routing:**
  - **No CPU/RAM Overhead:** Koi algorithms calculations background me run nahi hoti, routers resources full free rehte hain.
  - **High Security:** Administrator ke manually design paths ke alawa packets random spoof paths par bleed nahi ho sakte.
* **Dynamic Routing:**
  - **Self-Healing Capability:** Link fail hone par routes real-time me alternative lines par shift ho jate hain.
  - **Easy Management:** Hazaaron routers wale mesh network grid me manually configurations likhne ki jarurat nahi padti.
* **Default Routing:**
  - **Compact Routing Tables:** Edge routers par dynamic routes storage space memory limit reduce ho jati hai.

### ➖ Disadvantages (Nuksan)
* **Static Routing:**
  - **No scalability:** Bade enterprise network zones me isko setup karna impossible task ho jata hai (requires high human efforts).
  - **No automated recovery:** Lines physical break hone par path changes manual intervention mangte hain.
* **Dynamic Routing:**
  - **Resource consumption overhead:** Algorithms (Dijkstra SPF) run karne me server CPU utilization peaks aa sakti hain.
  - **Bandwidth Consumption:** Continuous network updates packages networks link capacity check lock karte hain.
* **Default Routing:**
  - **Routing Loop Risks:** Configuration error hone par packets routers ke beech circular loops structure me crash kar sakte hain.

### 📊 Diagram
Ye layout Static, Dynamic, aur Default routing setup formats comparison structures ko show karta hai:

```
[ Static Routing: Fixed manually configured line ]
Client Router Gi0/0 ================================> Target Server Network (192.168.2.0/24)

[ Dynamic Routing: Auto chooses best paths via OSPF/BGP metrics ]
Client Router ----> [ Router A (Path Cost: 10) ] ----> Target Network (192.168.2.0/24)
              ----> [ Router B (Path Cost: 50) ] ----/ (OSPF auto selects Router A path)

[ Default Routing: Unknown destinations sent to gateway ]
Home PC ----> Home Router ----> [ Default Route: 0.0.0.0/0 ] ----> ISP Gateway (Resolves everything)
```

### 💡 Real-world Example (Udaharan)
* **Office Commute Metaphors:**
  - **Static Routing:** Aapne dry route map paper par fix write kar liya ki office jaane ke liye hamesha Route 1 (Highway) hi lena hai. Highway close hone par bhi aap wait karenge jab tak rasta clear na ho (Manual path lock).
  - **Dynamic Routing:** Aap Google maps/navigator check karte hain. Agar live map notification aata hai ki Route 1 has high traffic delay, navigation line automatic Route 2 (Alternative street) choose kar legi (Adaptive auto path change).
  - **Default Routing (Drop Box):** Office me aapko nahi pata ki dynamic reports kis department employee ke pass deliver karni hai. Aap use simple **"Main Reception Desk Drop Box"** (Default Gateway) me drop kar dete hain, reception staff use automatic target desks send kar deta hai.

### 🚀 Application (Kahan use hota hai?)
* **Static Routing:** Stub networks (single gateway office outlets connecting to main branch).
* **Dynamic Routing:** High density multi-node ISP routing cores and global cloud grids.
* **Default Routing:** Home/office routers connecting local LANs to the public Internet ISPs.

---