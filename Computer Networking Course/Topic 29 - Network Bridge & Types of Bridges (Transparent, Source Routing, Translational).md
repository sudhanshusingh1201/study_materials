---
title: "Topic 29 - Network Bridge & Types of Bridges (Transparent, Source Routing, Translational)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🌉 29. Network Bridge & Types of Bridges (Transparent, Source Routing, Translational)

### 📝 Introduction (Intro)
**Bridge** ek intelligent hardware connection hardware device hai jo OSI Model ki **Data Link Layer (Layer 2)** par kaam karta hai. Iska primary objective ek hi network ke do different physical segments (ya do separate LANs) ko aapas me connect karna aur unke beech traffic stream ko **Filter** aur coordinate karna hai.

* **How it Works (MAC Address Table):** Hubs ke opposite, Bridge smart hota hai. Ye traffic observe karke automatic ek **MAC Address Table** generate kar leta hai. Jab segment A se data segment B ke kisi device ke liye dispatch hota hai, toh Bridge check karta hai:
  - *If target MAC is in Segment A:* Bridge door block kar deta hai (Filter), jisse data uselessly segment B me enter nahi karta.
  - *If target MAC is in Segment B:* Bridge frame ko aage route kar deta hai (Forward).

#### 🗂️ Types of Network Bridges:
1. **Transparent Bridge:** Ethernet networks me sabse popular. Ye systems ke liye completely invisible hota hai. Nodes ko pata bhi nahi chalta ki network me koi bridge install hai. Ye automatic data packets analysis se background me sources MAC tables learn, update, aur auto-refresh karta rehta hai.
2. **Source Routing Bridge:** Ye mostly legacy Token Ring networks standard ka part hai. Isme bridge intelligent nahi hota. Data transmission path routing ki complete information sender device frame ke andar specify karta hai, aur bridge use directly forward kar deta hai.
3. **Translational Bridge:** Ye do different topologies protocols structures (jaise ek side Ethernet network loop aur dusri side Token Ring network loop) ko interconnect karta hai. Ye link transition par frame formats and metadata convert/translate karta hai.

### ➕ Advantages (Fayde)
* **Collision Domain Segments:** Ye physical networks ko dynamic multiple collision domain segments me split karta hai, jisse localized packet collisions completely prevent hote hain.
* **Bandwidth Optimization:** Local segments traffic local limits me locked hone ke karan inter-segments paths par dynamic bandwidth free aur optimized rehti hai.
* **Geographical LAN Scaling:** Do normal LAN segments links setup join karke network loops range extend karta hai.

### ➖ Disadvantages (Nuksan)
* **Higher Latency (Slow processing):** Incoming frame ko completely read karna, MAC tables dynamic lookup lookup registers checks run karne me Hub ke comparison me zyada time lagta hai.
* **Broadcast Storm Vulnerability:** Bridge point-to-point traffic filter kar sakta hai, par broadcast addresses (FF-FF-FF-FF-FF-FF) ko filter nahi kar pata. Broadcast storm aane par bridge block crash ho sakta hai.
* **No IP Routing Power:** Ye globally different networks link nahi kar sakta (cannot route internet traffic), and routing tasks ke liye dynamic Layer 3 routers mandatory hote hain.

### 📊 Diagram
Ye layout do different LAN segments ke beech network traffic filtering aur forwarding structures ko show karta hai:

```mermaid
graph TD
    subgraph LAN Segment 1 (A & B)
        PCA[PC A] <--> Hub1[Local Hub 1]
        PCB[PC B] <--> Hub1
    end

    Hub1 <-->|Port 1| Bridge[Layer 2 Bridge <br> MAC Table: <br> Port 1: A, B <br> Port 2: C, D]
    
    subgraph LAN Segment 2 (C & D)
        Bridge <-->|Port 2| Hub2[Local Hub 2]
        PCC[PC C] <--> Hub2
        PCD[PC D] <--> Hub2
    end
```

### 💡 Real-world Example (Udaharan)
* **Office Wings Inter-Door Security Guard Metaphor:**
  - Maan lijiye ek block me do departments hain: **Marketing wing** aur **Accounts wing**. Dono corridors ek gate se separate hain.
  - **No Bridge (Hub):** Marketing wing ka har employee jab doosre se chilla kar baat karta hai, toh aawaz Accounts wing me bhi echo karti hai. Shor unbearable ho jata hai.
  - **Bridge (Security Guard):** Gate par ek guard khada kiya gaya jise dono compartments ke saare names listed hain. Jab Marketing member dynamic local room user ko bula raha hai, guard gate close rakhta hai (Filter). Par jab Marketing member Accounts member se consult chahta hai, guard name confirm karke lock open kar deta hai (Forward).

### 🚀 Application (Kahan use hota hai?)
* **LAN Segment separations:** Campus block internal sections local collision rates minimize karne ke liye.
* **Different Media Systems Link:** Ethernet systems ko localized coaxial or token ring networks interfaces se join karne me.
* **Modern Switch Base Concept:** Modern local switches basically high speed multi-port bridges hi hote hain jo dynamic software tables speed operations utilize karte hain.

---