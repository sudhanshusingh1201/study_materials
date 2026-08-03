---
title: "Topic 02 - Network Cables & Cabling Standards (Cat Ratings, UTPSTP, T568AB)"
tags:
  - networking
  - guide
  - study-material
type: guide-topic
---

← [[Computer Networking - Master Guide|Go Back to Networking Master Guide]]

# 🔌 2. Network Cables & Cabling Standards (Cat Ratings, UTP/STP, T568A/B)

Bhai, speed aur stability me physical cables ka koi tod nahi hai. 

### 🔀 Twisted Pair Cables (Ethernet)
Isme **8 copper wires** hote hain jo 4 pairs me twisted hote hain taaki electromagnetic interference (EMI/crosstalk) cancel out ho sake.
* **UTP (Unshielded Twisted Pair):** Normal ghar aur offices me use hone wale cheap aur flexible wires.
* **STP (Shielded Twisted Pair):** Wires ke upar metal foil ki shielding hoti hai. Factories ya server rooms me high interference se bachne ke liye use hote hain.

#### 📶 Ethernet Categories (Cat Ratings)
* **Cat 5e:** Max Speed 1 Gbps, Bandwidth 100 MHz, Max Distance 100m. (Standard Home Internet)
* **Cat 6:** Max Speed 10 Gbps (till 55m), Bandwidth 250 MHz. (Office Networks)
* **Cat 6a:** Max Speed 10 Gbps, Bandwidth 500 MHz, Max Distance 100m. (Server Rooms)
* **Cat 8:** Max Speed 40 Gbps, Bandwidth 2000 MHz, Max Distance 30m. (High-speed Data Centers)

### 🎨 T568A vs. T568B Wiring Standards
RJ45 connector ke end par wires ko order me lagane ke do standards hote hain. Inme **Orange aur Green pairs** aapas me swapped hote hain.

```
T568B (Standard) Pinout:
1. Orange-White | 2. Orange | 3. Green-White | 4. Blue | 5. Blue-White | 6. Green | 7. Brown-White | 8. Brown
```

#### 🔀 Cable Connection Types:
* **Straight-Through Cable:** Dono ends par same standard (T568B to T568B). Used to connect **different devices** (e.g., PC to Switch).
* **Crossover Cable:** Ek side T568A aur doosri side T568B. Used to connect **same devices** (e.g., PC to PC).
* **Rollover (Console) Cable:** Pins ka sequence ekdum reversed (Pin 1 to 8, Pin 2 to 7). Used to configure switch/router via CLI.

> [!TIP]
> **Auto-MDIX:** Modern switches automatically detect kar lete hain ki kaunsa wire connected hai aur internal hardware switch kar lete hain, isliye ab Crossover cables ki manual zaroorat nahi padti.

---