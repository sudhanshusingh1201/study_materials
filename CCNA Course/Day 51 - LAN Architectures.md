---
title: "Day 51 - LAN Architectures"
tags:
  - ccna
  - networking
  - study-material
  - cisco
  - jeremys-it-lab
type: course-topic
---

← [[Course on CCNA|Go Back to Course Hub]]

# 🌐 Day 51: LAN Architectures

Welcome to the notes for **Day 51: LAN Architectures** of Jeremy's IT Lab CCNA Complete Course! Aaj hum **Module 6: Advanced Architectures & Wireless** ko start karenge. Is lecture note mein hum seekhenge ki enterprise local networks kaise design kiye jate hain. Hum small office **SOHO** LANs, **Two-Tier (Collapsed Core)** architectures, **Three-Tier (Hierarchical)** structures, aur modern data center network layout **Spine-Leaf (Clos)** design ko network engineering guidelines, diagrams, aur comparisons ke sath detail mein cover karenge. Ye notes Hinglish language aur English/Latin script mein hain.

---

## 🚦 1. SOHO (Small Office / Home Office) LANs

**SOHO LANs** typically home networks ya very small office setups (1-10 users) hote hain.

*   **Integrated Devices:** In networks par standard huge switches aur separate routers nahi hote. Iske badle ek single **integrated device** (jaise standard home Wi-Fi router) use kiya jata hai.
*   **Multi-Function Unit:** Ye single device multiple capabilities combined display karta hai:
    1.  *Router:* Internet IP address connection translate and route karne ke liye.
    2.  *Switch:* Local wired devices (Smart TV, PC) connect karne ke liye.
    3.  *Access Point (AP):* Wireless Wi-Fi connections facilitate karne ke liye.
    4.  *DHCP & NAT Server:* Dynamic IP assign aur translation local level par automatic karne ke liye.

---

## 🏛️ 2. Two-Tier LAN Design (Collapsed Core)

Small to medium enterprises (100-1000 users) jahan separate core layers lagana cost-effective nahi hota, wahan **Two-Tier (Collapsed Core)** model standard hai.

```text
               +-----------------------------------+
               |  DISTRIBUTION LAYER / CORE LAYER  |  <-- Collapsed Core
               |     (Layer 3 Core Switches)       |      (Routing & Gateway)
               +-----------------------------------+
                                 |
                                 |  Dual redundant links
                                 |
                     +-----------------------+
                     |     ACCESS LAYER      |  <-- Layer 2 Access Switches
                     | (Connects to Host PCs)|      (Port Security & PoE)
                     +-----------------------+
```

### Two-Tier Layers Breakdown:
1.  **Access Layer:**
    *   Hosts (PCs, Printers, IP Phones) ko physical connectivity provide karta hai.
    *   *Features:* Port Security, Access VLANs membership, PoE support interfaces run hote hain. Layer 2 switches use hote hain.
2.  **Distribution Layer (Combined with Core = Collapsed Core):**
    *   Access switches ko aggregate (combine) karta hai.
    *   *Routing Boundary:* Layer 3 routing boundary yahan exist karti hai. Default gateways (using HSRP) and Inter-VLAN routing isi layer par process hote hain.
    *   *Security & Policies:* Access Control Lists (ACLs) and QoS policies execute ki jaati hain.

---

## 🧭 3. Three-Tier LAN Design (Hierarchical Model)

Large enterprise sites (multi-building campuses ya thousands of users) ke liye standard **Three-Tier (Hierarchical)** design recommend kiya jata hai:

```text
                     +-----------------------+
                     |      CORE LAYER       |  <-- High-Speed Backbone
                     |  (Speed Routing only) |      (No ACLs / No Filtering)
                     +-----------------------+
                                 |
                     +-----------------------+
                     |  DISTRIBUTION LAYER   |  <-- Layer 3 Routing Boundary
                     | (Aggregates Access)   |      (Gateway, QoS, ACLs)
                     +-----------------------+
                                 |
                     +-----------------------+
                     |     ACCESS LAYER      |  <-- Layer 2 Access Switch
                     | (Connects to Endpoints)|     (PoE, Port Security)
                     +-----------------------+
```

### Three-Tier Layers Details:
1.  **Access Layer:**
    *   *Function:* End-user device connection endpoints.
    *   *Device type:* Layer 2 switches (e.g. Cisco Catalyst 2960).
2.  **Distribution Layer:**
    *   *Function:* Access switches traffic aggregation, boundary routing, inter-VLAN routing, and security firewall/ACL policies.
    *   *Device type:* Multilayer (L3) switches (e.g. Cisco Catalyst 3850/9300).
3.  **Core Layer:**
    *   *Function:* **High-speed transport backbone**. Core layer ka ek hi goal hota hai—packets ko ek distribution block se doosre block tak jitni jaldi ho sake route (forward) karna.
    *   *Core Rule:* **No slow packet operations!** Core switches par kabhi bhi time-consuming policies (jaise ACL packet filtering, traffic shaping/policing, or security scans) apply nahi karni chahiye taaki speed and latency optimum rahe.

---

## 🕸️ 4. Spine-Leaf Architecture (Data Center Design)

Enterprise data centers mein server systems virtual machines host karte hain jahan server-to-server traffic (**East-West Traffic**) bahut heavy hota hai. Traditional 3-tier models is traffic load ke chalte STP blocks aur varying latencies create karte hain. Isko bypass karne ke liye **Spine-Leaf (Clos)** design use hota hai:

```text
               +---------------+     +---------------+
               |   SPINE 1     |     |   SPINE 2     |  <-- Spine Layer
               +---------------+     +---------------+  (No direct connections)
                 /     \               /     \
                /       \             /       \   (Full-Mesh mesh between layers)
               /         \           /         \
       +---------------+   +---------------+   +---------------+
       |    LEAF 1     |   |    LEAF 2     |   |    LEAF 3     |  <-- Leaf Layer
       +---------------+   +---------------+   +---------------+
         |           |       |           |       |           |
      [Server1]  [Server2] [Server3]  [Server4] [Server5]  [Server6]
```

### Spine-Leaf Architecture Rules:
1.  **Leaf Layer Switches:**
    *   Dono targets (Servers, Firewalls, storage arrays) ko directly physical connectivity identify karte hain.
    *   **Rule:** Har Leaf switch **network ke saare Spine switches se directly connected** hota hai. Leaf switches aapas mein direct wire connects nahi rakhte.
2.  **Spine Layer Switches:**
    *   Backbone forwarding plane jahan high-speed routing run hoti hai.
    *   **Rule:** No direct connection between Spine switches. No direct host connections.
3.  **Predictable Latency:**
    *   Kyunki har leaf switch har spine se connected hai, isliye network par connected Server-1 se Server-6 tak jane ke liye packet ko hamesha **exact 2-hops** (Leaf-1 $\rightarrow$ Spine $\rightarrow$ Leaf-3) hi travel karna padega. Latency constant/predictable rehti hai.
    *   **No STP Blockage:** DAI aur loop routing protocols ke badle yahan Layer 3 routing (like OSPF/IS-IS) with **ECMP (Equal-Cost Multi-Pathing)** chalaya jata hai, jisse saare redundant links active status par data load balance karte hain.

---

## 📝 5. CCNA Day 51 Practice Questions

1. **Q1: SOHO LAN environment mein integrated dynamic devices router switches capabilities ke alawa kis local wireless interface element ko hold karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **WAP (Wireless Access Point)** capability.
   </details>

2. **Q2: Two-Tier network architecture design mein, 'Collapsed Core' term kis specific layers ke integration segment ko denote karti hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Core Layer** aur **Distribution Layer** ko aggregate karke single layer banana.
   </details>

3. **Q3: Three-Tier Hierarchical model mein switch interface port security and PoE policies kis layer par configure ki jaati hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Access Layer** switches par.
   </details>

4. **Q4: Hierarchical design rules ke mutabik, Three-Tier model ke 'Core Layer' switches par ACLs ya traffic policing policies configure karna kyu forbidden hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Kyunki Core layer ka objective **high-speed packet forwarding** hai. ACL calculations ya filtering processes switches processor bandwidth consume karke transit latency badha dete hain.
   </details>

5. **Q5: Data center environments par adjacent server nodes ke aapas mein communications traffic flow lines ko network terminologies mein kya bolte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **East-West Traffic** (Server-to-Server communication). LAN to external Web (client-to-server) ko **North-South Traffic** kehte hain.
   </details>

6. **Q6: Spine-Leaf (Clos) architecture design rules ke core mutabik, dynamic switch mappings structures connections kis line configuration logic ko strictly reject karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Leaf switches aapas mein connect nahi ho sakte aur Spine switches aapas mein directly physical cable connect nahi kar sakte.
   </details>

7. **Q7: Spine-Leaf topology designs networks par server-to-server connection paths ke dynamic hops lengths kya constant scale show karte hain?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Exact 2 Hops** distance (Leaf-1 $\rightarrow$ Spine $\rightarrow$ Leaf-2). Isse data transmission latency completely predictable aur minimal level par maintain rehti hai.
   </details>

8. **Q8: Spine-Leaf architectures links utilization verify karne ke liye STP blocks dynamic interfaces logic bypass kar dynamic redundant path sharing implement karne ke liye kis technique ka use kiya jata hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** Layer 3 routing protocols run karke **ECMP (Equal-Cost Multi-Pathing)** status configure karna (jis se switch aapas mein saare backup links active bandwidth use kar sakein).
   </details>

9. **Q9: Multilayer Switches core network zones (e.g. Cisco Catalyst 9300) standard hierarchical design checks ke dynamic classifications maps mein kis layer par look kiya jata hai?**
   <details>
   <summary>🔓 Click to Reveal Answer</summary>
   **Answer:** **Distribution Layer** par.
   </details>

10. **Q10: SOHO routers external Internet service connectivity transitions perform karne ke liye local network parameters boundaries par kis IP management framework protocol settings ka use karte hain?**
    <details>
    <summary>🔓 Click to Reveal Answer</summary>
    **Answer:** **NAT (Network Address Translation)** and DHCP services.
    </details>
