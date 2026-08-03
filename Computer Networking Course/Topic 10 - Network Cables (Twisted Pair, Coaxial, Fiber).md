---
title: "Topic 10 - Network Cables (Twisted Pair, Coaxial, Fiber)"
tags:
  - networking
  - study-material
  - master-notes
type: course-topic
---

← [[Computer Networking - Study Notes|Go Back to Networking Hub]]

# 🔌 10. Network Cables (Twisted Pair, Coaxial, Fiber)

### 📝 Introduction (Intro)
Guided Media me network devices ke beech hardware connection banane ke liye **Network Cables** ka use kiya jata hai. Data ke physical transmission medium aur speed requirements ke base par teen main types ke network cables industry me use hote hain:

1. **Twisted Pair Cable (Ethernet):** Sabse zyada use hone wala cable. Isme **8 copper wires** hote hain jo 4 alag-alag pairs me twist (gundhe) hote hain. Twisted pattern background noise aur electromagnetic interference (EMI) ko cancel out karne me help karta hai.
   * **UTP (Unshielded Twisted Pair):** Cost-friendly aur flexible, bina outer metal shield ke.
   * **STP (Shielded Twisted Pair):** Har pair ke upar protective metal foil wrapping hoti hai jo static aur interference se bachaati hai.
   * **Cat Ratings (Categories):** Cat 5e (1 Gbps), Cat 6 (10 Gbps till 55m), Cat 6a (10 Gbps 100m), aur Cat 8 (40 Gbps 30m).
2. **Coaxial Cable:** Isme ek solid central copper core (wire) hota hai, jiske upar insulation dielectric plastic, ek metal braid shield, aur final plastic jacket hoti hai. Ye high-frequency dynamic analog/digital signals carry karta hai.
3. **Fiber Optic Cable:** Ye ultra-pure glass ya plastic ke behad patle (baal barabar) strands hote hain. Ye electric signals ke bajaye **Light pulses** (laser/LED) ke roop me data transmit karte hain. Ye **Total Internal Reflection (TIR)** ke principle par kaam karte hain.

### ➕ Advantages (Fayde)
* **Twisted Pair (Ethernet):** Sasta hota hai, install aur patch karna easy hai (uses simple RJ-45 plastic clips), aur office desks connect karne ke liye perfect hai.
* **Coaxial Cable:** Long-range coaxial TV feeds ke liye highly reliable hai, metal shielding ke karan outer noise impacts se isolated rehta hai.
* **Fiber Optic Cable:** Unmatched speeds (multiple terabits), long-range signals support (10km+ without signal booster), aur electromagnetic noise (EMI) se completely immune (neutral) kyunki isme physical electricity nahi balki light travel karti hai.

### ➖ Disadvantages (Nuksan)
* **Twisted Pair:** Range max **100 meters** tak limited hai (usse aage signal drop/attenuation hota hai), aur static high voltage signals se interferences aate hain.
* **Coaxial Cable:** Stiff (kathin/mota) hota hai, physical routers setup aur terminations hard hote hain, aur digital databases bulk routing me outdated ho chuka hai.
* **Fiber Optic Cable:** Behad expensive copper wires ke mukable, bending tolerance bahut sensitive hai (agar fiber jyada mod diya toh glass strands break ho jayenge), aur damage links ko jodne ke liye professional fusion splicing tools aur certified technician chahiye hote hain.

### 📊 Diagram
Ye teeno cables ke layer structures ko darshata hai:

```mermaid
graph TD
    subgraph Twisted Pair (Ethernet)
        Wires[8 Copper Wires in 4 Twisted Pairs] --> Conn[RJ-45 Plastic Connector]
    end

    subgraph Coaxial Cable Structure
        Core[Solid Copper Core] --- Ins[Dielectric Insulation] --- Shield[Metal Mesh Shield] --- Jack[Outer Jacket]
    end

    subgraph Fiber Optic Structure
        F_Core[Glass Core: Light Carrier] --- Clad[Cladding: Reflects Light back] --- Buff[Buffer Coating] --- F_Jack[Outer Protective Jacket]
    end
```

### 💡 Real-world Example (Udaharan)
* **Road Metaphor:**
  - **Twisted Pair = City Street:** Normal neighborhood and office traffic ke liye best hai, par high-speed highway connectivity nahi deta.
  - **Coaxial = Freight Railway Line:** Dedicated range lines (CCTV cameras ya cable network dish feeds) ke heavy load transfer utility.
  - **Fiber Optic = Hyperloop / Flight Tube:** Ultra-high speed direct connections bina traffic bottlenecks ke continents ke beech.
* **At Home Connections:** Local broadband operator aapke ghar ke pass pole se router tak patli black wire lata hai (Fiber Optic), aur router se aapke smart TV/Desktop PC tak connect hone wali yellow wire **Cat6 Ethernet** (Twisted Pair) hoti hai.

### 🚀 Application (Kahan use hota hai?)
* **Twisted Pair (Ethernet):** LAN connectivity local PC setups me router, switch, ya printer links ke liye.
* **Coaxial Cable:** Satellite Dish setup to Set-top box connections aur broadband Cable Modems.
* **Fiber Optic Cable:** Data Centers server racks backbone lines, Undersea Inter-continental Internet pipelines, aur FTTH (Fiber to the Home) modern high-speed broadband connections.

---